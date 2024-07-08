from django.shortcuts import render
from .forms import StudentForm, Teacher
from .models import Student
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
  std = Student.objects.all()
  t = Teacher()
  if request.method == "POST":
    form = StudentForm(request.POST)
    t = Teacher(request.POST)
    if form.is_valid():
      form.save()
      # print(f.cleaned_data['name'], f.cleaned_data['email'], f.cleaned_data['roll'])
    else:
      print("Form student not valid")
    if t.is_valid():
      print(t.cleaned_data['name'])
  else: 
    form = StudentForm()
  
  return render(request, "home.html", {'form': form, 'std': std, 'teacher': t})

@csrf_exempt
def save_data(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      name = request.POST['name']
      email = request.POST['email']
      roll = request.POST['roll']
      print(name,email, roll)
      std = Student(name= name, email = email, roll=roll)
      std.save()
      return JsonResponse({'status':"Data saved successfully"})
    else:
      return JsonResponse({'status': "Failed"})
    
   
def newForm(request):
  if request.method == "POST":
    form = StudentForm(request.POST)
    if form.is_valid():
      print("Validated")
  else:
    form = StudentForm()
  return render(request, "frm.html", {'form': form})


def home_value(request, value):
  return HttpResponse(value*value)

def home_value2(request, value, value2):
  return HttpResponse(value2)