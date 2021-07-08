from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
test_create = apps.get_model('teacher', 'test_create')
from .models import student_info


def give_code(request):
    return render(request, 'give_code.html')


def search_bar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        s = test_create.objects.all().filter(test_code__username=search)
        print(s)
    return render(request,'search_bar.html', {'s':s})

def final(request):
    if request.method == "GET":
      marks = request.GET.get('marks', False)
      roll_no = request.GET.get('roll_no', False)
      print("count status ", marks ,  roll_no)
      contact = student_info(roll_no=roll_no,marks=marks)
      contact.save()

    return HttpResponse("DONE")
