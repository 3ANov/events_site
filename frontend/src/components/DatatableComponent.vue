<template>
  <div class="">
    <h1 style="text-align: center;">Datatable with 3rd Party API</h1>
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
      totalEvents: 0,
      numberOfPages: 0,
      results: [],
      loading: true,
      options: {},
      headers: [
        { text: "Passenger Name", value: "name" },
        { text: "Number Of Trips", value: "trips" },
        { text: "Airline", value: "airline[0].name" },
        { text: "Logo", value: "logo" },
        { text: "Website", value: "website" },
      ],
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
