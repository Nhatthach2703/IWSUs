from django.contrib import admin

from diadiem.models import DiaDiem
from .models import DiaDiem

# Register your models here.
class DiaDiemAdmin(admin.ModelAdmin):
    list_display = ('ten_dia_diem', 'thanh_pho')

admin.site.register(DiaDiem, DiaDiemAdmin)