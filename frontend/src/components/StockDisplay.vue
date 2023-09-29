<template>
  <div>
    <h2>Stock data</h2>
    <LineChart2 />
    <!-- <h1>JSON Data from REST API</h1>
    {{ apiData["Open"] }}
    <br />
    {{ apiData["Close"] }}
    <ul v-if="apiData">
      <li v-for="(item, index) in apiData" :key="index">
        {{ index }} - {{ item }}
      </li>
    </ul>
    <p v-else>Loading data...</p> -->
  </div>
</template>


<script>
/* // import * as d3 from 'd3';
import {
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
); */
import LineChart2 from "./LineChart2.vue";

export default {
  components: { LineChart2 },
  data() {
    return {
      apiData: [],
    };
  },
  mounted() {
    fetch("http://localhost:8000/stock/AAPL")
      .then((response) => response.json())
      .then((data) => {
        this.apiData = data;
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  },
};
</script>
  
  <style scoped>
/* Component-specific styles go here */
</style>
  