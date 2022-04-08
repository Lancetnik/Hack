const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],

  devServer: {
    proxy: {
      "/": {
        target: "http://localhost:8000"
      }
    },
  },
  outputDir: process.env.NODE_ENV === 'production' ? '../back/app/static' : 'dist/',
  // Все ниже - относительно outputDir
  indexPath: process.env.NODE_ENV === 'production' ? '../templates/index.html' : 'index.html',
  assetsDir: '',
  publicPath: process.env.NODE_ENV === 'production' ? 'static' : '/',
})
