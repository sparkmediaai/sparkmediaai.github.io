/* ==========================================================================
   SPARKMEDIA.AI - MAIN JAVASCRIPT
   Version: 1.0.0
   Description: Interactive elements, animations, and performance optimizations
   ========================================================================== */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('SparkMedia.ai - Premium Homepage Loaded');
    
    // Initialize all components
    initHeaderScroll();
    initMobileMenu();
    initSmoothScroll();
    initCountUpAnimations();
    initHoverEffects();
    initIntersectionObserver();
    initCTAButtons();
});

/* ==========================================================================
   HEADER SCROLL EFFECT
   ========================================================================== */
function initHeaderScroll() {
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

/* ==========================================================================
   MOBILE MENU TOGGLE
   ========================================================================== */
function initMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    if (!menuBtn || !navLinks) return;

    const mobileQuery = window.matchMedia('(max-width: 900px)');
    const dropdowns = document.querySelectorAll('.dropdown');
    let backdrop = document.querySelector('.mobile-menu-backdrop');

    if (!backdrop) {
        backdrop = document.createElement('div');
        backdrop.className = 'mobile-menu-backdrop';
        document.body.appendChild(backdrop);
    }

    const closeMenu = () => {
        menuBtn.classList.remove('active');
        navLinks.classList.remove('is-open');
        menuBtn.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('nav-open');
        backdrop.classList.remove('is-visible');
        dropdowns.forEach(dropdown => dropdown.classList.remove('active'));
    };

    const openMenu = () => {
        menuBtn.classList.add('active');
        navLinks.classList.add('is-open');
        menuBtn.setAttribute('aria-expanded', 'true');
        document.body.classList.add('nav-open');
        backdrop.classList.add('is-visible');
    };

    const toggleMenu = (event) => {
        if (event) {
            event.preventDefault();
            event.stopPropagation();
        }

        if (menuBtn.classList.contains('active')) {
            closeMenu();
        } else {
            openMenu();
        }
    };

    const handleViewportChange = (event) => {
        if (!event.matches) {
            closeMenu();
            dropdowns.forEach(dropdown => dropdown.classList.remove('active'));
        }
    };

    menuBtn.setAttribute('aria-expanded', 'false');
    menuBtn.addEventListener('click', toggleMenu);
    menuBtn.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
            toggleMenu(event);
        }
    });

    backdrop.addEventListener('click', closeMenu);

    document.addEventListener('click', (event) => {
        if (!menuBtn.contains(event.target) && !navLinks.contains(event.target)) {
            closeMenu();
        }
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            closeMenu();
        }
    });

    if (mobileQuery.addEventListener) {
        mobileQuery.addEventListener('change', handleViewportChange);
    } else if (mobileQuery.addListener) {
        mobileQuery.addListener(handleViewportChange);
    }

    dropdowns.forEach(dropdown => {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        if (!toggle) return;

        toggle.addEventListener('click', function(e) {
            if (!mobileQuery.matches) return;
            e.preventDefault();
            e.stopPropagation();
            dropdown.classList.toggle('active');
        });
    });
}

/* ==========================================================================
   SMOOTH SCROLL FOR ANCHOR LINKS
   ========================================================================== */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (!targetElement) return;
            
            // Calculate header offset
            const headerHeight = document.querySelector('.header').offsetHeight;
            const targetPosition = targetElement.offsetTop - headerHeight - 20;
            
            // Smooth scroll
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
            const navLinks = document.querySelector('.nav-links');
            const menuBackdrop = document.querySelector('.mobile-menu-backdrop');
            if (mobileMenuBtn && navLinks && navLinks.classList.contains('is-open')) {
                navLinks.classList.remove('is-open');
                mobileMenuBtn.classList.remove('active');
                mobileMenuBtn.setAttribute('aria-expanded', 'false');
                document.body.classList.remove('nav-open');
                if (menuBackdrop) {
                    menuBackdrop.classList.remove('is-visible');
                }
            }
        });
    });
}

/* ==========================================================================
   COUNT UP ANIMATIONS FOR RESULTS
   ========================================================================== */
function initCountUpAnimations() {
    const resultValues = document.querySelectorAll('.result-value');
    if (resultValues.length === 0) return;
    
    // Create IntersectionObserver for count-up animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                const targetValue = parseInt(element.getAttribute('data-count'));
                
                // Start count-up animation
                animateCountUp(element, targetValue);
                
                // Stop observing after animation starts
                observer.unobserve(element);
            }
        });
    }, {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    });
    
    // Observe each result value
    resultValues.forEach(value => {
        observer.observe(value);
    });
}

function animateCountUp(element, targetValue) {
    const duration = 2000; // 2 seconds
    const startTime = Date.now();
    const startValue = 0;
    
    function updateCount() {
        const currentTime = Date.now();
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function for smooth animation
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const currentValue = Math.floor(startValue + (targetValue - startValue) * easeOutQuart);
        
        // Update element text
        if (element.classList.contains('result-value')) {
            // Format numbers with commas
            element.textContent = currentValue.toLocaleString() + (targetValue >= 1000000 ? '+' : '+');
        } else {
            element.textContent = currentValue;
        }
        
        // Continue animation if not complete
        if (progress < 1) {
            requestAnimationFrame(updateCount);
        }
    }
    
    // Start animation
    requestAnimationFrame(updateCount);
}

/* ==========================================================================
   HOVER EFFECTS FOR CARDS AND BUTTONS
   ========================================================================== */
function initHoverEffects() {
    // Card hover effects
    const cards = document.querySelectorAll('.service-card, .result-card, .floating-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all var(--transition-normal)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transition = 'all var(--transition-normal)';
        });
    });
    
    // Button hover effects
    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .cta-button, .nav-cta');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

/* ==========================================================================
   INTERSECTION OBSERVER FOR REVEAL ANIMATIONS
   ========================================================================== */
function initIntersectionObserver() {
    // Elements to animate on scroll
    const animateElements = document.querySelectorAll('.service-card, .result-card, .ai-content, .ai-visual, .pipeline-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                
                // Stop observing after animation
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    });
    
    // Observe each element
    animateElements.forEach(element => {
        observer.observe(element);
    });
    
    // Add CSS for animations
    const style = document.createElement('style');
    style.textContent = `
        .service-card,
        .result-card,
        .ai-content,
        .ai-visual,
        .pipeline-card {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        .service-card.animate-in,
        .result-card.animate-in,
        .ai-content.animate-in,
        .ai-visual.animate-in,
        .pipeline-card.animate-in {
            opacity: 1;
            transform: translateY(0);
        }
        
        /* Stagger animations for service cards */
        .service-card:nth-child(1) { transition-delay: 0.1s; }
        .service-card:nth-child(2) { transition-delay: 0.2s; }
        .service-card:nth-child(3) { transition-delay: 0.3s; }
        .service-card:nth-child(4) { transition-delay: 0.4s; }
        
        /* Stagger animations for result cards */
        .result-card:nth-child(1) { transition-delay: 0.1s; }
        .result-card:nth-child(2) { transition-delay: 0.2s; }
        .result-card:nth-child(3) { transition-delay: 0.3s; }
    `;
    document.head.appendChild(style);
}

/* ==========================================================================
   CTA BUTTON INTERACTIONS
   ========================================================================== */
function initCTAButtons() {
    const ctaButtons = document.querySelectorAll('.btn-primary, .btn-secondary, .cta-button');
    
    ctaButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Add click feedback
            this.style.transform = 'scale(0.95)';
            
            // Reset after animation
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
            
            // Route CTAs to the Free Audit booking page
            // (Swap to Calendly/GHL booking URL once available)
            setTimeout(() => {
                window.location.href = '/audit.html';
            }, 150);
        });
    });
}

/* ==========================================================================
   PERFORMANCE OPTIMIZATIONS
   ========================================================================== */

// Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for resize events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Optimize scroll events
window.addEventListener('scroll', debounce(function() {
    // Any scroll-based calculations go here
}, 100));

// Optimize resize events
window.addEventListener('resize', throttle(function() {
    // Any resize-based calculations go here
}, 250));

/* ==========================================================================
   ERROR HANDLING
   ========================================================================== */
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
    // In production, you might want to send this to an error tracking service
});

/* ==========================================================================
   PROGRESSIVE ENHANCEMENT
   ========================================================================== */

// Check for IntersectionObserver support
if (!('IntersectionObserver' in window)) {
    console.warn('IntersectionObserver not supported - fallback to basic animations');
    
    // Fallback: Show all elements immediately
    document.querySelectorAll('.service-card, .result-card, .ai-content, .ai-visual').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
    });
}

// Check for CSS custom properties support
if (!window.CSS || !CSS.supports('color', 'var(--test)')) {
    console.warn('CSS custom properties not supported - using fallback colors');
    
    // Add fallback styles
    const fallbackStyle = document.createElement('style');
    fallbackStyle.textContent = `
        :root {
            --color-bg-dark: #0C0F14;
            --color-primary: #FF005C;
            --color-secondary: #00C2FF;
            --color-text-primary: #FFFFFF;
            --color-text-secondary: #B8C1CC;
        }
    `;
    document.head.appendChild(fallbackStyle);
}

/* ==========================================================================
   LAZY LOADING FOR FUTURE IMAGES
   ========================================================================== */
function initLazyLoading() {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    } else {
        // Fallback: Load all images immediately
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.src = img.dataset.src;
        });
    }
}

// Initialize lazy loading when needed
if (document.querySelectorAll('img[data-src]').length > 0) {
    initLazyLoading();
}

/* ==========================================================================
   ACCESSIBILITY ENHANCEMENTS
   ========================================================================== */

// Add keyboard navigation for interactive elements
document.addEventListener('keydown', function(e) {
    // Focus trap for modals (when implemented)
    // Add skip to content functionality
    if (e.key === 'Tab') {
        // Ensure focus indicators are visible
        document.body.classList.add('keyboard-navigation');
    }
});

// Remove keyboard navigation class on mouse interaction
document.addEventListener('mousedown', function() {
    document.body.classList.remove('keyboard-navigation');
});

/* ==========================================================================
   ANALYTICS READY (COMMENTED OUT FOR NOW)
   ========================================================================== */
/*
// Example analytics event tracking
function trackEvent(category, action, label) {
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            'event_category': category,
            'event_label': label
        });
    }
    
    // Also track with custom analytics if needed
    console.log(`Analytics: ${category} - ${action} - ${label}`);
}

// Track CTA clicks
document.querySelectorAll('.btn-primary, .btn-secondary, .cta-button').forEach(button => {
    button.addEventListener('click', function() {
        const buttonText = this.textContent.trim();
        trackEvent('CTA', 'click', buttonText);
    });
});
*/

console.log('SparkMedia.ai JavaScript initialized successfully');