<template>
   <div id="app">
      <DatatableComponent/>
   </div>
</template>

<script>
import DatatableComponent from './components/DatatableComponent';
export default {
  name: 'App',
  components: {
    DatatableComponent,
  },
  data: () => ({
    //
  }),
};
</script>