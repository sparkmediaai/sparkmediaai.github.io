// Modern Features JavaScript
// Interactive functionality for the feature alternatives

document.addEventListener('DOMContentLoaded', function() {
    
    // Option 1: Feature Grid hover effects (already handled by CSS)
    
    // Option 2: Timeline interaction
    const timelineItems = document.querySelectorAll('.timeline-item');
    if (timelineItems.length > 0) {
        timelineItems.forEach(item => {
            item.addEventListener('click', function() {
                timelineItems.forEach(i => i.classList.remove('active'));
                this.classList.add('active');
            });
        });
    }
    
    // Option 3: Accordion functionality
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const item = this.parentElement;
            const isActive = item.classList.contains('active');
            
            // Close all accordion items
            document.querySelectorAll('.accordion-item').forEach(accordionItem => {
                accordionItem.classList.remove('active');
            });
            
            // Open clicked item if it wasn't active
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });
    
    // Option 5: 3D Tilt effect
    const tiltCards = document.querySelectorAll('.tilt-card');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Calculate tilt angles based on mouse position
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateY = ((x - centerX) / centerX) * 5; // Max 5 degrees
            const rotateX = ((centerY - y) / centerY) * 5; // Max 5 degrees
            
            // Update CSS custom properties for gradient position
            this.style.setProperty('--mouse-x', `${(x / rect.width) * 100}%`);
            this.style.setProperty('--mouse-y', `${(y / rect.height) * 100}%`);
            
            // Apply transform
            this.style.transform = `translateZ(20px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateZ(0) rotateX(0) rotateY(0)';
            this.style.transition = 'transform 0.5s ease';
            
            // Reset transition after animation
            setTimeout(() => {
                this.style.transition = '';
            }, 500);
        });
    });
    
    // Demo page option selector
    const optionButtons = document.querySelectorAll('.option-btn');
    optionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const option = this.getAttribute('data-option');
            
            // Update active button
            optionButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Show implementation steps for selected option
            updateImplementationSteps(option);
        });
    });
    
    // Function to update implementation steps based on selected option
    function updateImplementationSteps(option) {
        const stepsContainer = document.querySelector('.implementation-steps ol');
        if (!stepsContainer) return;
        
        const steps = {
            1: [
                'Add <code>modern-features.css</code> to your site',
                'Replace floating cards container with <code>.features-grid</code>',
                'Use <code>.feature-card</code> for each service',
                'Customize colors in CSS variables',
                'Test hover animations on desktop and mobile'
            ],
            2: [
                'Include both CSS and JS files',
                'Replace with <code>.features-timeline</code> container',
                'Add <code>.timeline-item</code> for each feature',
                'Implement horizontal scroll with CSS',
                'Add click interaction with JavaScript'
            ],
            3: [
                'Add accordion HTML structure',
                'Include JavaScript for expand/collapse',
                'Style active states with CSS',
                'Add smooth transition animations',
                'Make mobile-responsive'
            ],
            4: [
                'Use <code>.stats-grid</code> container',
                'Add <code>.stat-card</code> for each feature',
                'Implement hover gradient border',
                'Keep design minimal and clean',
                'Ensure good spacing on mobile'
            ],
            5: [
                'Add 3D perspective container',
                'Implement mouse tracking JavaScript',
                'Create depth with transform properties',
                'Add dynamic gradient lighting',
                'Test performance on different devices'
            ]
        };
        
        if (steps[option]) {
            stepsContainer.innerHTML = steps[option].map(step => 
                `<li>${step}</li>`
            ).join('');
        }
    }
    
    // Initialize with Option 1
    updateImplementationSteps('1');
    
    // Add smooth scrolling for demo page links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add copy-to-clipboard for code snippets
    document.querySelectorAll('.code-preview pre').forEach(pre => {
        pre.addEventListener('click', function() {
            const text = this.textContent;
            navigator.clipboard.writeText(text).then(() => {
                // Show copied notification
                const notification = document.createElement('div');
                notification.textContent = 'Code copied to clipboard!';
                notification.style.cssText = `
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    background: #00C2FF;
                    color: white;
                    padding: 12px 20px;
                    border-radius: 8px;
                    font-weight: 600;
                    z-index: 1000;
                    animation: fadeInOut 2s ease;
                `;
                
                document