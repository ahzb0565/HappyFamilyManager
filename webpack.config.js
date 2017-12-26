const webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin');
module.exports = {
  entry: {
    index: './src/js/index.jsx',
    home: './src/js/home.jsx',
    create_new: './src/js/new.jsx'
  },
  output: {
    path: __dirname + '/static/dist',  //abs path
    filename: '[name].bundle.js'
  },
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ }
    ]
  },
  plugins: [
    new CopyWebpackPlugin([
        {
            from: 'node_modules/bootstrap/dist/css/bootstrap.min.css'
        }
    ])
  ]
};