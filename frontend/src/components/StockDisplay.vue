<template>
  <div>
    <h1>JSON Data from REST API</h1>
    {{ apiData['Open'] }}
    <br>
    {{ apiData['Close'] }}
    <ul v-if="apiData">
      <li v-for="(item, index) in apiData" :key="index">
         <!-- {{ item.name }} - {{ item.description }} -->
         {{ item.name }} - {{ item }}
      </li>
    </ul>
    <p v-else>Loading data...</p>
  </div>
</template>


  <script>
  export default {
    data() {
      return {
        apiData: [],
      };
    },
    mounted() {
      // Fetch data from the REST API
      // You can use axios or fetch API here
      fetch('http://localhost:8000/stock/AAPL')
        .then((response) => response.json())
        .then((data) => {
          this.apiData = data;
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });
    },
  };
  </script>
  
  <style scoped>
  /* Component-specific styles go here */
  </style>
  