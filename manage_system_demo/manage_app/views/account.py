from django.shortcuts import render, HttpResponse, redirect

from manage_app import models
from manage_app.utils.form import LoginForm
from manage_app.utils.code import check_code


def account_login(request):
    """用户登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        admin_obj = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_obj:
            # 在指定输入框位置底部显示错误信息
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})
        if user_input_code.upper() != str.upper(request.session.get("image_code", "")):
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {"form": form})
        # 生成cookie，并写入到session中
        request.session['info'] = {"id": admin_obj.id, "username": admin_obj.username}
        request.session.set_expiry(60*60*24*7)
        request.session.pop('image_code')
        return redirect('/admin/list/')
    return render(request, 'login.html', {"form": form})


def account_logout(request):
    request.session.clear()
    return redirect('/login/')


from io import BytesIO
def image_code(request):
    img, code_str = check_code()
    stream = BytesIO()
    img.save(stream, 'png')
    request.session['image_code'] = code_str
    request.session.set_expiry(60)
    return HttpResponse(stream.getvalue())