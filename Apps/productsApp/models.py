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
    
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
