from django.contrib import admin

from acoffe.models import coffe, ingridient

class IngridientInline(admin.TabularInline):
    model = ingridient.coffe.through


class CoffeAdmin(admin.ModelAdmin):
    list_display = ('name', 'volume', 'price','create_date','update_date','exists', 'ingridients')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('price','exists')
    list_filter = ('exists',)
    inlines = [IngridientInline,]
    

class IngridientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'exists')
   
admin.site.register(coffe, CoffeAdmin)
admin.site.register(ingridient, IngridientAdmin)