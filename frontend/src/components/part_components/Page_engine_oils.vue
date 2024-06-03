<template>
  <div class="background-car">
    <div class="info-container">
      <h1 class="name_for">Моторні оливи</h1>
      <div v-for="(filter, index) in engineOils" :key="index" class="container-cards">
        <div v-for="(detail, detailIndex) in filter" :key="detailIndex" class="container-details">
          <div class="container-names"> 
            <h2>{{ detail.engine_oil_name }}</h2>
          </div>
          <div class="container-image">
            <img :src="getPhoto(detail)" alt="Cabin Filter Photo" class="contain-image">
          </div>
          <div class="container-type">
            <p>Тип: {{ detail.engine_oil_type }}</p>
          </div>
          <div class="container-brands">
            <p>Густина: {{ detail.engine_oil_density }}</p>
          </div>
          <div class="container-brands">
            <p>Допуски: {{ detail.engine_oil_tolerances }}</p>
          </div>
          <div class="container-brands">
            <p>Марка: {{ detail.engine_oil_brand }}</p>
          </div>
          <div class="container-description">
            <p>{{ detail.engine_oil_description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      engineOils: [],
      loading: true,
    };
  },
  created() {
    this.fetchCabinFilters();
  },
  methods: {
    getPhoto(detail) {
      try {
        const photoPath = detail.engine_oil_image.split('/images/EngineOils/')[1];
        const fileName = photoPath.split('/').pop();
        return require(`@/../../backend/images/EngineOils/${fileName}`);
      } catch (error) {
        console.error('Error loading photo:', error);
        return '';
      }
    },
    fetchCabinFilters() {
      const data = JSON.parse(localStorage.getItem('userInfo'));
      console.log(data);
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/selected_engine_oils/`, data)
        .then(response => {
          this.engineOils = { ...response.data };
          console.log(this.engineOils);
        })
        .catch(error => {
          console.log('Error fetching cabin filters:', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style>
.container-image {
  display: flex;
  justify-content: center;
}
.contain-image {
  width: 400px;
}
</style>