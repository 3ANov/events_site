<template>
  <div>
    <h3>{{event_data.title}} </h3>
    <p>{{event_data.description}} </p>
    <ul>
        <li v-for="event_instance in event_data.event_instances"
            v-bind:key="event_instance.id">
          <span class="mr-3">{{ event_instance.time_start }}</span>
          <span class="mr-3 font-italic">{{ event_instance.place.name }}</span>
          <span>{{ event_instance.place.city }}</span>
        </li>
      </ul>
  </div>
</template>

<script>
export default {
name: "EventDataComponent",
  props: {
    event_data: {
      id: Number,
      title: String,
      description: String,
      event_instances: Array,
      category: String
    },
  },

}
</script>

<style scoped>

</style>