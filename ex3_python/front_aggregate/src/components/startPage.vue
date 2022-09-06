<template>
  <div class="hello">
    <button
        class="btn btn-primary"
        data-bs-target="#collapseTarget"
        data-bs-toggle="collapse">
      Bootstrap collapse
    </button>
    <div class="collapse py-2" id="collapseTarget">
      This is the toggle-able content!
    </div>
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
  },
  methods: {
    getList() {
      this.axios.get('http://localhost:8000/aggregate/2022-08-08/2022-08-09/').then((response) => {
        this.$parent.$data.aggregates = response.data
        console.log(response.data)
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
