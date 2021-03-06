from __future__ import unicode_literals
from django.shortcuts import render
from  django.views.generic.list import  ListView
from mediaportalapp.models import Article

# Create your views here.

class ArticleListView(ListView):

    model = Article
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['articles'] = self.model.objects.all()
        context['custom_articles'] = self.model.custom_manager.all()
        return context
