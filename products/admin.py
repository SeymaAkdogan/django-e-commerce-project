from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','is_active','selected_categories',)
    list_editable = ('is_active',)
    search_fields = ('name','description')
    list_filter = ('is_active','categories',)

    def selected_categories(self,obj):
        html = "<ul>"
        for category in obj.categories.all():
            html += "<li>"+category.name + "</li>"
        
        html += "</ul>"
        return mark_safe(html)

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
