from rest_framework import serializers
from .models import Course, Student, Professor, Department



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        read_only_fields = ['id']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['id']

class CourseSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset=Professor.objects.all(), write_only=True)
    department = DepartmentSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        department_id = validated_data.pop('department_id')
        professor_id = validated_data.pop('professor_id')
        course = Course.objects.create(department=department_id, professor=professor_id, **validated_data)
        return course
