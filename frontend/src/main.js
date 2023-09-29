import { createApp, h } from 'vue';
import App from './App.vue';


//import CanvasJSC from 'canvasjs';
//App.use(CanvasJSChart);
//import CanvasJSChart from "@canvasjs/vue-charts";

//const app = createApp(App)
const app = createApp({
    render: () => h(App)
});
//app.use(CanvasJSChart);
app.mount('#app')
