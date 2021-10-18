<template>
  <div id="app">
    <h2>MayaTracker</h2>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>
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
}
</style>
