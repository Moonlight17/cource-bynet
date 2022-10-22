<template>
  <div id="navigbar">
    <nav class="navbar navbar-expand-md shad" :class="[sett ? 'navbar-light bg-light' : 'navbar-dark bg-dark']">
<!--    <nav class="navbar navbar-expand-md">-->
      <div class="container-fluid">
        <a class="navbar-brand" :class="[sett ? 'logo_light' : 'logo_dark']" id="logotype" href="#">
          Serov -
          <span class="type">{{type_build}}</span>
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
          <form class="d-flex nav-form" role="search">
            <transition name="no-mode-fade">
              <svg @click="changeTheme(!sett)" :class="[sett ? 'dark-light' : 'dark-theme']" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="mdi-theme-light-dark" viewBox="0 0 24 24"><path d="M7.5,2C5.71,3.15 4.5,5.18 4.5,7.5C4.5,9.82 5.71,11.85 7.53,13C4.46,13 2,10.54 2,7.5A5.5,5.5 0 0,1 7.5,2M19.07,3.5L20.5,4.93L4.93,20.5L3.5,19.07L19.07,3.5M12.89,5.93L11.41,5L9.97,6L10.39,4.3L9,3.24L10.75,3.12L11.33,1.47L12,3.1L13.73,3.13L12.38,4.26L12.89,5.93M9.59,9.54L8.43,8.81L7.31,9.59L7.65,8.27L6.56,7.44L7.92,7.35L8.37,6.06L8.88,7.33L10.24,7.36L9.19,8.23L9.59,9.54M19,13.5A5.5,5.5 0 0,1 13.5,19C12.28,19 11.15,18.6 10.24,17.93L17.93,10.24C18.6,11.15 19,12.28 19,13.5M14.6,20.08L17.37,18.93L17.13,22.28L14.6,20.08M18.93,17.38L20.08,14.61L22.28,17.15L18.93,17.38M20.08,12.42L18.94,9.64L22.28,9.88L20.08,12.42M9.63,18.93L12.4,20.08L9.87,22.27L9.63,18.93Z" /></svg>
            </transition>
            <button type="button" class="btn" :class="[sett ? 'btn-outline-dark' : 'btn-outline-light']" data-bs-toggle="modal" data-bs-target="#exampleModal">Settings</button>
<!--            <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal">Settings</button>-->
          </form>
        </div>
      </div>

    </nav>
    <div>
    </div>
      <div class="modal fade" :class="[sett ? 'color-dark' : 'color-light']"  id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="z-index:1100;">
        <div class="modal-dialog modal-xl">
          <div class="modal-content" :class="[sett ? 'bg-light' : 'bg-dark']">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Filters</h5>
              <div  @click="add_data(true)" :class="[initting ? 'rot' : '']" class="init">
                <svg v-if="sett" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" x="0px" y="0px" viewBox="0 0 512 512" xml:space="preserve"> <g><path style="fill:#0d6efd;" d="M14.519,304.842C6.502,304.842,0,298.34,0,290.323v-95.425C0,130.248,52.598,77.65,117.248,77.65h309.611c8.017,0,14.519,6.502,14.519,14.519s-6.502,14.519-14.519,14.519H117.248c-48.639,0-88.21,39.572-88.21,88.21v95.425C29.038,298.342,22.536,304.842,14.519,304.842z"/><path style="fill:#0d6efd;" d="M77.932,261.282c-8.017,0-14.519-6.502-14.519-14.519V194.9c0-29.182,24.653-53.835,53.835-53.835h164.556c8.017,0,14.519,6.502,14.519,14.519s-6.502,14.519-14.519,14.519H117.248c-13.211,0-24.797,11.586-24.797,24.797v51.863C92.451,254.78,85.95,261.282,77.932,261.282z"/> </g><polygon style="fill:#FFFFFF;" points="361.627,29.659 497.481,124.86 361.627,220.063 "/> <g><path style="fill:#0d6efd;" d="M361.625,234.582c-2.293,0-4.591-0.542-6.701-1.639c-4.804-2.5-7.817-7.466-7.817-12.88V29.657c0-5.414,3.013-10.38,7.817-12.88c4.803-2.502,10.6-2.12,15.034,0.99l135.853,95.203c3.878,2.718,6.187,7.155,6.187,11.89s-2.31,9.172-6.187,11.89l-135.853,95.201C367.472,233.696,364.555,234.582,361.625,234.582z M376.146,57.561v134.597l96.036-67.299L376.146,57.561z"/><path style="fill:#0d6efd;" d="M394.752,434.352H85.141c-8.017,0-14.519-6.502-14.519-14.519c0-8.017,6.502-14.519,14.519-14.519h309.611c48.639,0,88.21-39.572,88.21-88.21v-95.425c0-8.017,6.502-14.519,14.519-14.519S512,213.661,512,221.679v95.425C512,381.754,459.402,434.352,394.752,434.352z"/><path style="fill:#0d6efd;" d="M394.752,370.938H230.196c-8.017,0-14.519-6.502-14.519-14.519c0-8.017,6.502-14.519,14.519-14.519h164.556c13.211,0,24.797-11.586,24.797-24.797V265.24c0-8.017,6.502-14.519,14.519-14.519c8.017,0,14.519,6.502,14.519,14.519v51.863C448.587,346.284,423.932,370.938,394.752,370.938z"/> </g> <polygon style="fill:#FFFFFF;" points="150.372,482.344 14.519,387.142 150.372,291.94 "/><path style="fill:#0d6efd;" d="M150.373,496.863c-2.93,0-5.845-0.884-8.334-2.629L6.187,399.031C2.309,396.313,0,391.878,0,387.142 c0-4.736,2.31-9.172,6.187-11.89l135.853-95.201c4.436-3.109,10.229-3.49,15.034-0.99c4.804,2.5,7.817,7.466,7.817,12.88v190.405 c0,5.414-3.013,10.38-7.817,12.88C154.966,496.322,152.665,496.863,150.373,496.863z M39.818,387.142l96.036,67.3V319.844 L39.818,387.142z"/><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g></svg>
                <svg v-else      id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" x="0px" y="0px" viewBox="0 0 512 512" xml:space="preserve"> <g><path style="fill:#FFFFFF;" d="M14.519,304.842C6.502,304.842,0,298.34,0,290.323v-95.425C0,130.248,52.598,77.65,117.248,77.65h309.611c8.017,0,14.519,6.502,14.519,14.519s-6.502,14.519-14.519,14.519H117.248c-48.639,0-88.21,39.572-88.21,88.21v95.425C29.038,298.342,22.536,304.842,14.519,304.842z"/><path style="fill:#FFFFFF;" d="M77.932,261.282c-8.017,0-14.519-6.502-14.519-14.519V194.9c0-29.182,24.653-53.835,53.835-53.835h164.556c8.017,0,14.519,6.502,14.519,14.519s-6.502,14.519-14.519,14.519H117.248c-13.211,0-24.797,11.586-24.797,24.797v51.863C92.451,254.78,85.95,261.282,77.932,261.282z"/> </g><polygon style="fill:#000000;" points="361.627,29.659 497.481,124.86 361.627,220.063 "/> <g><path style="fill:#FFFFFF;" d="M361.625,234.582c-2.293,0-4.591-0.542-6.701-1.639c-4.804-2.5-7.817-7.466-7.817-12.88V29.657c0-5.414,3.013-10.38,7.817-12.88c4.803-2.502,10.6-2.12,15.034,0.99l135.853,95.203c3.878,2.718,6.187,7.155,6.187,11.89s-2.31,9.172-6.187,11.89l-135.853,95.201C367.472,233.696,364.555,234.582,361.625,234.582z M376.146,57.561v134.597l96.036-67.299L376.146,57.561z"/><path style="fill:#FFFFFF;" d="M394.752,434.352H85.141c-8.017,0-14.519-6.502-14.519-14.519c0-8.017,6.502-14.519,14.519-14.519h309.611c48.639,0,88.21-39.572,88.21-88.21v-95.425c0-8.017,6.502-14.519,14.519-14.519S512,213.661,512,221.679v95.425C512,381.754,459.402,434.352,394.752,434.352z"/><path style="fill:#FFFFFF;" d="M394.752,370.938H230.196c-8.017,0-14.519-6.502-14.519-14.519c0-8.017,6.502-14.519,14.519-14.519h164.556c13.211,0,24.797-11.586,24.797-24.797V265.24c0-8.017,6.502-14.519,14.519-14.519c8.017,0,14.519,6.502,14.519,14.519v51.863C448.587,346.284,423.932,370.938,394.752,370.938z"/> </g> <polygon style="fill:#000000;" points="150.372,482.344 14.519,387.142 150.372,291.94 "/><path style="fill:#FFFFFF;" d="M150.373,496.863c-2.93,0-5.845-0.884-8.334-2.629L6.187,399.031C2.309,396.313,0,391.878,0,387.142 c0-4.736,2.31-9.172,6.187-11.89l135.853-95.201c4.436-3.109,10.229-3.49,15.034-0.99c4.804,2.5,7.817,7.466,7.817,12.88v190.405 c0,5.414-3.013,10.38-7.817,12.88C154.966,496.322,152.665,496.863,150.373,496.863z M39.818,387.142l96.036,67.3V319.844 L39.818,387.142z"/><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g></svg>
              </div>
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
              <button type="button" class="btn btn-secondary" id="close_modal" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn" :class="[sett ? 'modal-footer-light btn-primary' : 'modal-footer-dark btn-outline-dark']" data-bs-dismiss="modal" @click="test(example.value);">Save changes</button>
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
    initting: Boolean,
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
        placeholder: 'Select visitor',
        closeOnSelect: false,
        searchable: true,
        trackBy: 'value',
        label: 'value',
        object: true,
        groups: true,
        value: [],
      },
      type_build: '',
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
    if(process.env.VUE_APP_TYPE_BUILD){
      this.type_build = process.env.VUE_APP_TYPE_BUILD;
    } else {
      this.type_build = '__TYPE_BUILD__';
    }
    
    this.type_build = this.type_build.toLocaleLowerCase();
  },
  methods:{
    add_data(value){
      if (!this.initting) {
        this.$parent.initting = value;
        this.$parent.add_data();
      }
    },
    test(){
      if (this.example.value.length == 0){
        this.$parent.getList(this.value[0], this.value[1]);
      } else {
        // console.log(this.example.value)
        this.$parent.getList(this.value[0], this.value[1], this.example.value);
      }
    },
    changeTheme(newVal){
      this.$parent.sett = newVal;
    }
  }
}
</script>

<style>
#navigbar{
  /*box-shadow: 10px 0 5px -2px #888 inset;*/
  position: fixed;
  width: 100%;
  z-index: 5000;
  -webkit-appearance: none;
}
.shad{
  box-shadow:  0px -9px 5px -7px #777777 inset;;
  width: 100%;
  z-index: 10;
  -webkit-appearance: none;
}
.init{
  min-width: 2em;
  margin-left: 0.7em;
}
div.rot {
  animation: 1s linear 0s normal none infinite running rot;
  -webkit-animation: 1s linear 0s normal none infinite running rot;
  /*width: 100px;*/
}
@keyframes rot {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes rot {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.filling{
  fill: pink;
}
.color-light{
  color:  var(--bs-light);
}
.color-dark{
  color:  var(--bs-dark);
}
.multiselect-dark {
  --ms-placeholder-color: white;
  --ms-tag-bg: gold;
  --ms-tag-color: black;
  --ms-bg: #353535 !important;
  --ms-border-color: #727272;
  --ms-ring-color: gold;
  --ms-dropdown-bg: #353535;
  --ms-option-color-pointed: black !important;
  --ms-option-color-selected-pointed: #FFFFFF;

  --ms-option-bg-pointed: #555;
  --ms-option-color-pointed: white !important;
  --ms-option-color-selected: #FFFFFF;
  --ms-group-label-bg-selected-pointed: gold;
  --ms-group-label-bg-selected: #6c757d;
}
.multiselect-light{
  --ms-placeholder-color: black;
  --ms-tag-bg: var(--bs-blue);
  --ms-tag-color: white;
  --ms-border-color: #727272;
  --ms-ring-color: var(--bs-blue);
  --ms-option-color-pointed: white !important;
  --ms-option-color-selected-pointed: #FFFFFF;

  --ms-option-bg-pointed: #aaa;
  --ms-option-color-pointed: black !important;
  --ms-option-color-selected: #f0f;
  --ms-group-label-bg-selected-pointed: var(--bs-blue);
  --ms-group-label-bg-selected: #6c757d;
}

input.multiselect-tags-search{
  background-color: var(--ms-bg) !important;
}
.dp__theme_dark {
  --dp-background-color: #353535 !important;
  --dp-primary-color: gold !important;
  --dp-border-color: gold;
}
.modal-footer > .btn-outline-dark, .nav-form > .btn-outline-light{
  --bs-btn-color: gold;
  --bs-btn-border-color: gold;
  --bs-btn-hover-color: black;
  --bs-btn-hover-bg: gold;
  --bs-btn-hover-border-color: gold;
  --bs-btn-active-color: black;
  --bs-btn-active-bg: gold;
  --bs-btn-active-border-color: gold;
  --bs-btn-active-shadow: inset 0 3px 5px rgba(255, 215, 0, 0.125);
  --bs-btn-disabled-color: gold;
  --bs-btn-disabled-border-color: gold;
  --bs-gradient: none;
}
.dark-theme {
  fill: gold;
  margin-right: 2em;
  width: 3rem;
  height: 3rem;
}
.dark-light {
  fill: black;
  margin-right: 2em;
  width: 3rem;
  height: 3rem;
}
.logo_light{
  color: black;
}
.logo_dark{
  color: white !important;
}
.logo_light > .type{
  color: var(--bs-blue);
}
.logo_dark > .type{
  color: gold !important;
}
#logotype{
  width: 10%;
  font-family: 'Rubik Dirt', cursive;
  font-size: 2.3rem;
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
.modal-footer-light{
  /*--bs-btn-bg: */
}
.modal-footer-dark{
  --bs-btn-bg: gold;
}
.no-mode-fade-enter-active, .no-mode-fade-leave-active {
  transition: opacity .5s
}

.no-mode-fade-enter-from, .no-mode-fade-leave-to {
  opacity: 0
}
</style>
