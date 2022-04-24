import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import { priceSplit, phoneSplit } from "./scripts/globalFunctions";

let app = createApp(App);

// global properties --------
// django api url
app.config.globalProperties.apiUrl = "http://127.0.0.1:8000/api/";
// static files that come from django static
app.config.globalProperties.staticPath = "http://127.0.0.1:8000/static/";

// global function ----------
// for show Price splited exp :  45000 => 45,000
app.config.globalProperties.$priceSplit = priceSplit;
// for show phone splited exp :  09126411923 => 0912-641-1923
app.config.globalProperties.$phoneSplit = phoneSplit;

app.use(router).mount("#app");
