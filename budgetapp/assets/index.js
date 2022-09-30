/**
 * Libraries.js
 */
import Alpine from 'alpinejs';

/**
 * Style
 */
import './css/main.css';

/**
 * Global objects
 */
window.Alpine = Alpine;
window.htmx = require('htmx.org');

/**
 * Alpine setup
 */
// Alpine.data('StoreCheckout', StoreCheckout);
Alpine.start();
