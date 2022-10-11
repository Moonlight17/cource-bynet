<template>
  <div :class="[sett ? 'light-fon' : 'dark-fon']">
    <navigBlock :users="participants" :sett="sett" />
    <aggregateTable :aggre="aggregates" :dates="dates" :sett="sett" :duration="duration"/>
    <div class="collapse py-2" id="collapseTarget">
      <aggregateTable :aggre="aggregates" :dates="dates" />
    </div>
  </div>
</template>

<script>
// import startPage from '@/components/startPage.vue'
import aggregateTable from '@/components/aggregateTable.vue'
import navigBlock from "@/components/navigbar.vue";

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
      duration: 0,
      // prefix: 'http://localhost:8000',
      prefix: '/api/1',
      participants: [],
      sett: true,
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
    changing(aggreg){
      let res = [];
      for (var user in aggreg){
        aggreg[user]['all_time'] = 0;
        for (var lesson in aggreg[user]['lessons']){
          aggreg[user]['all_time'] = aggreg[user]['all_time'] + aggreg[user]['lessons'][lesson]['time'];
        }
        aggreg[user]['duration'] = (aggreg[user]['all_time']/this.duration)*100;
        if (aggreg[user]['duration'] > 99){
          aggreg[user]['duration'] = '~ 100'
        }else{
          aggreg[user]['duration'] = aggreg[user]['duration'].toFixed(0)
        }
        res.push(aggreg[user]);
      }
      res.sort((x, y) => x.name.localeCompare(y.name));
      return res
    },
    getList(day_start, day_finish, need) {
      if (need == undefined) need = false;
      let url = this.prefix+'/aggregate/'+day_start+'/'+day_finish+'/';
      if(!need) {
      this.axios.get(url).then((response) => {
        let last = (response.data['dates']).length - 1;
        this.duration = response.data['dates'][last];
        response.data['dates'].splice(last, 1);
        this.dates = response.data['dates']
        delete response.data['dates'];
        this.aggregates = this.changing(response.data);
      })} else {
        let ids = [];
        for (let key in need){
          ids.push(need[key]['id'])
          // console.log(key)
        }
        const users = { 'need': ids };
        this.axios.post(url, users).then((response) => {
          let last = (response.data['dates']).length - 1;
          this.duration = response.data['dates'][last];
          response.data['dates'].splice(last, 1);
          this.dates = response.data['dates']
          delete response.data['dates'];
          this.aggregates = this.changing(response.data);
        })
        // console.log("test", ids);
      }
    },
    getParticipant() {
      let url = this.prefix+'/participants/';

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
