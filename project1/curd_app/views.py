from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student


class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'div']


class StudentList(ListView):
    model = Student


class StudentDetail(DetailView):
    model = Student


class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'div']
    success_url = "/"
    template_name = "curd_app/student_form.html"


class StudentDelete(DeleteView):
    model = Student
    success_url = "/"
    template_name = "curd_app/Student_confirm.html"
