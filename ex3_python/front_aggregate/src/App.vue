<template>
  <navigBlock />
<!--  <img alt="Vue logo" src="./assets/logo.png">-->
<!--  <h1>TEST</h1>-->
  <aggregateTable :aggre="aggregates" :dates="dates" />
<!--  <button-->
<!--      class="btn btn-primary"-->
<!--      data-bs-target="#collapseTarget"-->
<!--      data-bs-toggle="collapse">-->
<!--    Bootstrap collapse-->
<!--  </button>-->
  <div class="collapse py-2" id="collapseTarget">
    <aggregateTable :aggre="aggregates" :dates="dates" />
  </div>
<!--  <startPage msg="Welcome to Your Vue.js App"/>-->
<!--  <pre>{{$data}}</pre>-->
</template>

<script>
// import startPage from '@/components/startPage.vue'
import aggregateTable from '@/components/aggregateTable.vue'
import navigBlock from "@/components/navigbar";

export default {
  name: 'App',
  components: {
    // startPage,
    aggregateTable,
    navigBlock
  },
  data(){
    return {
      aggregates: [],
      dates: [],
    }
  },
  mounted() {
    // setInterval(() => {
    //   this.counter++
    // }, 1000)
    // this.getList();
  },
  methods: {
    getList(day_start, day_finish) {
      this.axios.get('http://localhost:8000/aggregate/'+day_start+'/'+day_finish+'/').then((response) => {
        this.dates = response.data['dates']
        delete response.data['dates'];
        this.aggregates = response.data
        // console.log(response.data)
      })
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
  /*margin-top: 60px;*/
}
</style>
