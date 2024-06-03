import { createRouter, createWebHashHistory } from 'vue-router';
import mainPC from './components/mainPage.vue';
import model from './components/modelPage.vue';
import brands from './components/brandsPage.vue';
import companyInformation from './components/companyInformation.vue';
import CabinFiltersPage from './components/part_components/Page_cabin_filters.vue';
import brakePads from './components/part_components/Page_brake_pads.vue';
import brakeFluids from './components/part_components/Page_brake_fluids.vue';
import engineOils from './components/part_components/Page_engine_oils.vue';
import oilFilters from './components/part_components/Page_oil_filters.vue';
import fuelFilters from './components/part_components/Page_fuel_filters.vue';
import airFilters from './components/part_components/Page_air_filters.vue';
import coolants from './components/part_components/Page_coolants.vue';
import transmissionOils from './components/part_components/Page_transmission_oils.vue';

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/', component: mainPC },
        { path: '/brands/:id', component: brands, props: true },
        { path: '/model/:id', name: 'model', component: model, props: true },
        { path: '/cabin_filters', name: 'CabinFilters', component: CabinFiltersPage },
        { path: '/brake_pads', name: 'brakePads', component: brakePads },
        { path: '/brake_fluids', name: 'brakeFluids', component: brakeFluids },
        { path: '/engine_oils', name: 'engineOils', component: engineOils },
        { path: '/oil_filters', name: 'oilFilters', component: oilFilters },
        { path: '/fuel_filters', name: 'fuelFilters', component: fuelFilters },
        { path: '/air_filters', name: 'airFilters', component: airFilters },
        { path: '/coolants', name: 'coolants', component: coolants },
        { path: '/transmission_oils', name: 'transmissionOils', component: transmissionOils },
        { path: '/company_information', component: companyInformation },
    ]
});

router.beforeEach((to, from, next) => {
    window.scrollTo(0, 0);
    next();
});

export default router;
