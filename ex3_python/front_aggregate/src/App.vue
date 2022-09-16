<template>
  <div :class="[sett ? 'light-fon' : 'dark-fon']">
    <navigBlock :users="participants" :sett="sett" />
    <aggregateTable :aggre="aggregates" :dates="dates" :sett="sett"/>
    <div class="collapse py-2" id="collapseTarget">
      <aggregateTable :aggre="aggregates" :dates="dates" />
    </div>
  </div>
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
      sett: false,
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
    getList(day_start, day_finish, need) {
      if (need == undefined) need = false;
      // console.log('need', need);
      let url = 'http://' + this.home_url + ':8000/aggregate/'+day_start+'/'+day_finish+'/';
      if(!need) {
      this.axios.get(url).then((response) => {
        this.dates = response.data['dates']
        delete response.data['dates'];
        this.aggregates = response.data
      })} else {
        let ids = [];
        for (let key in need){
          ids.push(need[key]['id'])
          // console.log(key)
        }
        const users = { 'need': ids };
        this.axios.post(url, users).then((response) => {
          this.dates = response.data['dates']
          delete response.data['dates'];
          this.aggregates = response.data
        })
        // console.log("test", ids);
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
@import url('https://fonts.googleapis.com/css2?family=Rubik+Dirt&display=swap');
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /*background-image: "./";*/
  /*margin-top: 60px;*/
}
.dark-fon{
  min-height: 100vh;
  color: #2c3e50;
  background-image: url('assets/Fon3.jpeg');
  background-attachment: fixed;
  background-position: top center;
  background-size: cover;
  padding-bottom: 1px;
}
.light-fon{
  min-height: 100vh;
  color: #2c3e50;
  background-image: url('./assets/Fon2.jpeg');
  background-attachment: fixed;
  background-position: top center;
  background-size: cover;
  padding-bottom: 1px;
}
</style>
