<template>
  <div class="container">
    <h1 class="text-center">Список событий</h1>

      <div class="d-flex justify-content-center">
        <b-button variant="primary" class="m-1" v-bind:href="previous">Previous</b-button>
        <b-button variant="primary" class="m-1" v-bind:href="next">Next</b-button>
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
        this.readDataFromAPI();
      },
    },
    deep: true,
  },
  methods: {
    readDataFromAPI() {
      this.loading = true;
      console.log("Page Number ", this.page);
      axios
          .get(
              "http://127.0.0.1:8000/api/events/" +
              "?page=" +
              this.page
          )
          .then((response) => {
            this.loading = false;
            this.next = response.data.next;
            this.previous = response.data.previous;
            this.results = response.data.results;
            this.totalEvents = response.data.count;
          });
    },
  },
  mounted() {
    this.readDataFromAPI();
  },
};
</script>
