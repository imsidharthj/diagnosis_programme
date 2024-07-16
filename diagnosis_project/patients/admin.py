from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'weight', 'allergy']

admin.site.register(Patient, PatientAdmin)
