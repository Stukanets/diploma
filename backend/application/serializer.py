from rest_framework.serializers import ModelSerializer
from .models import (CompanyInfo, CarBrand, CarModel, CarEngine, CarTransmission, CabinFilter, BrakePad, BrakeFluid,
                     EngineOil, OilFilter, FuelFilter, AirFilter, Coolant, TransmissionOil)


class CompanyInfoSerializer(ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ['company_name',
                  'company_email',
                  'company_phone_number']


class CarBrandsNameInfoSerializer(ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ['id',
                  'brand_name']


class CarModelsInfoSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id',
                  'model_name',
                  'model_years_of_production',
                  'model_body_type',
                  'model_wheel_drive_type',
                  'model_description',
                  'model_image']


class CompanyExtendedInfoSerializer(ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ['company_name',
                  'company_owner',
                  'company_email',
                  'company_phone_number',
                  'company_first_address',
                  'company_second_address',
                  'company_address_google_map']


class CarBrandsInfoSerializer(ModelSerializer):
    car_models_info = CarModelsInfoSerializer(many=True, read_only=True)

    class Meta:
        model = CarBrand
        fields = ['id',
                  'brand_name',
                  'brand_location',
                  'brand_year_of_establishment',
                  'brand_description',
                  'brand_logo_image',
                  'brand_website_link',
                  'car_models_info']


class CarEnginesInfoSerializer(ModelSerializer):
    class Meta:
        model = CarEngine
        fields = ['id',
                  'engine_name',
                  'engine_capacity',
                  'engine_hp',
                  'engine_number_of_cylinders',
                  'engine_number_of_valves',
                  'engine_fuel_type']


class CarTransmissionsInfoSerializer(ModelSerializer):
    class Meta:
        model = CarTransmission
        fields = ['id',
                  'transmission_type']


class CarModelsEngineAndTransmissionInfoSerializer(ModelSerializer):
    car_engines_info = CarEnginesInfoSerializer(many=True, read_only=True)
    car_transmissions_info = CarTransmissionsInfoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = ['id',
                  'model_name',
                  'model_years_of_production',
                  'model_body_type',
                  'model_wheel_drive_type',
                  'model_description',
                  'model_image',
                  'car_engines_info',
                  'car_transmissions_info']


class CabinFiltersInfoSerializer(ModelSerializer):
    class Meta:
        model = CabinFilter
        fields = ['id',
                  'cabin_filter_name',
                  'cabin_filter_type',
                  'cabin_filter_brand',
                  'cabin_filter_description',
                  'cabin_filter_image']


class BrakePadsInfoSerializer(ModelSerializer):
    class Meta:
        model = BrakePad
        fields = ['id',
                  'brake_pad_name',
                  'brake_pad_type',
                  'brake_pad_brand',
                  'brake_pad_description',
                  'brake_pad_image']


class BrakeFluidsInfoSerializer(ModelSerializer):
    class Meta:
        model = BrakeFluid
        fields = ['id',
                  'brake_fluid_name',
                  'brake_fluid_type',
                  'brake_fluid_brand',
                  'brake_fluid_description',
                  'brake_fluid_image']


class EngineOilsInfoSerializer(ModelSerializer):
    class Meta:
        model = EngineOil
        fields = ['id',
                  'engine_oil_name',
                  'engine_oil_type',
                  'engine_oil_density',
                  'engine_oil_tolerances',
                  'engine_oil_brand',
                  'engine_oil_description',
                  'engine_oil_image']


class OilFiltersInfoSerializer(ModelSerializer):
    class Meta:
        model = OilFilter
        fields = ['id',
                  'oil_filter_name',
                  'oil_filter_brand',
                  'oil_filter_description',
                  'oil_filter_image']


class FuelFiltersInfoSerializer(ModelSerializer):
    class Meta:
        model = FuelFilter
        fields = ['id',
                  'fuel_filter_name',
                  'fuel_filter_type',
                  'fuel_filter_brand',
                  'fuel_filter_description',
                  'fuel_filter_image']


class AirFiltersInfoSerializer(ModelSerializer):
    class Meta:
        model = AirFilter
        fields = ['id',
                  'air_filter_name',
                  'air_filter_type',
                  'air_filter_brand',
                  'air_filter_description',
                  'air_filter_image']


class CoolantsInfoSerializer(ModelSerializer):
    class Meta:
        model = Coolant
        fields = ['id',
                  'coolant_name',
                  'coolant_type',
                  'coolant_color',
                  'coolant_brand',
                  'coolant_description',
                  'coolant_image']


class TransmissionOilsInfoSerializer(ModelSerializer):
    class Meta:
        model = TransmissionOil
        fields = ['id',
                  'transmission_oil_name',
                  'transmission_oil_type',
                  'transmission_oil_atf_type',
                  'transmission_oil_brand',
                  'transmission_oil_description',
                  'transmission_oil_image']
