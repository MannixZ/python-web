"""manage_system_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from manage_app.views import depart, user, num, admin, account, task, order, char, upload, city

urlpatterns = [
    # path("admin/", admin.site.urls),
    # media 存放路径
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 部门管理
    path('depart/list/', depart.depart_list),
    path('add/depart/', depart.add_depart),
    path('delete/depart/', depart.delete_depart),
    path('edit/<int:nid>/depart/', depart.edit_depart),
    path('depart/multi/', depart.depart_multi),

    # 用户管理
    path('user/list/', user.user_list),
    path('add/user/', user.add_user),
    path('delete/user/', user.delete_user),
    path('edit/<int:nid>/user/', user.edit_user),

    # 靓号管理
    path('num/list/', num.num_list),
    path('add/num/', num.add_num),
    path('delete/<int:nid>/num/', num.delete_num),
    path('edit/<int:nid>/num/', num.edit_num),

    # 管理员
    path('admin/list/', admin.admin_list),
    path('add/admin/', admin.admin_add),
    path('delete/<int:nid>/admin/', admin.delete_admin),
    path('edit/<int:nid>/admin/', admin.edit_admin),
    path('reset/<int:nid>/admin/', admin.reset_admin),

    # 登录
    path('login/', account.account_login),
    path('logout/', account.account_logout),
    path('image/code/', account.image_code),

    # 用户管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('add/task/', task.add_task),

    # 订单管理
    path('order/list/', order.order_list),
    path('add/order/', order.add_order),
    path('delete/order/', order.delete_order),
    path('detail/order/', order.detail_order),
    path('edit/order/', order.edit_order),

    # 数据统计
    path('chars/list/', char.char_list),
    path('chars/bar/', char.char_bar),
    path('chars/pie/', char.char_pie),
    path('chars/line/', char.char_line),

    # 文件上传
    path('upload/file/', upload.upload_file),
    path('upload/form/', upload.upload_form),
    path('upload/modelform/', upload.upload_model_form),

    # 城市列表
    path('city/list/', city.city_list),
    path('add/city/', city.add_city),
]
