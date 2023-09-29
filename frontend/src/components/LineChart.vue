<template>
  <CanvasJSChart
    :options="options"
    :style="styleOptions"
    @chart-ref="chartInstance"
  />
</template>
  
  <script>
// import { Line } from "vue-chartjs";
// import { D3LineChart } from "vue-d3-charts";
// import options as chartConfig from './chartConfig.js'

import CanvasJSChart from "@canvasjs/vue-charts";

export default {
  components: {
    CanvasJSChart,
  },
  data() {
    return {
      chart: null,
      options: {
        animationEnabled: true,
        exportEnabled: true,
        theme: "light2",
        title: {
          text: "UPI Transactions in India",
        },
        axisX: {
          valueFormatString: "YYYY",
          labelTextAlign: "center",
          labelAngle: 0,
        },
        axisY: {
          title: "Amount (in ₹ Crore)",
          valueFormatString: "₹##,##,##0cr",
        },
        data: [
          {
            type: "line",
            yValueFormatString: "₹##,##,##0.## crores",
            dataPoints: [
              { label: "2016", y: 893.07 },
              { label: "2017", y: 57020.87 },
              { label: "2018", y: 585710.45 },
              { label: "2019", y: 1836638.18 },
              { label: "2020", y: 3387744.72 },
              { label: "2021", y: 7159285.8 },
              { label: "2022 (Jan-Oct)", y: 10122170.33 },
            ],
          },
        ],
      },
      styleOptions: {
        width: "100%",
        height: "360px",
      },
    };
  },
  methods: {
    chartInstance(chart) {
      this.chart = chart;
    },
  },
};
</script>
  