<template>
  <div>
    <h2>Stock data</h2>
    <input v-model="stock" type="text" placeholder="AAPL" />
    <button @click="getStockData">Submit</button>
    <LineChart2 :ticker="stock" ref="lineChartRef" />
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
      stock: "AAPL",
    };
  },
  methods: {
    getStockData: function () {
      this.$refs.lineChartRef.getData();
      
      /* const url = "http://localhost:8000/stock/" + this.stock;
      console.log("trying " + url + " data");
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          this.apiData = data;
          console.log("got " + this.stock + " data");
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        }); */
    },
  },
  mounted() {
    this.getStockData();
  },
};
</script>
  
  <style scoped>
/* Component-specific styles go here */
</style>
  