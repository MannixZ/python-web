"""
自定义分页使用说明：
from manage_app.utils.pagination import Pagination

    1. 按照自己情况去筛选数据
    queryset = PrettyNum.objects.all()

    2.实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
    "data_list": page_object.page_queryset,  # 分完页的数据
    "page_string": page_object.html()        # 页码前端数据
    }

    return render(request, 'num_list.html', context)

前端：
    <nav aria-label="...">
        <ul class="pagination">
            {{ page_string }}
        </ul>
    </nav>

"""

from django.utils.safestring import mark_safe


class Pagination:

    def __init__(self, request, queryset, page_size=2, page_param="page", plus=2):
        # 修复bug：在搜索后再点击分页组件搜索结果会失效问题
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.start = page * page_size - page_size
        self.end = page * page_size

        self.page = page
        self.page_param = page_param
        self.page_size = page_size
        self.page_queryset = queryset[self.start:self.end]

        # 2.获取数据库筛选后的总条数
        total_count = queryset.count()

        # 3.总页码
        total_page_count, div = divmod(total_count, self.page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus



    def html(self):

        # 6.当前页面如果已经满足显示所有数据，则页码数量不再需要调整
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        # 4.生成前端页码代码
        page_str_list = []

        # 首页
        self.query_dict.setlist(self.page_param, [1])
        prev = f"<li><a href='?{self.query_dict.urlencode()}'>首页</a></li>"
        page_str_list.append(prev)

        # 上一页
        self.query_dict.setlist(self.page_param, [self.page-1])
        if self.page > 1:
            prev = f"<li><a href='?{self.query_dict.urlencode()}'>上一页</a></li>"
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = f"<li><a href='?{self.query_dict.urlencode()}'>上一页</a></li>"
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = f"<li class='active'><a href='?{self.query_dict.urlencode()}'>{i}</a></li>"
            else:
                ele = f"<li><a href='?{self.query_dict.urlencode()}'>{i}</a></li>"
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = f"<li><a href='?{self.query_dict.urlencode()}'>下一页</a></li>"
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = f"<li><a href='?{self.query_dict.urlencode()}'>下一页</a></li>"
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        prev = f"<li><a href='?{self.query_dict.urlencode()}'>尾页</a></li>"
        page_str_list.append(prev)

        page_string = mark_safe("".join(page_str_list))
        return page_string