from django.shortcuts import HttpResponse, redirect, render

from manage_app import models
from manage_app.utils.bootstrap import BootStrapModelForm


def city_list(request):
    if request.method == "GET":
        data_list = models.City.objects.all()
        return render(request, 'city_list.html', {"data_list": data_list})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"


def add_city(request):
    title = "ModelForm 文件上传"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_model_form.html', {"form": form, "title": title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/city/list/')
    return render(request, 'upload_model_form.html', {"form": form, "title": title})
