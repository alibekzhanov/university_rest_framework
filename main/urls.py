from django.urls import path
from .views import CourseListCreateView, StudentListCreateView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
]
