<template>
  <div class="hello">
    <div id="counter">
      Счётчик: {{ counter }}
    </div>
    <button @click="getList()">OLOLO</button>
  </div>
</template>

<script>
export default {
  name: 'startPage',
  props: {
    msg: String
  },
    data() {
      return {
        counter: 0,

      }
    },
  mounted() {
    // setInterval(() => {
    //   this.counter++
    // }, 1000)
    this.getList();
  },
  methods: {
    today() {
      let currentDate = new Date();
      let day = ("0" + currentDate.getDate()).slice(-2);
      let month = ("0" + (currentDate.getMonth() + 1)).slice(-2);
      let year = currentDate.getFullYear();
      currentDate = day+'-'+month+'-'+year;
      return currentDate

    },
    getList() {
      let today = this.today();
      // console.log(today);
      this.axios.get('http://localhost:8000/aggregate/26-07-2022/'+today+'/').then((response) => {
        this.$parent.$data.dates = response.data['dates']
        delete response.data['dates'];
        this.$parent.$data.aggregates = response.data
        // console.log(response.data)
      })
    }
  }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
