from django.urls import path
from polls import views

# 一个工程可能有多个项目，比如这里的 polls。app_name 的作用就是在有多个项目的时候来区分  {% url %} 代表的是哪一个项目
app_name = 'polls'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
]