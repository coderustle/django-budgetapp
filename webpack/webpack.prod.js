/**
 * Webpack modules
 */
const webpack = require('webpack');
const { merge } = require('webpack-merge');

/**
 * Plugins import
 */
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

/**
 * Common configuration
 */
const common = require('./webpack.common');

module.exports = merge(common, {
  /**
   * Set the production mode
   */
  mode: 'production',
  /**
   * OPTIMIZATION
   */
  optimization: {
    minimize: true,
    minimizer: [
      // For webpack@5 you can use the `...` syntax to extend existing minimizers (i.e. `terser-webpack-plugin`), uncomment the next line
      `...`,
      new CssMinimizerPlugin(),
    ],
  },
});
