/**
 * Webpack modules
 */
const { merge } = require('webpack-merge');

/**
 * Common configuration
 */
const common = require('./webpack.config.common');

module.exports = merge(common, {
  /**
   * Set the development mode
   */
  mode: 'development',
  /**
   * Build and rebuild fast.
   */
  devtool: 'eval',
});
