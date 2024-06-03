<template>
  <div class="center-page">
    <div>
      <div class="main__display">
        <div class="model-image-dev">
          <img :src="getPhoto(model)" alt="" class="model-img">
        </div>
        <div class="model-desc">
          <div class="model-info">
            <h2 class="model-name">{{ model.model_name }}</h2>
            <div class="model-details">
              <table class="info-table last-mar">
                <tbody>
                  <tr>
                    <td class="info-label">Роки виходу:</td>
                    <td class="info-value">{{ model.model_years_of_production }}</td>
                  </tr>
                  <tr>
                    <td class="info-label">Тип кузова:</td>
                    <td class="info-value">{{ model.model_body_type }}</td>
                  </tr>
                  <tr>
                    <td class="info-label">Привід:</td>
                    <td class="info-value">{{ model.model_wheel_drive_type }}</td>
                  </tr>
                </tbody>
              </table>
              <div class="model-description">
                <span class="info-label">Опис моделі:</span>
                <span class="info-value">{{ lowercaseFirstWord(model.model_description) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <table class="dropdown-table">
          <tr>
              <td class="dropdown-label">Двигун:</td>
              <td class="dropdown-select">
                  <select id="engine-dropdown" v-model="selectedEngine" class="narrow-select" @change="handleSelectChange">
                      <option v-for="engine in model.car_engines_info" :key="engine.id" :value="engine">
                          {{ engine.engine_name }} (Об'єм: {{ engine.engine_capacity }}, КС: {{ engine.engine_hp }}, Циліндрів: {{ engine.engine_number_of_cylinders }}, Клапанів: {{ engine.engine_number_of_valves }}, Тип палива: {{ engine.engine_fuel_type }})
                      </option>
                  </select>
              </td>
          </tr>
          <tr>
              <td class="dropdown-label">Трансмісія:</td>
              <td class="dropdown-select">
                  <select id="transmission-dropdown" v-model="selectedTransmission" class="wide-select" @change="handleSelectChange">
                      <option v-for="transmission in model.car_transmissions_info" :key="transmission.id" :value="transmission">{{ transmission.transmission_type }}</option>
                  </select>
              </td>
          </tr>
      </table>
      <div v-if="error" class="error-message">{{ error }}</div>
      <div class="dropdown-table">
        <button class="submit-button" @click="submitForm">Підбір розхідників</button>
        <p v-if="showLink" class="mar">Результати підбору:</p>
        <div class="submit-link" :class="{ 'fade-in': showLink }">
          <a v-if="showLink" target="_blank" href="#/cabin_filters" @click="submitData">Фільтри салону</a>
          <a v-if="showLink" target="_blank" href="#/brake_pads" @click="submitData">Гальмівні колодки</a>
          <a v-if="showLink" target="_blank" href="#/brake_fluids" @click="submitData">Гальмівні рідини</a>
          <a v-if="showLink" target="_blank" href="#/engine_oils" @click="submitData">Моторні оливи</a>
          <a v-if="showLink" target="_blank" href="#/oil_filters" @click="submitData">Масляні фільтри</a>
          <a v-if="showLink" target="_blank" href="#/fuel_filters" @click="submitData">Паливні фільтри</a>
          <a v-if="showLink" target="_blank" href="#/air_filters" @click="submitData">Повітряні фільтри</a>
          <a v-if="showLink" target="_blank" href="#/coolants" @click="submitData">Охолоджувальні рідини</a>
          <a v-if="showLink" target="_blank" href="#/transmission_oils" @click="submitData">Трансмісійні оливи</a>
        </div>
        <div class="space" v-show="showLink"></div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      model: [],
      selectedEngine: null,
      selectedTransmission: null,
      error: '',
      showLink: false,
    };
  },
  mounted() {
    this.fetchData();
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
  fetchData() {
    const id = parseInt(this.$route.params.id);
    axios
      .get(`${process.env.VUE_APP_BACKEND_URL}/models/`)
      .then(response => {
        const models = response.data.car_model_engines_and_transmissions_info;
        if (Array.isArray(models)) {
          this.model = models.find(device => device.id === id);
        } else {
          console.log('Invalid data format received from the API.');
        }
      })
      .catch(error => {
        console.log('Error fetching data:', error);
      })
  },
  lowercaseFirstWord(description) {
    if (!description) return '';
    return description.charAt(0).toLowerCase() + description.slice(1);
  },
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
  submitForm() {
    if (!this.selectedEngine && !this.selectedTransmission) {
      this.error = 'Please select an engine and a transmission.';
    } else if (!this.selectedEngine) {
      this.error = 'Please select an engine.';
    } else if (!this.selectedTransmission) {
      this.error = 'Please select a transmission.';
    } else {
      this.error = '';
      const selectedIds = {
        Model: this.model.id,
        Engine: this.selectedEngine.id,
        Transmission: this.selectedTransmission.id,
      };
      console.log(selectedIds);
      this.showLink = true; 
    }
  },
  submitData() {
        if (this.selectedEngine && this.selectedTransmission) {
          const modelId = this.model.id;
          const engineId = this.selectedEngine.id;
          const transmissionId = this.selectedTransmission.id;
          const data = [modelId, engineId, transmissionId];
          console.log('Data being sent:', data);
          const userInfo = {
            "model_id": modelId,
            "engine_id": engineId,
            "transmission_id": transmissionId,
          };
          localStorage.setItem('cabinFilterData', JSON.stringify(data));
          localStorage.setItem('userInfo', JSON.stringify(userInfo));
        } else {
          console.log('Please select an engine and transmission.');
        }
    },
    handleSelectChange() {
        this.showLink = false;
    }
  }
};
</script>
  
<style>
.main__display {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 40px 0;
  gap: 40px;
}
select option {
  font-size: 16px; 
}
.mar {
  margin: -10px 0 20px;
}
.last-mar {
  margin-bottom: 20px;
}
.submit-link {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}
.fade-in {
  opacity: 1 !important;
}
.submit-link a {
  display: block;
  padding: 10px;
  text-align: center;
  background-color: #051C34; 
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s ease-in-out;
}
.submit-link a:hover {
  background-color: #1572D3;
}
.space {
  height: 40px;
  transition: height 0.5s ease-in-out;
}
.error-message {
  margin-top: 10px;
  color: red;
  font-size: 14px;
  text-align: center;
}
.submit-button {
  margin: 25px auto;
  padding: 10px 20px;
  background-color: #051C34;
  color: #fff;
  font-size: 18px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  transition: background-color 0.3s ease-in-out;

}
.submit-button:hover {
  background-color: #1572D3;
}
.center-page {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
}
.model-desc {
  display: flex;
  flex-wrap: wrap;
  max-width: 500px;
  background-color: #fff;
  box-shadow: 1px 1px 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px 20px 0;
  border-radius: 4px;
}
.model-name {
  font-size: 24px;
  color: #333;
  margin: 0 0 20px;
  text-align: center;
}
.model-details {
  margin-bottom: 20px;
}
.info-table {
  width: 250px;
  border-collapse: collapse;
  margin: 20px auto;
}
.info-label {
  font-weight: bold;
  color: #666;
  padding-bottom: 7px;
}
.info-value {
  color: #333;
  text-align: center;
}
.model-description {
  text-align: justify;
  line-height: 1.3;
}
.model-description .info-value {
  color: #333;
  text-align: left;
  padding-left: 10px;
}
.model-description .info-value {
  color: #333;
}
.dropdown-container {
  margin-bottom: 20px;
}
.dropdown-label {
  font-weight: bold;
  margin-right: 10px;
  color: #666;
}
.narrow-select {
  width: 200px;
  height: 32px;
  padding: 4px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
  color: #333;
}
.wide-select {
  width: 300px;
  height: 32px;
  padding: 4px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
  color: #333;
}
.model-image-dev {
  margin: 0 auto;
  margin: 20px 0;
  z-index: -10;
  text-align: center;
}
.model-image-dev .model-img {
  width: 750px;
  height: 380px;
  object-fit: cover;
}
.dropdown-table {
  width: 850px;
  margin: 0 auto 40px;
  border-collapse: collapse;
}
.dropdown-table td {
  padding: 10px 10px 10px 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.dropdown-table tr {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}
.dropdown-label {
  font-weight: bold;
  color: #666;
}
.dropdown-select {
  position: relative;
}
.narrow-select,
.wide-select {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 32px;
  padding: 4px;
  border: none;
  background-color: transparent;
  font-size: 14px;
  color: #333;
  appearance: none;
}
.dropdown-select::after {
  content: "";
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid #666;
}
</style>