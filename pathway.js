//original code from: https://github.com/webpack/webpack/issues/1189

// entry: {
//   'build/application/bundle': './src/application', // will be  ./build/application/bundle.js,
//   'build/library/bundle': './src/library`'// will be  ./build/library/bundle.js
// },
// output: {
//   path: './',
//   filename: '[name].js'
// }


// MY CODE modified for creating Mealyzer photo output paths
entry: {
  'build/application/bundle': './Github/mealyzer', // will be  ./build/application/bundle.js,
  'build/library/bundle': './src/library`'// will be  ./build/library/bundle.js
},
output: {
  path: './',
  filename: '[name].js'
}