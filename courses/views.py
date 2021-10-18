from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView
from courses.forms import NewCourseForm
from courses.models import Course


def hello(request):
    return HttpResponse('Witaj w swiecie kursow SDA!')

class CourseCreateView(CreateView):
    template_name = 'course_new.html'
    form_class = NewCourseForm
    success_url = reverse_lazy('index')

class CourseView(ListView):
    template_name = 'courses_list.html'
    model = Course
