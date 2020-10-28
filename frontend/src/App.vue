<template>
   <div id="app">
      <EventsListComponent/>
   </div>
</template>

<script>
import EventsListComponent from './components/EventsListComponent';
export default {
  name: 'App',
  components: {
    EventsListComponent,
  },
  data: () => ({
    //
  }),
};
</script>