from django.shortcuts import redirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    """中间件"""

    def process_request(self, request):
        # 获取当前用户访问的url
        if request.path_info in ["/login/", "/image/code/"]:
            return
        # 方法中没有返回值（返回None）,继续往后走
        # 如果有返回值，则从当前中间件返回，不会继续执行到视图函数
        info = request.session.get("info")
        if info:
            return
        return redirect('/login/')

    def process_response(self, request, response):
        return response
