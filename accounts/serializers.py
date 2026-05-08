from rest_framework import serializers
from .models import (
    ITI,
    UG_Courses,
    PG_Courses,
    Intermediate_Courses,
    Vocational_Courses
)

class ITISerializer(serializers.ModelSerializer):
    class Meta:
        model = ITI
        fields = '__all__'


class UGCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UG_Courses
        fields = '__all__'


class PGCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PG_Courses
        fields = '__all__'

from rest_framework import serializers
from .models import Polytechnic

class PolytechnicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polytechnic
        fields = '__all__'

class IntermediateCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intermediate_Courses
        fields = '__all__'


class VocationalCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocational_Courses
        fields = '__all__'



from .models import Degree

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'