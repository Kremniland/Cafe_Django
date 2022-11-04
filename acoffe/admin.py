from django.contrib import admin

from acoffe.models import coffe


class CoffeAdmin(admin.ModelAdmin):
    list_display = ('name','price','create_date','update_date','exists')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('price','exists')
    list_filter = ('exists',)

admin.site.register(coffe, CoffeAdmin)