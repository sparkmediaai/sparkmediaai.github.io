#!/bin/bash

# Test script for SparkMedia.ai website

echo "Testing SparkMedia.ai website..."
echo "================================"

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "❌ Hugo is not installed"
    exit 1
else
    echo "✅ Hugo is installed: $(hugo version)"
fi

# Check if we're in the right directory
if [ ! -f "hugo.toml" ]; then
    echo "❌ Not in website directory (hugo.toml not found)"
    exit 1
else
    echo "✅ In website directory"
fi

# Check if theme exists
if [ ! -d "themes/sparkmedia-theme" ]; then
    echo "❌ Theme not found"
    exit 1
else
    echo "✅ Theme found"
fi

# Check if content exists
if [ ! -f "content/services.md" ]; then
    echo "❌ Content files missing"
    exit 1
else
    echo "✅ Content files found"
fi

# Build the site
echo "Building site..."
hugo --minify

if [ $? -eq 0 ]; then
    echo "✅ Site built successfully"
    
    # Check if public directory was created
    if [ -d "public" ]; then
        echo "✅ Public directory created"
        
        # Count files
        file_count=$(find public -type f | wc -l)
        echo "📁 $file_count files generated"
        
        # Check key pages
        echo "Checking key pages..."
        pages=("index.html" "services/index.html" "free-audit/index.html" "about/index.html" "contact/index.html")
        
        for page in "${pages[@]}"; do
            if [ -f "public/$page" ]; then
                echo "  ✅ $page"
            else
                echo "  ❌ $page (missing)"
            fi
        done
        
        # Check for CNAME file
        if [ -f "public/CNAME" ]; then
            echo "✅ CNAME file present"
        else
            echo "⚠️  CNAME file missing"
        fi
        
        # Check for .nojekyll file
        if [ -f "public/.nojekyll" ]; then
            echo "✅ .nojekyll file present"
        else
            echo "⚠️  .nojekyll file missing"
        fi
        
    else
        echo "❌ Public directory not created"
        exit 1
    fi
else
    echo "❌ Build failed"
    exit 1
fi

echo ""
echo "Test completed successfully!"
echo ""
echo "Next steps:"
echo "1. Commit and push to GitHub"
echo "2. Configure GitHub Pages in repository settings"
echo "3. Set up custom domain (sparkmedia.ai)"
echo "4. Test live site"
echo ""
echo "For detailed instructions, see DEPLOYMENT.md"