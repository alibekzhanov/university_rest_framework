from django.db import models


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_surname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_surname}"


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_room = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_surname = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f"{self.student_name} {self.student_surname}"
