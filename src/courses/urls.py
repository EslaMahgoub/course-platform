
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list_view, name="course-list"),
    path('<int:course_id>/', views.course_detail_view, name="course-detail"),
    path('<int:course_id>/lessons/<int:lesson_id>/', views.lesson_detail_view, name="lesson-detail"),
]
