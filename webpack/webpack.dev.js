/**
 * Webpack modules
 */
const { merge } = require('webpack-merge');
const webpack = require('webpack');

/**
 * Common configuration
 */
const common = require('./webpack.common');

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
