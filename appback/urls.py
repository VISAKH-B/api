from django.urls import path
from.import views

urlpatterns = [
    path('api/', views.tbl_todolst.as_view()),
    path('api/<int:pk>/', views.tbl_todolst.as_view()),
]