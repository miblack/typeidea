from django.views.generic import ListView

from .models import Link
from blog.views import CommonViewMixin


class LinkView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
