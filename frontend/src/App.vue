<template>
  <fullHeader />
  <router-view></router-view>
  <fullFooter />
</template>

<script>
import fullHeader from './components/fullHeader.vue'
import fullFooter from './components/fullFooter.vue'

export default {
  components: {
    fullHeader,
    fullFooter
  }
}
</script>

<style>
body {
  margin: 0 auto;
}

#app {
  font-family: 'Oswald', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 10px;
}
</style>
