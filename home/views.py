from django.shortcuts import render
from django.http import HttpResponse

from .forms import Bookingform
from .models import Departments,Doctors
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = Bookingform(request.POST)
        if form.is_valid():
            booking = form.save()
            return render(request, 'confirmation.html',{'booking': booking})
    form = Bookingform()
    return render(request,'booking.html',{'form':form})

def doctors(request):
    doctors = Doctors.objects.all()
    return render(request,'doctors.html',{'doctors':doctors})

def contact(request):
    return render(request,'contact.html')

def department(request):
    departments = Departments.objects.all()
    return render(request,'department.html',{'departments': departments})