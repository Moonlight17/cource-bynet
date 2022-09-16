<template>
  <div class="aggregateTable ">
    <div class="table_block table-responsive">
      <table class="table scroll table-hover" :class="[sett ? 'table-light' : 'table-dark']">
        <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col" v-for="date in dates" :key="date.id">
            {{ date.date }}
          </th>
          <th scope="col">Total</th>
        </tr>
        </thead>
        <tbody class="table-group-divider noselect">
        <tr @contextmenu.prevent.stop="handleClick($event, item)" v-for="(item, name, index) in aggre" :key="item.id" >
          <td>{{ index +1 }}</td>
          <td>{{item.name}}</td>
          <td v-for="less in item.lessons" :key="less.id" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top">
            <a data-toggle="tooltip" data-placement="top" :title="less.date">{{  less.time ? less.time : '---' }}</a>
          </td>
          <td>{{item.all_time}}</td>
        </tr>
        </tbody>
      </table>
    </div>
<!--    <div style="height: 100vh;">-->
<!--&lt;!&ndash;      <div>&ndash;&gt;-->
<!--&lt;!&ndash;        <p @contextmenu.prevent="$refs.menu.open">&ndash;&gt;-->
<!--&lt;!&ndash;          Right click on me&ndash;&gt;-->
<!--&lt;!&ndash;        </p>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;      <div class="item-wrapper noselect" style="background-color: white; color: black; font-size: 20px; width: 200px; margin: 5px;">&ndash;&gt;-->
<!--&lt;!&ndash;        <div&ndash;&gt;-->
<!--&lt;!&ndash;            v-for="(item, name, index) in aggre"&ndash;&gt;-->
<!--&lt;!&ndash;            :key="index"&ndash;&gt;-->
<!--&lt;!&ndash;            @contextmenu.prevent.stop="handleClick($event, item)"&ndash;&gt;-->
<!--&lt;!&ndash;            class="list-group-item list-group-item-action"&ndash;&gt;-->
<!--&lt;!&ndash;        >&ndash;&gt;-->
<!--&lt;!&ndash;          {{ item.name }}&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->

<!--&lt;!&ndash;      <VueSimpleContextMenu&ndash;&gt;-->
<!--&lt;!&ndash;          element-id="myUniqueId"&ndash;&gt;-->
<!--&lt;!&ndash;          :options="Object.values(aggre)"&ndash;&gt;-->
<!--&lt;!&ndash;          ref="vueSimpleContextMenu"&ndash;&gt;-->
<!--&lt;!&ndash;          @option-clicked="optionClicked"&ndash;&gt;-->
<!--&lt;!&ndash;      />&ndash;&gt;-->
<!--    </div>-->
  </div>
</template>

<script>
export default {
  name: 'aggregateTable',
  props: {
    aggre: Object,
    dates: Array,
    sett: Boolean,
  },
    data() {
      return {
      }
    },
  mounted() {
    // this.
  },
  methods: {
    handleClick (event, item) {
      // this.$refs.vueSimpleContextMenu.showMenu(event, item);
      console.log(item.id);
    },
    optionClicked (event) {
      alert(JSON.stringify(event))
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
  border-collapse: separate;
  border-spacing: 0;
}
.table_block{
  width: 80vw;
  min-width:400px;
  max-width: 2500px;
  margin: 0 auto;
  margin-top: 6%;
  margin-bottom: 6%;
  box-shadow: 0 10px 28px rgba(0,0,0,0.5), 0 10px 10px rgba(0,0,0,0.4);
  text-align: center;
  border-radius: 7px;
}
thead{
  border-bottom: 1px solid whitesmoke;
}
tr{
  white-space: nowrap;
}
thead tr th:first-child {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  z-index: 10;
}
/*td{  background-color: white !important;}*/
th:nth-child(2), td:nth-child(2)
{
  position:sticky;
  left:0px;
  border-right: 1px solid whitesmoke;
  /*background-color: aliceblue;*/
}

Here is nice looking gradient from green to red

  /* Green - Yellow - Red */
.gradient_0    {background: #57bb8a;}
.gradient_5    {background: #63b682;}
.gradient_10   {background: #73b87e;}
.gradient_15   {background: #84bb7b;}
.gradient_20   {background: #94bd77;}
.gradient_25   {background: #a4c073;}
.gradient_30   {background: #b0be6e;}
.gradient_35   {background: #c4c56d;}
.gradient_40   {background: #d4c86a;}
.gradient_45   {background: #e2c965;}
.gradient_50   {background: #f5ce62;}
.gradient_55   {background: #f3c563;}
.gradient_60   {background: #e9b861;}
.gradient_65   {background: #e6ad61;}
.gradient_70   {background: #ecac67;}
.gradient_75   {background: #e9a268;}
.gradient_80   {background: #e79a69;}
.gradient_85   {background: #e5926b;}
.gradient_90   {background: #e2886c;}
.gradient_95   {background: #e0816d;}
.gradient_100  {background: #dd776e;}
.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
}
</style>
