<template>
  <div>
    <div v-if="data">
      <Line :data="data" :options="options" :style="myStyles" />
    </div>
    <p v-else>Loading data...</p>
  </div>
</template>
  
<script>
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

import { Line } from "vue-chartjs";
import { myStyles, options } from "./chartConfig.js";

// const options = {
//   responsive: false,
//   maintainAspectRatio: true,
// };

// const myStyles = {
//   height: "200px",
//   width: "300px",
//   //position: 'relative'
//   margin: "auto",
// };

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default {
  props: ["ticker"],
  setup(props) {
    console.log("ticker: " + props.ticker);
  },
  watch: {
    ticker(val) {
      if (val == "AAPL") {
        console.log("apple");
      }
    },
  },
  methods: {
    getData() {
      this.loaded = false;
      const url = "http://localhost:8000/stock/" + this.ticker;
      fetch(url)
        .then((response) => response.json())
        .then((apiData) => {
          //console.log(apiData);
          const d = {
            labels: Object.keys(apiData["Close"]),
            datasets: [
              {
                label: this.ticker,
                backgroundColor: "#f87979",
                data: Object.values(apiData["Close"]),
              },
            ],
          };
          this.data = d;
          this.loaded = true;
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },
  },
  components: {
    Line,
  },
  //   data() {
  //     return chartConfig;
  //   }
  data: () => ({
    loaded: false,
    data: null,
    options: options,
    myStyles: myStyles,
  }),

  mounted() {
    this.getData();
  },
};
</script>
  