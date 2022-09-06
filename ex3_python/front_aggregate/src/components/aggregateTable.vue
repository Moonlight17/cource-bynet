<template>
  <div class="aggregateTable">
    <h2>aggregateTable</h2>
    <table class="row justify-content-lg-center table table-hover">
      <thead></thead>
      <tbody>
      <tr v-for="item in aggre" :key="item.id" >
        <td>{{item.user.Name}}</td>
        <td>{{item.time_on_less}}</td>
        <td>{{item.date}}</td>
<!--        # TODO Сделать в качетсве имени столбца Date-->
<!--        {{item}}-->
      </tr>
      </tbody>
    </table>
<!--    <b-table-->
<!--        :items="aggre"-->
<!--        show-empty-->
<!--        hover-->
<!--    >-->
<!--    </b-table>-->
  </div>
</template>

<script>
export default {
  name: 'aggregateTable',
  props: {
    aggre: Array,
  },
    data() {
      return {
      }
    },
  mounted() {
  },
  methods: {
    getList() {
      this.axios.get('http://localhost:8000/aggregate/2022-08-01/2022-08-10/').then((response) => {
        console.log(response.data)
      })
    }
  }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.aggregateTable table{
  /*width: 80%;*/
  /*align-content: center;*/
  margin: 0 auto;
}
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
