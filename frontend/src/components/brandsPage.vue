<template>
  <div>
    <div class="brand-list">
      <h2 class="brand-title">{{ brand_name }}</h2>
    </div>
    <div class="brand-list">
      <router-link v-for="item in brandsCars" :key="item.id" :to="`/model/${item.id}`" class="brand-item">
        <div class="brand-center__img">
          <img :src="getPhoto(item)" alt="" class="brand-image">
        </div>
        <div class="brand-details">
          <h2 class="brand-name" @click="goToModelPage(item.id)">{{ item.model_name }}</h2>
          <div>
            <div class="brand">{{ item.model_years_of_production }} </div>
            <div class="brand">{{ item.model_body_type }} </div>
            <div class="brand">{{ item.model_wheel_drive_type }} </div>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      brandsCars: [],
      brand_name: '',
      brandsaveID: null,
    };
  },
  mounted() {
    this.brandsaveID = localStorage.getItem('brandsaveID');
    if (this.brandsaveID) {
      this.fetchData(this.brandsaveID);
    }
  },
  watch: {
    $route() {
      this.brandsaveID = this.$route.params.id;
      localStorage.setItem('brandsaveID', this.brandsaveID);
      this.fetchData(this.brandsaveID);
    },
  },
  methods: {
    getPhoto(detail) {
      try {
        const photoPath = detail.model_image.split('/images/CarModels/')[1];
        const fileName = photoPath.split('/').pop();
        return require(`@/../../backend/images/CarModels/${fileName}`);
      } catch (error) {
        console.error('Error loading photo:', error);
        return '';
      }
    },
    fetchData(id) {
      axios.get(`${process.env.VUE_APP_BACKEND_URL}/brands/`)
        .then((response) => {
          const brands = response.data.car_brand_info;
          const selectedBrand = brands.find(brand => brand.id === parseInt(id));
          if (selectedBrand) {
            this.types = brands;
            this.brand_name = selectedBrand.brand_name;
            this.brandsCars = selectedBrand.car_models_info;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goToModelPage(id) {
      this.$router.push(`/model/${id}`);
    }
  },
};
</script>

<style scoped>
.brand-title {
  text-align: center;
  font-style: normal;
  font-weight: 500;
  font-size: 38px;
  line-height: 130%;
  color: #333333;
  margin: 0 auto;
}
.brand-list {
  width: 1200px;
  margin: 30px auto 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.brand-item {
  width: calc(33.33% - 30px);
  margin-bottom: 40px;
  border: 1px solid #ddd;
  border-radius: 5px;
  overflow: hidden;
  position: relative;
  box-shadow: 0px 12px 24px rgba(16, 76, 139, 0.16); 
  border-radius: 15px;
  transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
  text-decoration: none;
}
.brand-item:hover {
  box-shadow: 0px 12px 24px rgba(16, 76, 139, 0.5); 
  transform: scale(1.05); 
}
.brand-item:nth-child(4n) {
  margin: 0 auto 40px;
}
.brand-center__img {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
.brand-image {
  height: 300px;
  width: 370px;
  object-fit: contain;
}
.brand-details {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  background-color: #051C34;
  text-decoration: none
}
.brand-details .brand-name {
  font-style: normal;
  font-weight: 500;
  font-size: 26px;
  line-height: 150%;
  color: white;
  margin: 0;
  border-bottom: none;

}
.brand-details .brand {
  font-style: normal;
  font-weight: 500;
  font-size: 17px;
  line-height: 150%;
  color: #c7c7c7;
}
.brand-name {
  font-size: 1.2em;
}
</style>