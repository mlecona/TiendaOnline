""" Models for Products """

from django.db import models
from simple_history.models import HistoricalRecords
# Models
from Apps.baseApp.models import BaseModel

class MeasureUnit(BaseModel):
    """ Model definition for MeasureUnit """

    # TODO: Define fields here
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """ Meta definition for MeasureUnit """

        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        """ Unicode representation of MeasureUnit """
        return self.description
    
    
class CategoryProduct(BaseModel):
    """ Model definition for CategoryProduct """

    # TODO: Define fields here
    description = models.CharField('Descripción', max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """ Meta definition for CategoryProduct """

        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Producto'

    def __str__(self):
        """ Unicode representation of CategoryProduct """
        return self.description

class Indicator(BaseModel):
    """ Model definition for Indicator """

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """ Meta definition for Indicator """

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        """ Unicode representation of Indicator """
        return f"Oferta de la Categoría {self.category_product} : {self.descount_value}%"

class Product(BaseModel):
    """ Model definition for Product """

    # TODO: Define fields here
    name = models.CharField('Nombre Producto', max_length=150, unique=True, blank=False, null=False)
    description  = models.TextField('Descripción Producto', blank=False, null=False)
    imagen = models.ImageField('Imagen Producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría de Producto', null=True)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """ Meta definition for Product """
        
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """ Unicode representation of Product """
        return self.name
