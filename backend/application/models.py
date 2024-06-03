from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=50)
    company_owner = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    company_phone_number = PhoneNumberField(null=False, blank=False, unique=False)
    company_first_address = models.CharField(max_length=100)
    company_second_address = models.CharField(max_length=100)
    company_address_google_map = models.TextField()

    class Meta:
        db_table = 'company_info'
        ordering = ['company_name']
        managed = True
        verbose_name = 'Company information'
        verbose_name_plural = 'Company information'

    def __str__(self):
        return f'{str(self.company_name)}'


class CarBrand(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='car_brands_info')
    brand_name = models.CharField(max_length=50)
    brand_location = models.CharField(max_length=50)
    brand_year_of_establishment = models.DateField()
    brand_description = models.TextField()
    brand_logo_image = models.ImageField(null=True, blank=True, upload_to='images/')
    brand_website_link = models.TextField()

    class Meta:
        db_table = 'car_brands'
        ordering = ['brand_name']
        managed = True
        verbose_name = 'Car brands'
        verbose_name_plural = 'Car brands'

    def __str__(self):
        return f'{str(self.brand_name)}'


class CarModel(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='car_models_info')
    model_name = models.CharField(max_length=50)
    model_years_of_production = models.CharField(max_length=20)
    model_body_type = models.CharField(max_length=50)
    model_wheel_drive_type = models.CharField(max_length=50)
    model_description = models.TextField()
    model_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'car_models'
        ordering = ['model_name']
        managed = True
        verbose_name = 'Car models'
        verbose_name_plural = 'Car models'

    def __str__(self):
        return f'{str(self.model_name)}'


class CarEngine(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='car_engines_info')
    engine_name = models.CharField(max_length=50)
    engine_capacity = models.DecimalField(max_digits=2, decimal_places=1)
    engine_hp = models.IntegerField()
    engine_number_of_cylinders = models.IntegerField()
    engine_number_of_valves = models.IntegerField()
    engine_fuel_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'car_engines'
        ordering = ['engine_name']
        managed = True
        verbose_name = 'Car engines'
        verbose_name_plural = 'Car engines'

    def __str__(self):
        return f'{str(self.engine_name)}'


class CarTransmission(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='car_transmissions_info')
    transmission_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'car_transmissions'
        ordering = ['transmission_type']
        managed = True
        verbose_name = 'Car transmissions'
        verbose_name_plural = 'Car transmissions'

    def __str__(self):
        return f'{str(self.transmission_type)}'


class CabinFilter(models.Model):
    cabin_filter_name = models.CharField(max_length=50)
    cabin_filter_type = models.CharField(max_length=50)
    cabin_filter_brand = models.CharField(max_length=50)
    cabin_filter_description = models.TextField()
    cabin_filter_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'cabin_filters'
        ordering = ['cabin_filter_name']
        managed = True
        verbose_name = 'Cabin filters'
        verbose_name_plural = 'Cabin filters'

    def __str__(self):
        return f'{str(self.cabin_filter_name)}'


class BrakePad(models.Model):
    brake_pad_name = models.CharField(max_length=50)
    brake_pad_type = models.CharField(max_length=50)
    brake_pad_brand = models.CharField(max_length=50)
    brake_pad_description = models.TextField()
    brake_pad_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'brake_pads'
        ordering = ['brake_pad_name']
        managed = True
        verbose_name = 'Brake pads'
        verbose_name_plural = 'Brake pads'

    def __str__(self):
        return f'{str(self.brake_pad_name)}'


class BrakeFluid(models.Model):
    brake_fluid_name = models.CharField(max_length=50)
    brake_fluid_type = models.CharField(max_length=50)
    brake_fluid_brand = models.CharField(max_length=50)
    brake_fluid_description = models.TextField()
    brake_fluid_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'brake_fluids'
        ordering = ['brake_fluid_name']
        managed = True
        verbose_name = 'Brake fluids'
        verbose_name_plural = 'Brake fluids'

    def __str__(self):
        return f'{str(self.brake_fluid_name)}'


class EngineOil(models.Model):
    engine_oil_name = models.CharField(max_length=50)
    engine_oil_type = models.CharField(max_length=50)
    engine_oil_density = models.CharField(max_length=50)
    engine_oil_tolerances = models.CharField(max_length=50)
    engine_oil_brand = models.CharField(max_length=50)
    engine_oil_description = models.TextField()
    engine_oil_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'engine_oils'
        ordering = ['engine_oil_name']
        managed = True
        verbose_name = 'Engine oils'
        verbose_name_plural = 'Engine oils'

    def __str__(self):
        return f'{str(self.engine_oil_name)}'


class OilFilter(models.Model):
    oil_filter_name = models.CharField(max_length=50)
    oil_filter_brand = models.CharField(max_length=50)
    oil_filter_description = models.TextField()
    oil_filter_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'oil_filters'
        ordering = ['oil_filter_name']
        managed = True
        verbose_name = 'Oil filters'
        verbose_name_plural = 'Oil filters'

    def __str__(self):
        return f'{str(self.oil_filter_name)}'


class FuelFilter(models.Model):
    fuel_filter_name = models.CharField(max_length=50)
    fuel_filter_type = models.CharField(max_length=50)
    fuel_filter_brand = models.CharField(max_length=50)
    fuel_filter_description = models.TextField()
    fuel_filter_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'fuel_filters'
        ordering = ['fuel_filter_name']
        managed = True
        verbose_name = 'Fuel filters'
        verbose_name_plural = 'Fuel filters'

    def __str__(self):
        return f'{str(self.fuel_filter_name)}'


class AirFilter(models.Model):
    air_filter_name = models.CharField(max_length=50)
    air_filter_type = models.CharField(max_length=50)
    air_filter_brand = models.CharField(max_length=50)
    air_filter_description = models.TextField()
    air_filter_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'air_filters'
        ordering = ['air_filter_name']
        managed = True
        verbose_name = 'Air filters'
        verbose_name_plural = 'Air filters'

    def __str__(self):
        return f'{str(self.air_filter_name)}'


class Coolant(models.Model):
    coolant_name = models.CharField(max_length=50)
    coolant_type = models.CharField(max_length=50)
    coolant_color = models.CharField(max_length=50)
    coolant_brand = models.CharField(max_length=50)
    coolant_description = models.TextField()
    coolant_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'coolants'
        ordering = ['coolant_name']
        managed = True
        verbose_name = 'Coolants'
        verbose_name_plural = 'Coolants'

    def __str__(self):
        return f'{str(self.coolant_name)}'


class TransmissionOil(models.Model):
    transmission_oil_name = models.CharField(max_length=50)
    transmission_oil_type = models.CharField(max_length=50)
    transmission_oil_atf_type = models.CharField(max_length=50)
    transmission_oil_brand = models.CharField(max_length=50)
    transmission_oil_description = models.TextField()
    transmission_oil_image = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'transmission_oils'
        ordering = ['transmission_oil_name']
        managed = True
        verbose_name = 'Transmission oils'
        verbose_name_plural = 'Transmission oils'

    def __str__(self):
        return f'{str(self.transmission_oil_name)}'


class CarModelCabinFilter(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    cabin_filter = models.ForeignKey(CabinFilter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_model_cabin_filters'
        ordering = ['car_model']
        managed = True
        verbose_name = 'Car model - cabin filters'
        verbose_name_plural = 'Car model - cabin filters'

    def __str__(self):
        return f'{str(self.car_model)} - {str(self.cabin_filter)}'


class CarModelBrakePad(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    brake_pad = models.ForeignKey(BrakePad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_model_brake_pads'
        ordering = ['car_model']
        managed = True
        verbose_name = 'Car model - brake pads'
        verbose_name_plural = 'Car model - brake pads'

    def __str__(self):
        return f'{str(self.car_model)} - {str(self.brake_pad)}'


class CarModelBrakeFluid(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    brake_fluid = models.ForeignKey(BrakeFluid, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_model_brake_fluids'
        ordering = ['car_model']
        managed = True
        verbose_name = 'Car model - brake fluids'
        verbose_name_plural = 'Car model - brake fluids'

    def __str__(self):
        return f'{str(self.car_model)} - {str(self.brake_fluid)}'


class CarEngineEngineOil(models.Model):
    car_engine = models.ForeignKey(CarEngine, on_delete=models.CASCADE)
    engine_oil = models.ForeignKey(EngineOil, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_engine_engine_oils'
        ordering = ['car_engine']
        managed = True
        verbose_name = 'Car engine - engine oils'
        verbose_name_plural = 'Car engine - engine oils'

    def __str__(self):
        return f'{str(self.car_engine)} - {str(self.engine_oil)}'


class CarEngineOilFilter(models.Model):
    car_engine = models.ForeignKey(CarEngine, on_delete=models.CASCADE)
    oil_filter = models.ForeignKey(OilFilter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_engine_oil_filters'
        ordering = ['car_engine']
        managed = True
        verbose_name = 'Car engine - oil filters'
        verbose_name_plural = 'Car engine - oil filters'

    def __str__(self):
        return f'{str(self.car_engine)} - {str(self.oil_filter)}'


class CarEngineFuelFilter(models.Model):
    car_engine = models.ForeignKey(CarEngine, on_delete=models.CASCADE)
    fuel_filter = models.ForeignKey(FuelFilter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_engine_fuel_filters'
        ordering = ['car_engine']
        managed = True
        verbose_name = 'Car engine - fuel filters'
        verbose_name_plural = 'Car engine - fuel filters'

    def __str__(self):
        return f'{str(self.car_engine)} - {str(self.fuel_filter)}'


class CarEngineAirFilter(models.Model):
    car_engine = models.ForeignKey(CarEngine, on_delete=models.CASCADE)
    air_filter = models.ForeignKey(AirFilter, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_engine_air_filters'
        ordering = ['car_engine']
        managed = True
        verbose_name = 'Car engine - air filters'
        verbose_name_plural = 'Car engine - air filters'

    def __str__(self):
        return f'{str(self.car_engine)} - {str(self.air_filter)}'


class CarEngineCoolant(models.Model):
    car_engine = models.ForeignKey(CarEngine, on_delete=models.CASCADE)
    coolant = models.ForeignKey(Coolant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_engine_coolants'
        ordering = ['car_engine']
        managed = True
        verbose_name = 'Car engine - coolants'
        verbose_name_plural = 'Car engine - coolants'

    def __str__(self):
        return f'{str(self.car_engine)} - {str(self.coolant)}'


class CarTransmissionTransmissionOil(models.Model):
    car_transmission = models.ForeignKey(CarTransmission, on_delete=models.CASCADE)
    transmission_oil = models.ForeignKey(TransmissionOil, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_transmission_transmission_oils'
        ordering = ['car_transmission']
        managed = True
        verbose_name = 'Car transmission - transmission oils'
        verbose_name_plural = 'Car transmission - transmission oils'

    def __str__(self):
        return f'{str(self.car_transmission)} - {str(self.transmission_oil)}'
