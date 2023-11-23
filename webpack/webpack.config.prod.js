/**
 * Webpack modules
 */
const { merge } = require('webpack-merge');

/**
 * Plugins import
 */
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');

/**
 * Common configuration
 */
const common = require('./webpack.config.common');

module.exports = merge(common, {
  /**
   * Set the production mode
   */
  mode: 'production',
  /**
 * OUTPUT
 *
 * The output property tells webpack where to emit the bundles it creates
 * and how to name these files. All the files are outputed to ../project_name/static/js/
 */
  output: {
    filename: '[name]-[fullhash].js',
  },
  /**
   * PLUGINS
   *
   * While loaders are used to transform certain types of modules, plugins can be
   * leveraged to perform a wider range of tasks like bundle optimization,
   * asset management and injection of environment variables
   */
  plugins: [
    /**
     * This plugin is used to extract the css in its own file
     */
    new MiniCssExtractPlugin({
      filename: '[name]-[fullhash].css',
    }),
    /**
     * This plugin is used to compress the .js modules
     */
    new CompressionPlugin({ test: /\.js(\?.*)?$/i }),
  ],
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
