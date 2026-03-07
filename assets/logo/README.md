# SparkMedia.AI Logo Assets

Professional logo system for SparkMedia.AI with dark cinematic theme.

## Color Palette
- **Primary Pink**: `#FF005C`
- **Secondary Cyan**: `#00C2FF` 
- **Background Dark**: `#0C0F14`
- **Gradient**: `#FF005C` → `#00C2FF`

## Files Included

### SVG Files (Vector)
1. **`sparkmedia-logo.svg`** - Full logo with text and icon
   - Dimensions: 400x120px
   - Usage: Website headers, footers, print materials
   
2. **`sparkmedia-icon.svg`** - Icon-only version
   - Dimensions: 100x100px
   - Usage: Favicons, social media, small spaces

### PNG Files (To be generated)
Run the generation script to create PNG files:
```bash
cd assets/logo/
./generate-favicons.sh
```

### Generated Files (after running script)
- `favicon.ico` - Standard favicon (16x16, 32x32, 48x48)
- `favicon-16x16.png` - 16x16 favicon
- `favicon-32x32.png` - 32x32 favicon
- `apple-touch-icon.png` - Apple Touch Icon (180x180)
- `android-chrome-192x192.png` - Android Chrome icon
- `android-chrome-512x512.png` - Android Chrome icon
- `og-image.png` - Open Graph image (1200x630)
- `twitter-card.png` - Twitter card image (400x400)

## Usage Guidelines

### Website Implementation
Add to your HTML `<head>` section:

```html
<!-- Favicons -->
<link rel="icon" href="assets/logo/favicon.ico" sizes="any">
<link rel="icon" href="assets/logo/favicon-32x32.png" type="image/png" sizes="32x32">
<link rel="icon" href="assets/logo/favicon-16x16.png" type="image/png" sizes="16x16">
<link rel="apple-touch-icon" href="assets/logo/apple-touch-icon.png">

<!-- Web App Manifest -->
<link rel="manifest" href="assets/logo/site.webmanifest">

<!-- Open Graph / Twitter Cards -->
<meta property="og:image" content="assets/logo/og-image.png">
<meta name="twitter:image" content="assets/logo/twitter-card.png">
```

### Logo Usage Rules
1. **Minimum Clear Space**: Maintain 20px clear space around logo
2. **Minimum Size**: 
   - Full logo: 200px width minimum
   - Icon: 32px width minimum
3. **Backgrounds**: Optimized for dark backgrounds (#0C0F14)
4. **Do Not**:
   - Alter colors
   - Stretch or distort
   - Add effects or shadows
   - Rotate or skew
   - Place on busy backgrounds

### Social Media
- **Profile Pictures**: Use `sparkmedia-icon.svg` (scaled appropriately)
- **Cover Images**: Use `sparkmedia-logo.svg` with sufficient clear space
- **Posts**: Use full logo when space allows, otherwise use icon

## Design Specifications

### Logo Elements
1. **Spark Icon**: Represents energy, innovation, and AI spark
2. **Typography**: Inter font family, bold weight for impact
3. **Gradient**: Pink-to-cyan gradient represents AI fusion
4. **Modern Style**: Clean, tech-forward, cinematic aesthetic

### Responsive Scaling
The SVG logos scale perfectly at any size. For raster images:
- Web: 2x resolution for retina displays
- Print: 300 DPI minimum
- Mobile: Test at various breakpoints

## Preview
Open `logo-preview.html` in a browser to see all logo variations and usage examples.

## License
These logo assets are proprietary to SparkMedia.AI and may only be used for official SparkMedia.AI branding and marketing materials.