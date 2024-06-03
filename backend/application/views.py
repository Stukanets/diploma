from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (CompanyInfo, CarBrand, CarModel, CarModelCabinFilter, CabinFilter, CarModelBrakePad, BrakePad,
                     CarModelBrakeFluid, BrakeFluid, CarEngineEngineOil, EngineOil, CarEngineOilFilter, OilFilter,
                     CarEngineFuelFilter, FuelFilter, CarEngineAirFilter, AirFilter, CarEngineCoolant, Coolant,
                     CarTransmissionTransmissionOil, TransmissionOil)
from .serializer import (CompanyInfoSerializer, CarBrandsNameInfoSerializer, CarModelsInfoSerializer,
                         CompanyExtendedInfoSerializer, CarBrandsInfoSerializer,
                         CarModelsEngineAndTransmissionInfoSerializer, CabinFiltersInfoSerializer,
                         BrakePadsInfoSerializer, BrakeFluidsInfoSerializer, EngineOilsInfoSerializer,
                         OilFiltersInfoSerializer, FuelFiltersInfoSerializer, AirFiltersInfoSerializer,
                         CoolantsInfoSerializer, TransmissionOilsInfoSerializer)


class CompanyInformation:
    @staticmethod
    def get():
        company_info = CompanyInfoSerializer(CompanyInfo.objects, many=True)
        return company_info.data


class CarBrandName:
    @staticmethod
    def get():
        car_brand_name_ = CarBrandsNameInfoSerializer(CarBrand.objects, many=True)
        return car_brand_name_.data


class CarModelInformation:
    @staticmethod
    def get():
        car_model_info = CarModelsInfoSerializer(CarModel.objects, many=True)
        return car_model_info.data


class Top3CarsInformation:
    @staticmethod
    def get():
        car_model_info = CarModelsInfoSerializer(CarModel.objects.filter(Q(id=4) | Q(id=5) | Q(id=10)), many=True)
        return car_model_info.data


class HomePageView(APIView):
    @staticmethod
    def get(request):
        company_info = CompanyInformation.get()
        car_brand_name_info = CarBrandName.get()
        car_model_info = CarModelInformation.get()
        top_3_cars_info = Top3CarsInformation.get()
        return Response({'company_info': company_info,
                         'car_brand_name_info': car_brand_name_info,
                         'car_models_info': car_model_info,
                         'top_3_cars_info': top_3_cars_info})


class CompanyExtendedInformation:
    @staticmethod
    def get():
        company_extended_info = CompanyExtendedInfoSerializer(CompanyInfo.objects, many=True)
        return company_extended_info.data


class InformationPageView(APIView):
    @staticmethod
    def get(request):
        company_extended_info = CompanyExtendedInformation.get()
        return Response({'company_extended_info': company_extended_info})


class CarBrandInformation:
    @staticmethod
    def get():
        car_brand_info = CarBrandsInfoSerializer(CarBrand.objects, many=True)
        return car_brand_info.data


class BrandPageView(APIView):
    @staticmethod
    def get(request):
        car_brand_info = CarBrandInformation.get()
        return Response({'car_brand_info': car_brand_info})


class CarModelsEngineAndTransmissionInformation:
    @staticmethod
    def get():
        car_model_engine_and_transmission_info = CarModelsEngineAndTransmissionInfoSerializer(
            CarModel.objects, many=True)
        return car_model_engine_and_transmission_info.data


class ModelPageView(APIView):
    @staticmethod
    def get(request):
        car_model_engine_and_transmission_info = CarModelsEngineAndTransmissionInformation.get()
        return Response({'car_model_engines_and_transmissions_info': car_model_engine_and_transmission_info})


class SelectedCabinFilters(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        model_id = post_data.get('model_id')

        selected_cabin_filters_id = [elem.cabin_filter.id for elem in CarModelCabinFilter.objects.filter(
            car_model_id=model_id)]
        cabin_filter_info = CabinFiltersInfoSerializer(CabinFilter.objects.filter(id__in=selected_cabin_filters_id),
                                                       many=True).data
        return Response({'cabin_filter_info': cabin_filter_info})


class SelectedBrakePads(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        model_id = post_data.get('model_id')

        selected_brake_pads_id = [elem.brake_pad.id for elem in CarModelBrakePad.objects.filter(
            car_model_id=model_id)]
        brake_pads_info = BrakePadsInfoSerializer(BrakePad.objects.filter(id__in=selected_brake_pads_id),
                                                  many=True).data
        return Response({'brake_pads_info': brake_pads_info})


class SelectedBrakeFluids(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        model_id = post_data.get('model_id')

        selected_brake_fluids_id = [elem.brake_fluid.id for elem in CarModelBrakeFluid.objects.filter(
            car_model_id=model_id)]
        brake_fluids_info = BrakeFluidsInfoSerializer(BrakeFluid.objects.filter(id__in=selected_brake_fluids_id),
                                                      many=True).data
        return Response({'brake_fluids_info': brake_fluids_info})


class SelectedEngineOils(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        engine_id = post_data.get('engine_id')

        selected_engine_oils_id = [elem.engine_oil.id for elem in CarEngineEngineOil.objects.filter(
            car_engine_id=engine_id)]
        engine_oils_info = EngineOilsInfoSerializer(EngineOil.objects.filter(id__in=selected_engine_oils_id),
                                                    many=True).data
        return Response({'engine_oils_info': engine_oils_info})


class SelectedOilFilters(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        engine_id = post_data.get('engine_id')

        selected_oil_filters_id = [elem.oil_filter.id for elem in CarEngineOilFilter.objects.filter(
            car_engine_id=engine_id)]
        oil_filters_info = OilFiltersInfoSerializer(OilFilter.objects.filter(id__in=selected_oil_filters_id),
                                                    many=True).data
        return Response({'oil_filters_info': oil_filters_info})


class SelectedFuelFilters(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        engine_id = post_data.get('engine_id')

        selected_fuel_filters_id = [elem.fuel_filter.id for elem in CarEngineFuelFilter.objects.filter(
            car_engine_id=engine_id)]
        fuel_filters_info = FuelFiltersInfoSerializer(FuelFilter.objects.filter(id__in=selected_fuel_filters_id),
                                                      many=True).data
        return Response({'fuel_filters_info': fuel_filters_info})


class SelectedAirFilters(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        engine_id = post_data.get('engine_id')

        selected_air_filters_id = [elem.air_filter.id for elem in CarEngineAirFilter.objects.filter(
            car_engine_id=engine_id)]
        air_filters_info = AirFiltersInfoSerializer(AirFilter.objects.filter(id__in=selected_air_filters_id),
                                                    many=True).data
        return Response({'air_filters_info': air_filters_info})


class SelectedCoolants(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        engine_id = post_data.get('engine_id')

        selected_coolants_id = [elem.coolant.id for elem in CarEngineCoolant.objects.filter(
            car_engine_id=engine_id)]
        coolants_info = CoolantsInfoSerializer(Coolant.objects.filter(id__in=selected_coolants_id),
                                               many=True).data
        return Response({'coolants_info': coolants_info})


class SelectedTransmissionOils(APIView):
    @staticmethod
    def post(request):
        post_data = request.data
        transmission_id = post_data.get('transmission_id')

        selected_transmission_oils_id = [elem.transmission_oil.id for elem in
                                         CarTransmissionTransmissionOil.objects.filter(
                                             car_transmission_id=transmission_id)]
        transmission_oils_info = TransmissionOilsInfoSerializer(TransmissionOil.objects.filter(
            id__in=selected_transmission_oils_id), many=True).data
        return Response({'transmission_oils_info': transmission_oils_info})
