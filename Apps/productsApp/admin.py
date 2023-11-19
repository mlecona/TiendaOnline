from django.contrib import admin
from Apps.productsApp.models import * 


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

# Register your models here.
admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator)
admin.site.register(Product)
