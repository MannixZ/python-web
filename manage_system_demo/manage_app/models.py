from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2,
                                  default=0)  # max_digits 数字长度， decimal_places 小数位数
    creta_time = models.DateField(verbose_name="入职时间")
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    def __str__(self):
        return self.name


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(max_length=32, verbose_name="手机号")
    # 想要允许为空 null=True, blank=True
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价值", default=0)
    level_choices = (
        (1, 'Lv1'),
        (2, 'Lv2'),
        (3, 'Lv3'),
        (4, 'Lv4')
    )
    level = models.SmallIntegerField(verbose_name="等级", choices=level_choices, default=1)
    status_choices = (
        (1, "占用"),
        (2, "未占用")
    )
    status = models.SmallIntegerField(verbose_name="占用状态", choices=status_choices, default=2)


class Admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)


class Task(models.Model):
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时")
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="任务详请", max_length=64)
    user = models.ForeignKey(verbose_name="负责人", to=UserInfo, to_field="id", on_delete=models.CASCADE)


class Order(models.Model):
    """订单"""
    oid = models.CharField(verbose_name="订单号", max_length=64, null=False, blank=False)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    status_choices = (
        (1, "已售"),
        (2, "未售")
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    user = models.ForeignKey(verbose_name="负责人", to=UserInfo, to_field="id", on_delete=models.CASCADE)


class Boss(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    img = models.CharField(verbose_name="图片", max_length=64)


class City(models.Model):
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")

    # FileField 本质上也是 CharField，使用 FileField 的好处是能自动保存到 upload_to 指定的文件夹，例如这里是 city/ ,实际保存到的路径是 media/city 文件夹下
    img = models.FileField(verbose_name="oLog", max_length=64, upload_to='city/')