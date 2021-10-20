<template>
  <div id="app">
    
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style lang="scss">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

main {
  margin: 30px auto;
  width: 500px;
}

h2 {
  text-align: center;
  margin: 20px auto;
  color: $navy;
}

.close {
    float: right;
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 1;
    color: #000;
    text-shadow: 0 1px 0 #fff;
    opacity: .5;
    background-color: transparent;
    border: 0;
    &:hover {
      opacity: 1;
    }
}
</style>
