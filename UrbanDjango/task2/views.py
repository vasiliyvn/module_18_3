from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def func_f(request):
    return render(request,'func_template.html')

class clas_s(TemplateView):
    template_name = 'class_template.html'