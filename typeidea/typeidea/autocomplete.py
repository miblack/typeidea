from dal import autocomplete
from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():    # 没有登录
            return Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user)

        if self.q:  # URl传递过来的参数
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():  # 没有登录
            return Tag.objects.none()

        qs = Tag.objects.filter(owner=self.request.user)

        if self.q:  # URl传递过来的参数
            qs = qs.filter(name__istartswith=self.q)
        return qs
