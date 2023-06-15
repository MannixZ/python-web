import os.path

from django import forms
from django.shortcuts import render, HttpResponse

from manage_app import models
from manage_app.utils.bootstrap import BootStrapForm, BootStrapModelForm


def upload_file(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    # 获取 post 数据
    print(request.POST)
    # 获取前端 name = avatar 的文件上传对象
    file_obj = request.FILES.get("avatar")
    # 获取上传文件的名称
    file_name = file_obj.name
    print(file_name)
    # 将上传的文件保存到文件下，图片需要用二进制格式写入 wb
    with open('/Users/mannix/Data/Study/python-web/manage_system_demo/manage_app/static/img/' + file_name, 'wb') as f:
        # 写文件
        for chunk in file_obj.chunks():
            f.write(chunk)
    return HttpResponse("...")


class UploadForm(BootStrapForm):
    # 过滤 img 不显示 bootstrap 样式
    bootstrap_exclude_fields = ['img']

    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


def upload_form(request):
    title = "Form 上传文件"
    if request.method == "GET":
        form = UploadForm()
        context = {
            'title': title,
            'form': form
        }
        return render(request, 'upload.html', context=context)
    form = UploadForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 1.读取图片内容，写入到文件夹中并获取路文件路径
        image_obj = form.cleaned_data.get('img')

        from django.conf import settings

        # 路径拼接
        # db_file_path = os.path.join('static', 'img', image_obj.name)
        # 保存文件路径
        # file_path = os.path.join('manage_app', db_file_path)

        # 文件存放在 media 目录下
        media_path = os.path.join("media", image_obj.name)
        print(media_path)

        with open(media_path, 'wb') as f:
            for chunk in image_obj.chunks():
                f.write(chunk)

        # 2.将图片文件路径写入到数据库
        models.Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data.get('age'),
            img=media_path
        )
        return HttpResponse("...")
    return render(request, 'upload.html', {"title": title, "form": form})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"


def upload_model_form(request):
    title = "ModelForm 文件上传"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_model_form.html', {"form": form, "title": title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("上传成功")
    return render(request, 'upload_model_form.html', {"form": form, "title": title})
