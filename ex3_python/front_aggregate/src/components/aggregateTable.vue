<template>
  <div class="aggregateTable ">
<!--    <h2>aggregateTable</h2>-->
    <div class="table_block table-responsive">
      <table class="table scroll">
        <thead class="table-light">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col" v-for="date in dates" :key="date.id">
            {{ date.date }}
          </th>
        </tr>
        </thead>
        <tbody class="table-group-divider">
        <tr v-for="(item, name, index) in aggre" :key="item.id" >
          <td>{{ index +1 }}</td>
          <td>{{item.Name}}</td>
          <td v-for="less in item.lessons" :key="less.id">
            {{  less.time ? less.time : '---' }}
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'aggregateTable',
  props: {
    aggre: Object,
    dates: Array,
  },
    data() {
      return {
      }
    },
  mounted() {
    // this.
  },
  methods: {
    getList() {
      this.axios.get('http://localhost:8000/aggregate/2022-07-01/2022-08-10/').then((response) => {
        console.log(response.data)
      })
    },
    formatCurrency(value) {
      console.log("value");
      console.log(value);
      return value+'!!!date'
    }
  }

    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.aggregateTable table{

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
table.scroll{
  overflow-x: auto;
  position: relative;
}
.table_block{
  width: 80vw;
  min-width:400px;
  max-width: 2500px;
  margin: 0 auto;
  margin-top: 6%;
  box-shadow: 0 10px 28px rgba(0,0,0,0.5), 0 10px 10px rgba(0,0,0,0.4);
  text-align: center;
  border-radius: 7px;
}
thead tr:first-child th {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  z-index: 10;
}
td{  background-color: white !important;}
th:nth-child(2), td:nth-child(2)
{
  position:sticky;
  left:0px;
  /*background-color: aliceblue;*/
}
</style>
