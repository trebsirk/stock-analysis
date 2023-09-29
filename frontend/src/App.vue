<template>
  <div>
    <StockDisplay />
  </div>
</template>

<script>
//import LineChart from "./components/LineChart.vue";
import StockDisplay from "./components/StockDisplay.vue";

export default {
  name: "App",
  components: {
    StockDisplay,
    //LineChart
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
