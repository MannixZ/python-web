from django.shortcuts import render, redirect, HttpResponse

from manage_app.utils.pagination import Pagination
from manage_app.utils.form import *
from manage_app.models import *


def user_list(request):
    """用户列表"""
    queryset = UserInfo.objects.all()
    for obj in queryset:
        # datetime 格式转换为字符串，并格式化
        obj.creta_time.strftime("%Y-%m-%d")
        # django 定义的嵌套元祖格式映射值获取
        obj.get_gender_display()
        # 外键字段获取
        obj.depart.title
    page_obj = Pagination(request, queryset)

    context = {"queryset": page_obj.page_queryset, "page_string": page_obj.html()}

    return render(request, 'user_list.html', context)


def add_user(request):
    """用户添加"""
    if request.method == "GET":
        form = UserModel()
        return render(request, 'add_user.html', {"form": form})
    form = UserModel(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'add_user.html', {"form": form})
    # return redirect('/user/list/')


def edit_user(request, nid):
    """用户编辑"""
    row_obj = UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModel(instance=row_obj)
        return render(request, 'edit_user.html', {"form": form})
    form = UserModel(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'edit_user.html', {"form": form})


def delete_user(request):
    nid = request.GET.get("id")
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
