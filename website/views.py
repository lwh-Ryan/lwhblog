from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from article.models import Blog
from website.mixin import FrontMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy


class HomepageView(FrontMixin, ListView):
    template_name = 'website/frontend/homepage.html'
    model = Blog
    paginate_by = 5
    context_object_name = 'article_list'


class DashboardOverviewView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('user-login')
    template_name = 'website/backend/overview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardOverviewView, self).get_context_data(**kwargs)
        context['active_page'] = 'overview'
        return context


class AboutMeView(FrontMixin, TemplateView):
    template_name = 'website/frontend/about.html'


class GuestBookView(FrontMixin, TemplateView):
    template_name = 'website/frontend/guest_book.html'
