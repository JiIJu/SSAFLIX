const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// module.exports = {
//   devServer: {
//     devServer : {
//       port:8080,
//       proxy: {
//         'api/*' : {
//           'target' : 'http://localhost:8000/',
//           'pathRewrite' : {'^/':''},
//           'changeOrigin' : true,
//           'secure' : false
//         }
//       }
//     }
//     }
// }