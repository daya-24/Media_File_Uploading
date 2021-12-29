from django.shortcuts import render, redirect
from .forms import LaptopModelForm
from .models import Laptop
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




# Create your views here.

class AddLaptopView(View):
    def get(self, request):
        form = LaptopModelForm()

        context = {'form': form}
        templates_name = 'LaptopApp/add_lap.html'
        return render(request, templates_name, context)

    def post(self, request):

        form = LaptopModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_lap')
        context = {'form': form}
        templates_name = 'LaptopApp/add_lap.html'
        return render(request, templates_name, context)



class ShowLaptopView(View):
    def get(self, request):
        show_obj = Laptop.objects.all()
        templates_name = 'LaptopApp/show_lap.html'
        context = {'show_obj': show_obj}
        return render(request, templates_name, context)

class DeleteLaptopView(View):
    def get(self, request, i):
        var1 = Laptop.objects.get(id=i)
        var1.delete()
        return redirect('show_lap')


class UpdateLaptopView(View):
    def get(self, request, i):
        s2 = Laptop.objects.get(id=i)
        form = LaptopModelForm(instance=s2)

        context = {'form': form}
        templates_name = 'LaptopApp/add_lap.html'
        return render(request, templates_name, context)

    def post(self, request, i):
        s2 = Laptop.objects.get(id=i)
        form = LaptopModelForm(request.POST, instance=s2)
        if form.is_valid():
            form.save()
            return redirect('show_lap')

        template_name = 'LaptopApp/add_lap.html'
        context = {'form': form}
        return render(request, template_name, context)

class LaptopInfo(View):
    def get(self, request, i):
        laptop = Laptop.objects.get(id=i)
        template_name = 'LaptopApp/laptop_info.html'
        context = {'laptop': laptop}
        return render(request, template_name, context)