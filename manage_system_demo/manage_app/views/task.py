import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from manage_app import models
from manage_app.utils.form import TaskModelForm
from manage_app.utils.pagination import Pagination


def task_list(request):
    queryset = models.Task.objects.all().order_by("-id")
    form = TaskModelForm()
    page_object = Pagination(request, queryset)
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码前端数据
    }
    return render(request, 'task_list.html', context)

@csrf_exempt
def task_ajax(request):
    content = {
        "msg": "success"
    }
    print(request.POST)
    return JsonResponse(content)
    # json_string = json.dumps(content)
    # return HttpResponse(json_string)

@csrf_exempt
def add_task(request):
    content = {
        "status": True,
        "data": request.POST
    }
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse(content)
    print(form.errors.as_json())
    data_dict = {"status": False, "error": form.errors}
    return JsonResponse(data_dict)
    # return HttpResponse(json.dumps(data_dict, ensure_ascii=False))