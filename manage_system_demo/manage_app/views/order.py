import random
from datetime import datetime

from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from manage_app.utils.form import OrderModelForm
from manage_app.utils.pagination import Pagination
from manage_app import models


def order_list(request):
    queryset = models.Order.objects.all().order_by("-id")
    page_object = Pagination(request, queryset, page_size=100)
    form = OrderModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码前端数据
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def add_order(request):
    oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = oid
        form.instance.user_id = request.session["info"]["id"]
        print("user_id", form.instance.user_id)
        form.save()
        data_dict = {"status": True, "msg": "success"}
        return JsonResponse(data_dict)
    data_dict = {"status": False, "error": form.errors}
    return JsonResponse(data_dict)


@csrf_exempt
def delete_order(request):
    uid = request.POST.get('uid')
    if models.Order.objects.filter(id=uid).exists():
        models.Order.objects.filter(id=uid).delete()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "msg": "订单不存在,删除失败"})


@csrf_exempt
def detail_order(request):
    uid = request.GET.get("uid")
    row_obj = models.Order.objects.filter(id=uid).values('title', 'price', 'status').first()
    if not row_obj:
        return JsonResponse({"status": False, "error": "订单不存在"})
    result = {
        "status": True,
        "data": row_obj
    }
    return JsonResponse(result)


@csrf_exempt
def edit_order(request):
    uid = request.GET.get('uid')
    row_obj = models.Order.objects.filter(id=uid).first()
    if not row_obj:
        return JsonResponse({"status": False, "tips": "订单不存在"})
    form = OrderModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

