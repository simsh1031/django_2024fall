from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Student(Person):
    student_id = models.CharField(max_length=10, verbose_name="학번")
    department = models.ForeignKey("example_app.department", on_delete=models.PROTECT)

    class Meta:
        db_table = 'student'
        verbose_name = '학생'

class Professor(Person):
    employee_id = models.CharField(max_length=10)
    department = models.ForeignKey("example_app.department", on_delete=models.PROTECT)

    class Meta:
        db_table = 'professor'
        verbose_name = '교직원'

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'
        verbose_name = '학과'

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey("example_app.department", on_delete=models.CASCADE)
    professor = models.ForeignKey("example_app.professor", on_delete=models.CASCADE)


    class Meta:
        db_table = 'course'
        verbose_name = '강의'
