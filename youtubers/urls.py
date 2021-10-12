from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtubers, name="youtubers"),
    path('<int:id>', views.youtubers_detail, name="youtubers_detail"),
    path('youtubers_1', views.youtubers_1, name="youtubers_1"),
    path('youtubers_2', views.youtubers_2, name="youtubers_2"),
    path('youtubers_3', views.youtubers_3, name="youtubers_3"),
   
    
    
    
    path('search', views.search, name="search"),
    
]
