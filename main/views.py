from rest_framework import generics
from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer


# Представление для списка и создания курсов
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Представление для списка и создания студентов
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
