<template>
  <div class="container">
    <h1 class="text-center">Список событий</h1>
    <div class="d-flex justify-content-center">
      <b-button variant="primary" class="m-1" v-on:click="click_previous">Previous</b-button>
      <b-button variant="primary" class="m-1" v-on:click="click_next">Next</b-button>
    </div>
    <div class="row">
      <ul class="list-group mt-2 col-6">
        <li v-for="event in results"
            v-bind:key="event.id"
            class="list-group-item"
            v-on:click="show_event_data(event)">
          {{ event.title }}
        </li>
      </ul>
      <div class="col-6 mt-3 d-none" id="event-extern-data">
        <EventDataComponent v-bind:event_data="current_event"/>
      </div>
    </div>
  </div>
</template>
<style scoped></style>
<script>
import axios from "axios";
import EventDataComponent from "@/components/EventDataComponent";



export default {
  name: "EventsListComponent",
  components: {EventDataComponent},
  data() {
    return {
      page: 1,
      current_url: "http://127.0.0.1:8000/api/events/?page=1",
      current_event: [],
      next: null,
      previous: null,
      totalEvents: 0,
      results: [],
      loading: true,
    };
  },
  watch: {
    options: {
      handler() {
        this.readDataFromAPI(this.current_url);
      },
    },
    deep: true,
  },
  methods: {
    readDataFromAPI(url) {
      this.loading = true;
      // console.log("Page Number ", this.page);
      // console.log("Current url ", url);
      // console.log(this.page);
      axios
          .get(url)
          .then((response) => {
            this.loading = false;
            this.next = response.data.next;
            this.previous = response.data.previous;
            this.results = response.data.results;
            this.totalEvents = response.data.count;
          });
    },
    click_next: function () {
      if (this.next != null){
        this.readDataFromAPI(this.next)
      }
    },
    click_previous: function () {
      if(this.previous != null){
        this.readDataFromAPI(this.previous)
      }
    },
    show_event_data: function (event_data) {
      document.getElementById('event-extern-data').classList.remove('d-none');
      this.current_event = event_data;
    }
  },
  mounted() {
    this.readDataFromAPI(this.current_url);
  },

};

</script>
