from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from manage_app.models import Department, UserInfo, PrettyNum, Admin, Task, Order
from manage_app.utils.bootstrap import BootStrapModelForm, BootStrapForm
from manage_app.utils.encrypt import md5
from manage_app import models


class UserModel(BootStrapModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age', 'account', 'creta_time', 'gender', 'depart']

        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control"}, ),
            "creta_time": forms.DateTimeInput(attrs={"autocomplete": "off"}, )
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         pass
    #         if name == "creta_time":
    #             field.widget.attrs["autocomplete"] = "off"
    #         # field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    #         field.widget.attrs["class"] = "form-control"
    #         field.widget.attrs["placeholder"] = field.label


class NumModel(forms.ModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
    )

    class Meta:
        model = PrettyNum
        fields = ["mobile", "price", "level", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 校验数据库中是否有已存在的手机号
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']

        exists = PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile


class NumEditModel(forms.ModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
    )

    class Meta:
        model = PrettyNum
        fields = ["mobile", "price", "level", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 校验数据库中是否有已存在的手机号
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        # 编辑需要排除自身后再进行过滤手机号是否存在
        exists = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile


class AdminModel(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        print(self.cleaned_data)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm


class AdminEditModel(BootStrapModelForm):
    class Meta:
        model = Admin
        fields = ['username']
        widgets = {
        }


class AdminResetModel(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        pwd_md5 = md5(pwd)

        # 校验新密码是否和当前密码是否一致
        if models.Admin.objects.filter(id=self.instance.pk, password=pwd_md5).exists():
            raise ValidationError("新密码与旧密码一致")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        print(self.cleaned_data)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(
            render_value=True
        )
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput
    )

    def clean_password(self):
        pwd = md5(self.cleaned_data.get("password"))
        return pwd


class TaskModelForm(BootStrapModelForm):

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput,
        }


class OrderModelForm(BootStrapModelForm):

    class Meta:
        model = Order
        exclude = ['oid', 'user']
