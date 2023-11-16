""" Models for BaseModel """

from django.db import models

class BaseModel(models.Model):
    """ Model definition for BaseModel """
    
    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    create_date = models.DateField('Fecha Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha Eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        """ Meta definition BaseModel """
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
