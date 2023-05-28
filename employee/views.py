from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee

# Create your views here.

# Index page
def index(request):
    myEmployee = Employee.objects.all().values()
    context = {
        "myEmployee": myEmployee,
    }
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

# Create page for employee
def create(request):
    template = loader.get_template('createPage.html')
    return HttpResponse(template.render({}, request))

# Fetch create page data
def createData(request):
    empName = request.POST["name"]
    empTitle = request.POST["title"]
    newEmp = Employee(name=empName, title=empTitle)
    newEmp.save()

    return HttpResponseRedirect(reverse('index'))

# Update employee page
def update(request, empID):
    emp = Employee.objects.get(id=empID)
    context = {
        "emp": emp,
    }
    template = loader.get_template('updatePage.html')
    return HttpResponse(template.render(context, request))

# Fetch update employee page data
def updateData(request, empID):
    emp = Employee.objects.get(id=empID)
    empName = request.POST["name"]
    empTitle = request.POST["title"]
    emp.name = empName
    emp.title = empTitle
    emp.save()
    
    return HttpResponseRedirect(reverse("index")) 

# Delete employee
def delete(request, empID):
    emp = Employee.objects.get(id=empID)
    emp.delete()
    return HttpResponseRedirect(reverse('index'))
