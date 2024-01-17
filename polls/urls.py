from django.urls import path

from . import views
<<<<<<< HEAD
import datetime 
=======
>>>>>>> e155754313e6cee09eeb673833dff3d3ef6f47f0
from .views import contestView


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('contest/', contestView, name='contest'),

]