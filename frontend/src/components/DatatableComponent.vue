<template>
  <div class="container">
    <h1 class="text-center">Список событий</h1>

    <div class="d-flex justify-content-center">
      <b-button variant="primary" class="m-1" v-on:click="click_previous">Previous</b-button>
      <b-button variant="primary" class="m-1" v-on:click="click_next">Next</b-button>
    </div>
    <ul id="example-1">
      <li v-for="event in results" v-bind:key="event.id">
        {{ event.title }}
      </li>
    </ul>
  </div>
</template>
<style scoped></style>
<script>
import axios from "axios";


export default {
  name: "DatatableComponent",
  data() {
    return {
      page: 1,
      current_url: "http://127.0.0.1:8000/api/events/?page=1",
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
      console.log("Page Number ", this.page);
      console.log("Current url ", url);
      console.log(this.page);
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
    }
  },
  mounted() {
    this.readDataFromAPI(this.current_url);
  },

};

</script>
