<template>
  <div id="navigbar">
    <nav class="navbar navbar-expand-md" :class="[sett ? 'navbar-light bg-light' : 'navbar-dark bg-dark']">
<!--    <nav class="navbar navbar-expand-md">-->
      <div class="container-fluid">
        <a class="navbar-brand" id="logotype" href="#">
          Serov
<!--          <img alt="Logo" src="../assets/Logotype.png">-->
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
          <ul class="navbar-nav me-auto mb-2 mb-sm-0">
            <li class="nav-item">

            </li>
<!--            <li class="nav-item">-->
<!--              <a class="nav-link disabled">Disabled</a>-->
<!--            </li>-->
          </ul>
          <form class="d-flex" role="search">
            <button type="button" class="btn" :class="[sett ? 'btn-outline-dark' : 'btn-outline-light']" data-bs-toggle="modal" data-bs-target="#exampleModal">Settings</button>
<!--            <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal">Settings</button>-->
          </form>
        </div>
      </div>

    </nav>
    <div>
    </div>
      <div class="modal fade" :class="[sett ? 'color-dark' : 'color-light']"  id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl">
          <div class="modal-content" :class="[sett ? 'bg-light' : 'bg-dark']">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Filters</h5>
              <button type="button" :class="[sett ? '' : 'btn-close-white']" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <MultiSelect
                  v-model="example.value"
                  v-bind="example"
                  :options="users"
                  class=""
                  :class="[sett ? 'multiselect-light' : 'multiselect-dark']"
              >
              </MultiSelect>
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
                  :dark="!sett"
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
    sett: Boolean,
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

<style>
.color-light{
  color:  var(--bs-light);
}
.color-dark{
  color:  var(--bs-dark);
}
/*.multiselect-dark {*/
/*  --ms-bg: #454545;*/
/*  --ms-tag-bg: #D1FAE5;*/
/*  --ms-tag-color: #059669;*/
/*  --ms-border-color: #00ff00;*/
/*  --ms-placeholder-color: pink;*/
/*  !*background-color: red;*!*/
/*}*/
/*div.multiselect-tags > div > input.multiselect-tags-search{*/
/*  background-color: var(--ms-bg);*/
/*}*/
/*.multiselect input{*/
/*  background-color: gold;*/
/*}*/
.multiselect{
  --ms-placeholder-color: white;
  --ms-tag-bg: #0d6efd;
  --ms-bg: #353535 !important;
  --ms-border-color: #727272;
  --ms-dropdown-bg: #353535;
  --ms-option-color-pointed: white !important;
  --ms-option-color-selected-pointed: #FFFFFF;

  --ms-option-bg-pointed: #FFFFFF;
  --ms-option-color-pointed: black !important;
  --ms-option-color-selected: #FFFFFF;
  --ms-group-label-bg-selected-pointed: #0d6efd;
}

input.multiselect-tags-search{
  background-color: var(--ms-bg) !important;
}
.dp__theme_dark {
  --dp-background-color: #353535 !important;
  --dp-primary-color: #0d6efd !important;
  --dp-border-color: gold;
}
#logotype{
  width: 10%;
  font-family: 'Rubik Dirt', cursive;
  font-size: 2.3rem;
  color: gold;
  padding: 0;
  margin: 0;
}
#logotype img{
  width: 100%;
}
.nav{
  padding: 10px 3%;
}
.modal-body{
  margin: 0 auto;
}
/*.multiselect-blue{*/
/*  --ms-border-color: #D1D5DB;*/
/*  --ms-tag-bg: #DBEAFE;*/
/*  --ms-tag-color: #2563EB;*/
/*  --ms-group-label-bg: #E5E7EB;*/
/*  --ms-group-label-color: #374151;*/
/*  --ms-group-label-bg-pointed: #D1D5DB;*/
/*  --ms-group-label-color-pointed: #374151;*/
/*  --ms-group-label-bg-disabled: #F3F4F6;*/
/*  --ms-group-label-color-disabled: #D1D5DB;*/
/*  --ms-group-label-bg-selected: #0d6efd;*/
/*  --ms-group-label-color-selected: #FFFFFF;*/
/*  --ms-group-label-bg-selected-pointed: #0d6efd;*/
/*  --ms-group-label-color-selected-pointed: #FFFFFF;*/
/*  --ms-group-label-bg-selected-disabled: #6aa5ff;*/
/*  --ms-group-label-color-selected-disabled: #6aa5fc;*/
/*}*/
</style>
