<template>
<!--  <navigBlock :aggre="aggregates" />-->
  <img alt="Vue logo" src="./assets/logo.png">
  <h1>TEST</h1>
  <aggregateTable :aggre="aggregates"/>
  <startPage msg="Welcome to Your Vue.js App"/>
  <pre>{{$data}}</pre>
</template>

<script>
import startPage from '@/components/startPage.vue'
import aggregateTable from '@/components/aggregateTable.vue'
// import navigBlock from "@/components/navigbar";

export default {
  name: 'App',
  components: {
    startPage,
    aggregateTable,
    // navigBlock
  },
  data(){
    return {
      aggregates: [],
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
