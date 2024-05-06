from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def template_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        TRO = Register(name = name, pno = pno, email = email, add = add, gender = gender, course = course, username = un, password = pw)
        TRO.save()
        return HttpResponse('Done')
    return render(request, 'template_register.html')

def ModelRegister(request):
    EMRFO= ModelRegisterForm()
    d = {'EMRFO' :EMRFO}
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        un = request.POST.get('username')
        pw = request.POST.get('password')
        TRO = Register(name = name, pno = pno, email = email, add = add, gender = gender, course = course, username = un, password = pw)
        TRO.save()
        return HttpResponse('Done')
    return render(request, 'ModelRegisterForm.html', d)


