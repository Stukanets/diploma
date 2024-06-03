from django.urls import path
from .views import (HomePageView, InformationPageView, BrandPageView, ModelPageView, SelectedCabinFilters,
                    SelectedBrakePads, SelectedBrakeFluids, SelectedEngineOils, SelectedOilFilters, SelectedFuelFilters,
                    SelectedAirFilters, SelectedCoolants, SelectedTransmissionOils)


urlpatterns = [
    path('home/', HomePageView.as_view()),
    path('company_information/', InformationPageView.as_view()),
    path('brands/', BrandPageView.as_view()),
    path('models/', ModelPageView.as_view()),
    path('selected_cabin_filters/', SelectedCabinFilters.as_view()),
    path('selected_brake_pads/', SelectedBrakePads.as_view()),
    path('selected_brake_fluids/', SelectedBrakeFluids.as_view()),
    path('selected_engine_oils/', SelectedEngineOils.as_view()),
    path('selected_oil_filters/', SelectedOilFilters.as_view()),
    path('selected_fuel_filters/', SelectedFuelFilters.as_view()),
    path('selected_air_filters/', SelectedAirFilters.as_view()),
    path('selected_coolants/', SelectedCoolants.as_view()),
    path('selected_transmission_oils/', SelectedTransmissionOils.as_view())
]
