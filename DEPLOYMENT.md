# Deployment Guide for SparkMedia.ai Website

This guide provides step-by-step instructions for deploying the SparkMedia.ai website to GitHub Pages and configuring a custom domain.

## Prerequisites

1. **GitHub Account**: `sparkmediaai` account with repository access
2. **Repository**: `sparkmedia-website` (private repository)
3. **Domain**: `sparkmedia.ai` (registered with a domain registrar)

## Step 1: Create GitHub Repository

1. Log in to GitHub as `sparkmediaai`
2. Create a new private repository named `sparkmedia-website`
3. Initialize with README (optional)

## Step 2: Push Website Code

```bash
# Clone this repository locally (if not already done)
git clone https://github.com/sparkmediaai/sparkmedia-website.git
cd sparkmedia-website

# Add all files and commit
git add .
git commit -m "Initial SparkMedia.ai website"

# Push to GitHub
git push origin main
```

## Step 3: Configure GitHub Pages

1. Go to repository Settings → Pages
2. Under "Build and deployment":
   - Source: **GitHub Actions**
   - Branch: **main**
3. Save configuration

## Step 4: Verify GitHub Actions Workflow

1. Go to repository Actions tab
2. You should see the "Deploy Hugo site to Pages" workflow running
3. Wait for it to complete (should take 2-3 minutes)
4. Once complete, the site will be available at:
   - `https://sparkmediaai.github.io`

## Step 5: Custom Domain Configuration

### DNS Configuration (at Domain Registrar)

Add the following DNS records:

| Type  | Name                | Value                      | TTL   |
|-------|---------------------|----------------------------|-------|
| CNAME | sparkmedia.ai       | sparkmediaai.github.io     | 3600  |
| CNAME | www.sparkmedia.ai   | sparkmediaai.github.io     | 3600  |
| A     | sparkmedia.ai       | 185.199.108.153            | 3600  |
| A     | sparkmedia.ai       | 185.199.109.153            | 3600  |
| A     | sparkmedia.ai       | 185.199.110.153            | 3600  |
| A     | sparkmedia.ai       | 185.199.111.153            | 3600  |

**Note**: Use either CNAME or A records, not both. CNAME is recommended for simplicity.

### GitHub Pages Custom Domain

1. Go to repository Settings → Pages
2. Under "Custom domain", enter: `sparkmedia.ai`
3. Check "Enforce HTTPS"
4. Save configuration

### Update Hugo Configuration

Update the `baseURL` in `hugo.toml`:

```toml
baseURL = 'https://sparkmedia.ai/'
```

Commit and push this change:

```bash
git add hugo.toml
git commit -m "Update baseURL for custom domain"
git push origin main
```

## Step 6: Verify Deployment

1. Wait for DNS propagation (up to 48 hours, usually 1-2 hours)
2. Test the website:
   - `https://sparkmedia.ai`
   - `https://www.sparkmedia.ai`
3. Verify HTTPS is working (padlock icon in browser)
4. Test all pages and forms

## Step 7: Post-Deployment Checklist

- [ ] Website loads at `https://sparkmedia.ai`
- [ ] HTTPS is enforced (no mixed content warnings)
- [ ] All pages render correctly
- [ ] Navigation works on mobile and desktop
- [ ] Contact form displays correctly (note: requires backend for functionality)
- [ ] Google Analytics is configured (if needed)
- [ ] SEO meta tags are present
- [ ] Site loads quickly (under 3 seconds)

## Troubleshooting

### GitHub Pages Not Building

1. Check Actions tab for workflow errors
2. Verify `hugo.toml` has correct configuration
3. Ensure theme is properly configured

### Custom Domain Not Working

1. Verify DNS records have propagated using `dig sparkmedia.ai`
2. Check GitHub Pages custom domain configuration
3. Wait up to 24 hours for full propagation

### HTTPS Not Working

1. Ensure "Enforce HTTPS" is checked in GitHub Pages settings
2. Wait for SSL certificate provisioning (automatic with GitHub Pages)
3. Clear browser cache and try again

### Contact Form Not Functional

The contact form is front-end only. For production use, you need to:

1. Set up a form backend (Formspree, Netlify Forms, etc.)
2. Update the form action URL in `contact.md`
3. Or implement a serverless function (AWS Lambda, Vercel, etc.)

## Maintenance

### Updating Content

1. Edit Markdown files in `content/` directory
2. Commit and push changes
3. GitHub Actions will automatically rebuild and deploy

### Updating Design

1. Edit CSS in theme files
2. Update templates in `themes/sparkmedia-theme/layouts/`
3. Test locally with `hugo server`
4. Commit and push changes

### Adding New Pages

```bash
# Create new page
hugo new content/new-page.md

# Edit the generated file
# Commit and push
```

## Monitoring

1. **GitHub Actions**: Monitor build status
2. **Google Search Console**: Submit sitemap and monitor indexing
3. **Google Analytics**: Track traffic and conversions
4. **Uptime Monitoring**: Use services like UptimeRobot

## Backup

The repository itself serves as backup. For additional safety:

1. Regular commits to main branch
2. Consider branching strategy for major changes
3. Backup domain registrar credentials separately

## Support

For issues with deployment:
1. Check GitHub Actions logs
2. Review Hugo documentation
3. Contact GitHub Support for Pages issues
4. Contact domain registrar for DNS issues