<template>
  <div id="navigbar">
    <nav class="navbar navbar-expand-md bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
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
            <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Change dates</button>
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
              <h5 class="modal-title" id="exampleModalLabel">Change dates</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">

              <Datepicker
                  v-model="value"
                  :startDate="minDate"
                  range
                  multiCalendars
                  multiCalendarsSolo
                  inline
                  autoApply
                  :disabledWeekDays="[0, 5, 6]"
                  :minDate="minDate"
                  modelType="dd-MM-yyyy"
                  :enableTimePicker="false"
              />

            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary" @click="test();">Save changes</button>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script>
// import { ref } from 'vue';

export default {
  // setup() {
  //   const date = ref(new Date());
  //   // In case of a range picker, you'll receive [Date, Date]
  //   const format = (date) => {
  //     const day = date.getDate();
  //     const month = date.getMonth() + 1;
  //     const year = date.getFullYear();
  //
  //         return `Selected date is ${day}-${month}-${year}`;
  //     }
  //       return {
  //         date,
  //         format,
  //   }
  // },
  name: "navigBlock",
  components: {
    // Calendar
    // navigBlock
  },
  // props: {
  //   list: Array,
  // },
  data(){
    return{
      list_countries:null,
      selected: [],
      minDate: new Date(2022, 6, 26),
      value: [],
      filter: '',

    }
  },
  created() {
    this.value[0] = this.minDate;
    this.value[1] = new Date();
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

  },
  methods:{
    test(){
      this.$parent.getList(this.value[0], this.value[1]);
    }
  }
}
</script>

<style scoped>
.nav{
  padding: 10px 3%;
}
.drop-downbox{
  color: red;
}
</style>
