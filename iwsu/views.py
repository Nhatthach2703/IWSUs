# from django.http import HttpResponse

from django.shortcuts import render, redirect
import urllib.request, urllib.parse, urllib.error
import json
import ssl
from diadiem.models import DiaDiem
def home(request):
    danh_sach_dia_diem = DiaDiem.objects.all()


    context = {
        'danh_sach_dia_diem': danh_sach_dia_diem
    }
    return render(request, 'home.html', context)

def detail(request):
    return render(request, 'detail.html')
    # return HttpResponse('Homepages')