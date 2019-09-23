from django.urls import re_path  # re_path добавил сам
from mediaportalapp.views import ArticleListView

urlpatterns = [
    re_path(r'^$', ArticleListView.as_view()),
]