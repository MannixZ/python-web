from django.shortcuts import render, redirect, HttpResponse

from manage_app.utils.pagination import Pagination
from manage_app.utils.form import *
from manage_app.models import *


def num_list(request):
    data_dict = {}
    # request.GET.get("q", "")，第二个参数为key的值，比如这里是默认将q复制为""，如果不填，将会显示为None
    value = request.GET.get("q", "")
    if value:
        data_dict["mobile__contains"] = value

    queryset = PrettyNum.objects.filter(**data_dict).order_by("-level")
    page_object = Pagination(request, queryset)

    # 1.根据用户想要访问的页码，计算出起止位置
    # page = int(request.GET.get('page', 1))
    # page_size = 2
    # start = page * page_size - page_size
    # end = page * page_size

    # # 2.获取数据库筛选后的总条数
    # total_count = PrettyNum.objects.filter(**data_dict).order_by("-level").count()
    #
    # # 3.总页码
    # total_page_count, div = divmod(total_count, page_size)
    # if div:
    #     total_page_count += 1

    # 5.计算当前页的前x页和后x页，用于页码仅展示前 x 页 和 后 x页
    # plus = 2
    #
    # # 6.当前页面如果已经满足显示所有数据，则页码数量不再需要调整
    # if total_page_count <= 2 * plus + 1:
    #     start_page = 1
    #     end_page = total_page_count
    # else:
    #     if page <= plus:
    #         start_page = 1
    #         end_page = 2 * plus + 1
    #     else:
    #         if (page + plus) > total_page_count:
    #             start_page = total_page_count - 2 * plus
    #             end_page = total_page_count
    #         else:
    #             start_page = page - plus
    #             end_page = page + plus

    # # 4.生成前端页码代码
    # page_str_list = []
    #
    # # 首页
    # prev = f"<li><a href='?page={1}'>首页</a></li>"
    # page_str_list.append(prev)
    #
    # # 上一页
    # if page > 1:
    #     prev = f"<li><a href='?page={page-1}'>上一页</a></li>"
    # else:
    #     prev = f"<li><a href='?page={1}'>上一页</a></li>"
    # page_str_list.append(prev)
    #
    # for i in range(start_page, end_page + 1):
    #     if i == page:
    #         ele = f"<li class='active'><a href='?page={i}'>{i}</a></li>"
    #     else:
    #         ele = f"<li><a href='?page={i}'>{i}</a></li>"
    #     page_str_list.append(ele)
    #
    # # 下一页
    # if page < total_page_count:
    #     prev = f"<li><a href='?page={page+1}'>下一页</a></li>"
    # else:
    #     prev = f"<li><a href='?page={total_page_count}'>下一页</a></li>"
    # page_str_list.append(prev)
    #
    # # 尾页
    # prev = f"<li><a href='?page={total_page_count}'>尾页</a></li>"
    # page_str_list.append(prev)
    #
    # page_string = mark_safe("".join(page_str_list))

    context = {"data_list": page_object.page_queryset, "value": value, "page_string": page_object.html()}

    return render(request, 'num_list.html', context)


def add_num(request):
    if request.method == "GET":
        form = NumModel()
        return render(request, 'add_num.html', {"form": form})
    form = NumModel(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/num/list/')
    return render(request, 'add_num.html', {'form': form})


def edit_num(request, nid):
    raw_obj = PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = NumEditModel(instance=raw_obj)
        return render(request, 'edit_num.html', {"form": form})
    form = NumEditModel(data=request.POST, instance=raw_obj)
    if form.is_valid():
        form.save()
        return redirect('/num/list/')
    return render(request, 'edit_num.html', {"form": form})


def delete_num(request, nid):
    PrettyNum.objects.filter(id=nid).delete()
    return redirect('/num/list/')
