<template>
  <navigBlock :users="participants" />
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
      home_url: 'localhost',
      participants: [],
    }
  },
  mounted() {
    // setInterval(() => {
    //   this.counter++
    // }, 1000)
    // this.getList();
    // console.log(this.BASE_URL);
  },
  methods: {
    getList(day_start, day_finish, need=false) {
      let url = 'http://' + this.home_url + ':8000/aggregate/'+day_start+'/'+day_finish+'/';
      if(!need) {
      this.axios.get(url).then((response) => {
        this.dates = response.data['dates']
        delete response.data['dates'];
        this.aggregates = response.data
      })} else {
        let ids = [];
        for (let item in need){
          ids.push(item.id)
        }
        const article = { 'need': ids };
        this.axios.post(url, article).then((response) => {
          this.participants = response.data
        })
        console.log("test", need);
      }
    },
    getParticipant() {
      let url = 'http://' + this.home_url + ':8000/participants/';

        this.axios.get(url).then((response) => {
          this.participants = response.data

        })
    },
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
  /*background-image: "./";*/
  /*margin-top: 60px;*/
  background-image: url('./assets/Fon2.jpeg');
  background-attachment: fixed;
  background-position: top center;
  background-size: cover;
}
</style>
