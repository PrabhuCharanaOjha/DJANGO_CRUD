import imp
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from .forms import Studentdata
from .models import Student

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = Studentdata(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Sir Student Details Add Successfully...")
    data = Student.objects.all()
    form = Studentdata()
    dt = {'form': form, 'data': data}
    return render(request, 'home.html', dt)


class updatestudent(UpdateView):
    model = Student
    form_class = Studentdata
    success_url = '/'
    template_name = "home.html"


class deletestudent(DeleteView):
    model = Student
    template_name = 'delete.html'
    success_url = '/'
