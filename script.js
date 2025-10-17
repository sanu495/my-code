// Smooth scroll polyfill is enabled by CSS scroll-behavior, but let's enhance contact form submission feedback
document.getElementById('contactForm').addEventListener('submit', e => {
  e.preventDefault();
  alert('Thank you for reaching out! We will get back to you shortly.');
  e.target.reset();
});