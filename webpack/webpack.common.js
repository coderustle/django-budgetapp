/**
 * Node.js modules
 */
const path = require('path');

/**
 * Plugins import
 */
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CompressionPlugin = require('compression-webpack-plugin');

module.exports = {
  /**
   * ENTRY
   *
   * index.js: is the main entrypoint.
   * babel.bundle.js: is the bable entrypoint
   * vue.bundle.js: is the vue.js entrypoint
   */
  entry: {
    /**
     * Alpine.js entrypoint
     */
    alpine: 'alpinejs',
    /**
     * HTMX load
     */
    htmx: 'htmx.org',
    /**
     * index.js entrypoint
     */
    index: {
      import: path.resolve(__dirname, '../budgetapp/assets/index.js'),
      dependOn: [ 'htmx', 'alpine'], // ['htmx', 'vue']
    },
  },
  /**
   * OUTPUT
   *
   * The output property tells webpack where to emit the bundles it creates
   * and how to name these files. All the files are outputed to ../mihaelamocanu/static/js/
   */
  output: {
    /**
     * Thi is the path where the bundle files will be placed
     */
    path: path.resolve(__dirname, '../budgetapp/static/javascript/'),
    /**
     * This is the public path where the server will look for static files
     * Something like https://localhost:8000/static/js/index.bundle.js
     */
    publicPath: '/static/',
    /**
     * This is the file name that will result from the entries
     */
    filename: '[name].bundle.js',
    /**
     * This settings is for assets, to specify where to be placed.
     */
    assetModuleFilename: '../../[hash][ext]',
    /**
     * Everytime webpack runs will clear the '../budgetapp/static/javascript/ folder
     */
    clean: true,
  },
  /**
   * LOADERS
   *
   * Loaders allow webpack to process other types of files and convert them into
   * valid modules that can be consumed by your application and added to the
   * dependency graph
   */
  module: {
    /**
     * Rules defined for different files
     * The test property identifies which file or files should be transformed.
     * The use property indicates which loader should be used to do the transforming.
     */
    rules: [
      /**
       * Rule 1: use bable to transform all the js.files.
       * Exclude the node_modules folder.
       */
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
            plugins: ['@babel/plugin-transform-regenerator'],
          },
        },
      },
      /**
       * Rule 2: understand and parse the css files
       * A directory path will be created as for the source file.
       */
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'],
      },
    ],
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
    new MiniCssExtractPlugin({ filename: '../css/main.css' }),
    /**
     * This plugin is used to compress the .js modules
     */
    new CompressionPlugin({ test: /\.js(\?.*)?$/i }),
  ],
  /**
   * OPTIMIZATION
   */
  optimization: {
    minimize: false,
    runtimeChunk: 'single',
  },
};
