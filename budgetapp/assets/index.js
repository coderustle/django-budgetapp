/**
 * Images
 */
import "./images/favicon.ico";
import "./images/apple-touch-icon.png";
import "./images/android-chrome-192x192.png";

/**
 * Style
 */
import "./css/main.css";

/**
 * Third party libraries
 */
import "boxicons";
import Alpine from "alpinejs";
import persist from "@alpinejs/persist";

/**
 * Htmx setup
 */
window.htmx = require("htmx.org");

/**
 * Alpine setup
 */
Alpine.plugin(persist);
Alpine.start();

console.log("Hello World");
