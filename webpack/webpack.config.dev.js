/**
 * Webpack modules
 */
const { merge } = require('webpack-merge');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
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
  /**
   * OUTPUT
   *
   * The output property tells webpack where to emit the bundles it creates
   * and how to name these files. All the files are outputed to ../project_name/static/js/
   */
  output: {
    filename: '[name].js'
  },
  /**
   * PLUGINS
   *
   * While loaders are used to transform certain types of modules, plugins can be
   * leveraged to perform a wider range of tasks like bundle optimization,
   * asset management and injection of environment variables
   */
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
    }),
  ]

});
