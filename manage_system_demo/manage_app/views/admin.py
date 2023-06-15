from django.shortcuts import render, redirect, HttpResponse
from manage_app import models

from manage_app.utils.pagination import Pagination
from manage_app.utils.form import AdminModel, AdminEditModel, AdminResetModel


def admin_list(request):
    """管理员列表"""
    info = request.session.get("info")
    if not info:
        return redirect("/account/login")

    data_dict = {}
    value = request.GET.get("q", "")
    if value:
        data_dict["username__contains"] = value
    queryset = models.Admin.objects.all(**data_dict)
    page_obj = Pagination(request, queryset, page_size=10)
    context = {
        "queryset": page_obj.page_queryset,
        "page_string": page_obj.html(),
        "value": value
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    title = "添加管理员"
    if request.method == "GET":
        form = AdminModel()
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminModel(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"form": form, "title": title})


def edit_admin(request, nid):
    raw_obj = models.Admin.objects.filter(id=nid).first()
    if not raw_obj:
        msg = "用户不存在"
        return render(request, 'error.html', {'msg': msg})

    title = "编辑管理员"
    if request.method == "GET":
        form = AdminEditModel(instance=raw_obj)
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminEditModel(request.POST, instance=raw_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"form": form, "title": title})


def delete_admin(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


def reset_admin(request, nid):
    title = "重置密码"
    obj = models.Admin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = AdminResetModel(instance=obj)
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminResetModel(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"form": form, "title": title})
