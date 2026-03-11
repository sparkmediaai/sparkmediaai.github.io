# Implementation Guide: Replace Floating Cards

## Quick Start (Option 1 - Recommended)

### 1. Add CSS File
Add this to your `<head>` section in `index.html`:
```html
<link rel="stylesheet" href="css/modern-features.css">
```

### 2. Replace Floating Cards Section
Find this section in your HTML (around line 160-220):
```html
<div class="floating-cards-container">
    <a href="industries.html" class="floating-card card-1">...</a>
    <a href="industries.html" class="floating-card card-2">...</a>
    <a href="industries.html" class="floating-card card-3">...</a>
    <a href="industries.html" class="floating-card card-4">...</a>
</div>
```

Replace it with:
```html
<!-- Modern Feature Grid -->
<div class="features-grid">
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3 class="feature-title">Lead Capture</h3>
        <p class="feature-description">AI-powered lead qualification and routing</p>
        <a href="/services#lead-capture" class="feature-link">Learn more</a>
    </div>
    
    <div class="feature-card">
        <div class="feature-icon">⚙️</div>
        <