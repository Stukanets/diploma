from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group, User
from .models import CompanyInfo, CarBrand, CarModel, CarEngine, CarTransmission, CabinFilter, BrakePad, BrakeFluid, \
    EngineOil, OilFilter, FuelFilter, AirFilter, Coolant, TransmissionOil, CarModelCabinFilter, CarModelBrakePad, \
    CarModelBrakeFluid, CarEngineEngineOil, CarEngineOilFilter, CarEngineFuelFilter, CarEngineAirFilter, \
    CarEngineCoolant, CarTransmissionTransmissionOil

admin.site.unregister(Group)


class UserAdmin(auth_admin.UserAdmin):
    model = User

    change_password_form = auth_admin.AdminPasswordChangeForm

    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']
    readonly_fields = ('last_login', 'date_joined',)
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    ordering = ['-is_staff']

    fieldsets = (('Personal info', {'fields': ('username', 'password', 'email')}),
                 ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
                 ('Important dates', {'fields': ('date_joined', 'last_login')}))


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(CompanyInfo)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(CarEngine)
admin.site.register(CarTransmission)
admin.site.register(CabinFilter)
admin.site.register(BrakePad)
admin.site.register(BrakeFluid)
admin.site.register(EngineOil)
admin.site.register(OilFilter)
admin.site.register(FuelFilter)
admin.site.register(AirFilter)
admin.site.register(Coolant)
admin.site.register(TransmissionOil)
admin.site.register(CarModelCabinFilter)
admin.site.register(CarModelBrakePad)
admin.site.register(CarModelBrakeFluid)
admin.site.register(CarEngineEngineOil)
admin.site.register(CarEngineOilFilter)
admin.site.register(CarEngineFuelFilter)
admin.site.register(CarEngineAirFilter)
admin.site.register(CarEngineCoolant)
admin.site.register(CarTransmissionTransmissionOil)
