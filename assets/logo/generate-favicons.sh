#!/bin/bash
# Favicon generation script for SparkMedia.AI
# Requires: ImageMagick (convert command)

echo "Generating favicon files from SVG..."

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo "Error: ImageMagick is not installed."
    echo "Install it with: sudo apt-get install imagemagick (Ubuntu/Debian)"
    echo "Or download from: https://imagemagick.org/"
    exit 1
fi

# Create favicon.ico (multiple sizes in one file)
echo "Creating favicon.ico (16x16, 32x32, 48x48)..."
convert sparkmedia-icon.svg -resize 16x16 favicon-16.png
convert sparkmedia-icon.svg -resize 32x32 favicon-32.png
convert sparkmedia-icon.svg -resize 48x48 favicon-48.png
convert favicon-16.png favicon-32.png favicon-48.png favicon.ico

# Create individual PNG favicons
echo "Creating PNG favicons..."
convert sparkmedia-icon.svg -resize 16x16 favicon-16x16.png
convert sparkmedia-icon.svg -resize 32x32 favicon-32x32.png
convert sparkmedia-icon.svg -resize 64x64 favicon-64x64.png
convert sparkmedia-icon.svg -resize 128x128 favicon-128x128.png

# Create Apple Touch Icon (180x180)
echo "Creating Apple Touch Icon..."
convert sparkmedia-icon.svg -resize 180x180 apple-touch-icon.png

# Create Android Chrome icons
echo "Creating Android Chrome icons..."
convert sparkmedia-icon.svg -resize 192x192 android-chrome-192x192.png
convert sparkmedia-icon.svg -resize 512x512 android-chrome-512x512.png

# Create social media icons
echo "Creating social media icons..."
convert sparkmedia-icon.svg -resize 1200x630 -background "#0C0F14" -gravity center -extent 1200x630 og-image.png
convert sparkmedia-icon.svg -resize 400x400 twitter-card.png

# Clean up temporary files
rm -f favicon-16.png favicon-32.png favicon-48.png

echo "Favicon generation complete!"
echo ""
echo "Files created:"
echo "  favicon.ico              - Standard favicon (multiple sizes)"
echo "  favicon-16x16.png        - 16x16 favicon"
echo "  favicon-32x32.png        - 32x32 favicon"
echo "  favicon-64x64.png        - 64x64 favicon"
echo "  favicon-128x128.png      - 128x128 favicon"
echo "  apple-touch-icon.png     - Apple Touch Icon (180x180)"
echo "  android-chrome-192x192.png - Android Chrome icon"
echo "  android-chrome-512x512.png - Android Chrome icon"
echo "  og-image.png             - Open Graph image (1200x630)"
echo "  twitter-card.png         - Twitter card image (400x400)"
echo ""
echo "To use these favicons, add to your HTML head:"
echo ""
echo "<link rel=\"icon\" href=\"assets/logo/favicon.ico\" sizes=\"any\">"
echo "<link rel=\"icon\" href=\"assets/logo/favicon-32x32.png\" type=\"image/png\" sizes=\"32x32\">"
echo "<link rel=\"icon\" href=\"assets/logo/favicon-16x16.png\" type=\"image/png\" sizes=\"16x16\">"
echo "<link rel=\"apple-touch-icon\" href=\"assets/logo/apple-touch-icon.png\">"
echo "<link rel=\"manifest\" href=\"assets/logo/site.webmanifest\">"