const webpack = require('webpack');
module.exports = {
  entry: './static/js/test.jsx',
  output: {
    path: __dirname + '/static/dist',  //abs path
    filename: 'test.js'
  },
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ }
    ]
  }
};