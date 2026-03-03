# SparkMedia.ai Website

Professional static website for SparkMedia.ai built with Hugo and deployed to GitHub Pages.

## Overview

This website showcases SparkMedia.ai's specialized Google Ads and SEO services for plumbing businesses. The site features a modern, responsive design with a magenta/cyan color scheme that reflects the brand identity.

## Features

- **Responsive Design**: Mobile-first approach that works on all devices
- **Professional Layout**: Clean, modern design that establishes credibility
- **Brand Colors**: Magenta/cyan color scheme matching SparkMedia.ai branding
- **Key Pages**:
  - Homepage with value proposition and call-to-action
  - Services page focused on plumbing business marketing
  - Free audit/consultation page
  - About page with company story and team
  - Contact page with form and contact information
- **GitHub Pages Deployment**: Automatic deployment via GitHub Actions
- **Custom Domain Ready**: Configured for sparkmedia.ai domain

## Technology Stack

- **Hugo**: Static site generator (v0.157.0)
- **GitHub Pages**: Hosting and deployment
- **GitHub Actions**: CI/CD pipeline
- **Custom Theme**: SparkMedia.ai brand-specific theme
- **Vanilla CSS**: Custom styling with CSS variables for theming

## Local Development

### Prerequisites

- Hugo v0.157.0 or later
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sparkmediaai/sparkmedia-website.git
   cd sparkmedia-website
   ```

2. Run the development server:
   ```bash
   hugo server --buildDrafts
   ```

3. Open http://localhost:1313 in your browser

### Building for Production

```bash
hugo --minify
```

The built site will be in the `public/` directory.

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch. The deployment workflow is configured in `.github/workflows/hugo.yml`.

### Manual Deployment

1. Build the site:
   ```bash
   hugo --minify
   ```

2. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update website"
   git push origin main
   ```

## Custom Domain Setup

To use the custom domain `sparkmedia.ai`:

1. **DNS Configuration**:
   - Add a CNAME record pointing `sparkmedia.ai` to `sparkmediaai.github.io`
   - Add a CNAME record pointing `www.sparkmedia.ai` to `sparkmediaai.github.io`

2. **GitHub Pages Configuration**:
   - Go to repository Settings → Pages
   - Under "Custom domain", enter `sparkmedia.ai`
   - Check "Enforce HTTPS"

3. **Update Hugo Configuration**:
   - Update `baseURL` in `hugo.toml` to `https://sparkmedia.ai/`

## Site Structure

```
sparkmedia-website/
├── content/           # Page content (Markdown)
│   ├── services.md
│   ├── free-audit.md
│   ├── about.md
│   └── contact.md
├── themes/
│   └── sparkmedia-theme/  # Custom theme
│       ├── layouts/       # HTML templates
│       └── static/        # Static assets
├── public/            # Built site (generated)
├── hugo.toml         # Site configuration
└── .github/workflows/
    └── hugo.yml      # GitHub Actions workflow
```

## Brand Guidelines

- **Primary Color**: Magenta (#FF00FF)
- **Secondary Color**: Cyan (#00FFFF)
- **Accent Color**: Dark Gray (#333333)
- **Light Background**: Light Gray (#F8F9FA)
- **Typography**: System font stack (sans-serif)

## License

© 2026 SparkMedia.ai. All rights reserved.