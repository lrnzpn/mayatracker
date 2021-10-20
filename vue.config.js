module.exports = {
    lintOnSave: false,
    css: {
      loaderOptions: {
        sass: {
          data: `@import "@/styles/_variables.scss";`
        }
      }
    },
    publicPath: "./"
  };