<template>
  <div class="find-bar">
    <input type="text" v-model="searchModel" @input="handleInput" placeholder="Знайти..." ref="searchInput" class="search-sel" @click="showsearchMod = true">
    <ul v-if="showsearchMod" class="selects search-results">
      <li v-for="searchResult in searchResults" :key="searchResult.id" @click="selectProduct(searchResult)">
        <router-link :to="{ name: 'model', params: { id: searchResult.id }}" class="product-items">
          {{ searchResult.model_name }} - ({{ searchResult.model_years_of_production }})
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      search: [],
      searchModel: "",
      showsearchMod: false,
      searchResults: [],
    };
  },
  mounted() {
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/home/`)
      .then((response) => {
        this.search = response.data.car_models_info;
        console.log(this.search)
      })
      .catch((error) => {
        console.log(error);
      });
    document.addEventListener('click', (event) => {
      if (!this.$refs.searchInput.contains(event.target)) {
        this.showsearchMod = false;
      }
    });
  },
  methods: {
    handleInput() {
      this.searchResults = [];
      let counter = 0; 
      if (this.searchModel.length > 0) {
        this.search.forEach(product => {
          if (counter >= 5) return; 
          if (product.model_name.toLowerCase().includes(this.searchModel.toLowerCase())) {
            this.searchResults.push(product);
            counter++;
          }
        });
        this.showsearchMod = true;
      } else {
        this.showsearchMod = false;
      }
    },
    selectProduct(product) {
      this.searchModel = "";
      this.showsearchMod = false;
      localStorage.setItem('selectedProductId', product.id.toString());
      this.searchResults = []; 
    },
  },
};
</script>
<style>
.find-bar {
  position: relative;
}
.find-bar input {
  background-color: #f5f9ff;
}
.search-sel {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 1px;
  padding: 12px;
  font-size: 16px;
  background-color: #fff0f0;
  width: 220px;
  box-shadow: 0 2px 4px;
  transition: background-color 0.3s ease;
}
.selects {
  margin: 0;
  padding: 0;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  border-top: none;
  border-radius: 0 0 5px 5px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  z-index: 1;
}
.selects li {
  padding: 10px;
  width: 223px;

  cursor: pointer;
  list-style: none;
}
.selects li:hover {
  background-color: #f5f5f5;
}
.selects a {
  text-decoration: none;
  color: #333;
}
</style>