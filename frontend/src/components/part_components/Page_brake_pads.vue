<template>
  <div class="background-car">
    <div class="info-container">
      <h1 class="name_for">Гальмівні колодки</h1>
      <div v-for="(filter, index) in brakePad" :key="index" class="container-cards">
        <div v-for="(detail, detailIndex) in filter" :key="detailIndex" class="container-details">
          <div class="container-names"> 
            <h2>{{ detail.brake_pad_name }}</h2>
          </div>
          <div class="container-image">
            <img :src="getPhoto(detail)" alt="Cabin Filter Photo" class="contain-image">
          </div>
          <div class="container-type">
            <p>Тип: {{ detail.brake_pad_type }}</p>
          </div>
          <div class="container-brands">
            <p>Марка: {{ detail.brake_pad_brand }}</p>
          </div>
          <div class="container-description">
            <p>{{ detail.brake_pad_description }}</p>
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
      brakePad: [],
      loading: true,
    };
  },
  created() {
    this.fetchCabinFilters();
  },
  methods: {
    getPhoto(detail) {
      try {
        const photoPath = detail.brake_pad_image.split('/images/BrakePads/')[1];
        const fileName = photoPath.split('/').pop();
        return require(`@/../../backend/images/BrakePads/${fileName}`);
      } catch (error) {
        console.error('Error loading photo:', error);
        return '';
      }
    },
    fetchCabinFilters() {
      const data = JSON.parse(localStorage.getItem('userInfo'));
      console.log(data);
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/selected_brake_pads/`, data)
        .then(response => {
          this.brakePad = { ...response.data };
          console.log(this.brakePad);
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
.less {
  height: 300px;
  width: 400px;
  object-fit: cover;
}
.container-image {
  display: flex;
  justify-content: center;
}
</style>