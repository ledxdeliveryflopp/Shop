from django.contrib import admin

from .models import Company, Category


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryCompanyAdmin(admin.ModelAdmin):
    pass