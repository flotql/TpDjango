from django.urls import path
from . import views

app_name = 'vote'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:idIdees>/', views.detail, name='detail'),
    path('<int:idIdees>/results', views.results, name='results'),
    path('<int:idIdees>/vote', views.vote, name='vote'),
]