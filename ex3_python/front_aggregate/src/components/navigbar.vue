<template>
  <div id="navigbar">
    <nav class="navbar navbar-expand-md bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" id="logotype" href="#"><img alt="Logo" src="../assets/Logotype.png"></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
          <ul class="navbar-nav me-auto mb-2 mb-sm-0">
            <li class="nav-item">

            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Filters</button>
          </form>
        </div>
      </div>

    </nav>
    <div>
    </div>
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Filters</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <MultiSelect
                  v-model="example.value"
                  v-bind="example"
                  :options="users"
                  class="multiselect-blue"
              >
              </Multiselect>
              <br>
              <br>
              <br>
              <br>
              <Datepicker
                  v-model="value"
                  :startDate="minDate"
                  range
                  multiCalendars
                  multiCalendarsSolo
                  inline
                  textInput
                  autoApply
                  :minDate="minDate"
                  modelType="dd-MM-yyyy"
                  :enableTimePicker="false"
              />

            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="test(example.value);">Save changes</button>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script>
// import { ref } from 'vue';

export default {
  name: "navigBlock",
  components: {
  },
  props: {
    users: Array,
  },
  data(){
    return{
      list_countries:null,
      selected: [],
      minDate: new Date(2022, 6, 26),
      value: [],
      filter: '',
      find: [],
      example: {
        mode: 'tags',
        placeholder: 'Select employees',
        closeOnSelect: false,
        searchable: true,
        trackBy: 'value',
        label: 'value',
        object: true,
        groups: true,
        value: [],
      },
    }
  },
  created() {
    let startDate = new Date(2022, 6, 26);
    let currentDate = new Date();
    let start_day = ("0" + startDate.getDate()).slice(-2);
    let start_month = ("0" + (startDate.getMonth() + 1)).slice(-2);
    let start_year = startDate.getFullYear();
    let finish_day = ("0" + currentDate.getDate()).slice(-2);
    let finish_month = ("0" + (currentDate.getMonth() + 1)).slice(-2);
    let finish_year = currentDate.getFullYear();

    let start = start_day+'-'+start_month+'-'+start_year;
    let finish = finish_day+'-'+finish_month+'-'+finish_year;
    this.$parent.getList(start, finish);
    this.value[0] = start;
    this.value[1] = finish;
    this.$parent.getParticipant();

  },
  mounted() {
    // this.users = this.$parent.participants;
  },
  methods:{
    test(){
      if (this.example.value.length == 0){
        this.$parent.getList(this.value[0], this.value[1]);
      } else {
        // console.log(this.example.value)
        this.$parent.getList(this.value[0], this.value[1], this.example.value);
      }
    }
  }
}
</script>

<style scoped>
#logotype{
  width: 10%;
}
#logotype img{
  width: 100%;
}
.nav{
  padding: 10px 3%;
}
.drop-downbox{
  /*color: red;*/
}
.modal-body{
  margin: 0 auto;
}
.dp__theme_light{
  /*background: #0d6efd !important;*/
  /*--dp-primary-color: red;*/
}
.multiselect-blue{
  --ms-border-color: #D1D5DB;
  --ms-tag-bg: #DBEAFE;
  --ms-tag-color: #2563EB;
  /*--ms-group-label-bg-selected: red;*/
  --ms-group-label-bg: #E5E7EB;
  --ms-group-label-color: #374151;
  --ms-group-label-bg-pointed: #D1D5DB;
  --ms-group-label-color-pointed: #374151;
  --ms-group-label-bg-disabled: #F3F4F6;
  --ms-group-label-color-disabled: #D1D5DB;
  --ms-group-label-bg-selected: #0d6efd;
  --ms-group-label-color-selected: #FFFFFF;
  --ms-group-label-bg-selected-pointed: #0d6efd;
  --ms-group-label-color-selected-pointed: #FFFFFF;
  --ms-group-label-bg-selected-disabled: #6aa5ff;
  --ms-group-label-color-selected-disabled: #6aa5fc;
}
</style>
