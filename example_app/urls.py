from django.urls import path

from example_app import views

from .views import (
    CourseListAPIView, CourseDetailAPIView,
    StudentListAPIView, StudentDetailAPIView,
    ProfessorListAPIView, ProfessorDetailAPIView,
    DepartmentListAPIView, DepartmentDetailAPIView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('professors/', ProfessorListAPIView.as_view(), name='professor-list'),
    path('professors/<int:pk>/', ProfessorDetailAPIView.as_view(), name='professor-detail'),
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail')
]