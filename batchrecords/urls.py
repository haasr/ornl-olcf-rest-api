from django.urls import path
from . import views

urlpatterns = [
    path('batch_jobs/', views.BatchJobList.as_view()),
]