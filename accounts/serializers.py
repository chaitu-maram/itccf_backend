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



from rest_framework import serializers
from .models import StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'



from rest_framework import serializers
from .models import StudentProfile, InterviewQuestion


class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestion
        fields = ['question']


class StudentProfileSerializer(serializers.ModelSerializer):
    questions = InterviewQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = StudentProfile
        fields = '__all__'


from rest_framework import serializers
from .models import HR


class HRSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = "__all__"



from rest_framework import serializers
from .models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"



from rest_framework import serializers
from .models import Employer, IndustrySector


class IndustrySectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndustrySector
        fields = ["id", "name"]


class EmployerSignupSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employer

        fields = [
            "name",
            "designation",
            "contact_number",
            "email",
            "password",
            "company_name",
            "company_industry",
            "company_address_line1",
            "company_address_line2",
            "company_city",
            "company_state",
            "company_pincode",
            "manufacturing_activity",
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_contact_number(self, value):

        if len(value) != 10:
            raise serializers.ValidationError(
                "Contact number must be 10 digits"
            )

        return value

    def validate_company_pincode(self, value):

        if len(value) != 6:
            raise serializers.ValidationError(
                "Pincode must be 6 digits"
            )

        return value
    


from rest_framework import serializers
from .models import HR


class HRProfileSerializer(serializers.ModelSerializer):

    hr_name = serializers.SerializerMethodField()

    class Meta:
        model = HR

        fields = [
            "hr_id",
            "first_name",
            "last_name",
            "hr_name",
            "email",
            "phone",
            "college_name",
            "college_code",
            "current_year",
            "college_state",
            "college_city",
            "roll_number",
            "created_at",
        ]

    def get_hr_name(self, obj):

        first = obj.first_name or ""
        last = obj.last_name or ""

        return f"{first} {last}".strip()