from django.urls import path
from .views import person_detail, person_list

urlpatterns = [
    path('', person_list, name='person_list'),
    path('<int:pk>/', person_detail, name='person_detail'),
]