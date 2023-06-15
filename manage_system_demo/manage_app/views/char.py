import random
from django.shortcuts import render
from django.http import JsonResponse


def char_list(request):
    return render(request, 'char_list.html')


def char_bar(request):
    legend = ['销量1']
    data_list = [
        {
            "name": '销量1',
            "type": 'bar',
            "data": [51, 201, 361, 101, 101, 201]
        }
    ]
    type_list = ['衬衫1', '羊毛衫1', '雪纺衫1', '裤子1', '高跟鞋1', '袜子1']
    result = {
        "status": True,
        "data": {
            "legend": legend,
            "data_list": data_list,
            "type_list": type_list
        }
    }
    return JsonResponse(result)


def char_pie(request):
    data_list = [
        {"value": 104, "name": 'Search Engine'},
        {"value": 73, "name": 'Direct'},
        {"value": 58, "name": 'Email'},
        {"value": 48, "name": 'Union Ads'},
        {"value": 30, "name": 'Video Ads'}
    ]

    result = {
        "status": True,
        "data": {
            "data_list": data_list
        }
    }
    return JsonResponse(result)


def char_line(request):
    line_dict = {}
    data_list = ['Mon1', 'Tue2', 'Wed3', 'Thu4', 'Fri5', 'Sat6', 'Sun7']
    for i in range(5):
        line_dict[f"line{str(i + 1)}_data"] = [random.randint(1, 100) for i in range(7)]
    print(line_dict)

    result = {
        "status": True,
        "data": {
            "data_list": data_list,
            "line1_data": line_dict["line1_data"],
            "line2_data": line_dict["line2_data"],
            "line3_data": line_dict["line3_data"],
            "line4_data": line_dict["line4_data"],
            "line5_data": line_dict["line5_data"]
        }
    }
    return JsonResponse(result)
