# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'tongxinkaoshiwang'

urlpatterns = [
    path('', views.essay_question_list, name='essay_question_list'),
    path('search/', views.search, name='search'),
    path('<tag>', views.tag, name='tags'),
]