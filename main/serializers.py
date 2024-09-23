from rest_framework import serializers
from .models import Course, Teacher, Student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'teacher_surname', 'subject']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_name', 'student_surname']


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Вложенный сериализатор для учителя
    students = serializers.SlugRelatedField(
        many=True, slug_field='student_name', queryset=Student.objects.all()
    )  # Связанный сериализатор для студентов

    class Meta:
        model = Course
        fields = ['course_name', 'course_room', 'teacher', 'students']

    def create(self, validated_data):
        # Извлекаем данные учителя
        teacher_data = validated_data.pop('teacher')
        # Создаем учителя
        teacher = Teacher.objects.create(**teacher_data)
        
        # Создаем курс, связанный с учителем
        course = Course.objects.create(teacher=teacher, **validated_data)
        
        # Добавляем студентов, если они переданы
        students = validated_data.get('students', [])
        for student in students:
            course.students.add(student)
        
        return course
