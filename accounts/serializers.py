# from rest_framework import serializers
# from .models import (
#     ITI,
#     UG_Courses,
#     PG_Courses,
#     Intermediate_Courses,
#     Vocational_Courses
# )

# class ITISerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ITI
#         fields = '__all__'


# class UGCoursesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UG_Courses
#         fields = '__all__'


# class PGCoursesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PG_Courses
#         fields = '__all__'

# from rest_framework import serializers
# from .models import Polytechnic

# class PolytechnicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Polytechnic
#         fields = '__all__'

# class IntermediateCoursesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Intermediate_Courses
#         fields = '__all__'


# class VocationalCoursesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vocational_Courses
#         fields = '__all__'



# from .models import Degree

# class DegreeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Degree
#         fields = '__all__'



# from rest_framework import serializers
# from .models import StudentProfile

# class StudentProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentProfile
#         fields = '__all__'



# from rest_framework import serializers
# from .models import StudentProfile, InterviewQuestion


# class InterviewQuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InterviewQuestion
#         fields = ['question']


# # class StudentProfileSerializer(serializers.ModelSerializer):
# #     questions = InterviewQuestionSerializer(many=True, read_only=True)

# #     class Meta:
# #         model = StudentProfile
# #         fields = '__all__'


# # from rest_framework import serializers

# # class StudentProfileSerializer(serializers.ModelSerializer):
# #     questions = InterviewQuestionSerializer(many=True, read_only=True)

# #     hr_name = serializers.SerializerMethodField()
# #     hr_id = serializers.SerializerMethodField()

# #     class Meta:
# #         model = StudentProfile
# #         fields = '__all__'

# #     def get_hr_name(self, obj):
# #         if obj.hr:
# #             return f"{obj.hr.first_name} {obj.hr.last_name}"
# #         return None

# #     def get_hr_id(self, obj):
# #         if obj.hr:
# #             return obj.hr.hr_id
# #         return None


# class StudentProfileSerializer(serializers.ModelSerializer):

#     questions = InterviewQuestionSerializer(
#         many=True,
#         read_only=True
#     )

#     hr_name = serializers.SerializerMethodField()
#     hr_id = serializers.SerializerMethodField()

#     class Meta:
#         model = StudentProfile
#         fields = "__all__"

#     def get_hr_name(self, obj):

#         if obj.hr:
#             first = obj.hr.first_name or ""
#             last = obj.hr.last_name or ""

#             return f"{first} {last}".strip()

#         return ""

#     def get_hr_id(self, obj):

#         if obj.hr:
#             return obj.hr.hr_id

#         return ""
    

# from rest_framework import serializers
# from .models import HR


# class HRSignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HR
#         fields = "__all__"



# from rest_framework import serializers
# from .models import University


# class UniversitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = University
#         fields = "__all__"



# from rest_framework import serializers
# from .models import Employer, IndustrySector


# class IndustrySectorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = IndustrySector
#         fields = ["id", "name"]


# class EmployerSignupSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = Employer

#         fields = [
#             "name",
#             "designation",
#             "contact_number",
#             "email",
#             "password",
#             "company_name",
#             "company_industry",
#             "company_address_line1",
#             "company_address_line2",
#             "company_city",
#             "company_state",
#             "company_pincode",
#             "manufacturing_activity",
#         ]

#         extra_kwargs = {
#             "password": {"write_only": True}
#         }

#     def validate_contact_number(self, value):

#         if len(value) != 10:
#             raise serializers.ValidationError(
#                 "Contact number must be 10 digits"
#             )

#         return value

#     def validate_company_pincode(self, value):

#         if len(value) != 6:
#             raise serializers.ValidationError(
#                 "Pincode must be 6 digits"
#             )

#         return value
    


# from rest_framework import serializers
# from .models import HR


# class HRProfileSerializer(serializers.ModelSerializer):

#     hr_name = serializers.SerializerMethodField()

#     class Meta:
#         model = HR

#         fields = [
#             "hr_id",
#             "first_name",
#             "last_name",
#             "hr_name",
#             "email",
#             "phone",
#             "college_name",
#             "college_code",
#             "current_year",
#             "college_state",
#             "college_city",
#             "roll_number",
#             "created_at",
#         ]

#     def get_hr_name(self, obj):

#         first = obj.first_name or ""
#         last = obj.last_name or ""

#         return f"{first} {last}".strip()
    







# from rest_framework import serializers
# from .models import JobPosting   
 
# class JobPostingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = JobPosting
#         fields = [
#             'id', 'employer_id', 'org', 'role',
#             'location', 'salary', 'available_jobs',
#             'description', 'is_active', 'created_at',
#         ]
#         read_only_fields = ['id', 'created_at', 'employer_id']  # ← add employer_id

#     def validate_available_jobs(self, value):
#         if value < 1:
#             raise serializers.ValidationError("Must have at least 1 vacancy.")
#         return value
    
 
# class JobBoardSerializer(serializers.Serializer):
#     """
#     Shape returned to the Index page JobGrid:
#       [ { org, role, n }, … ]
#     where n = sum of available_jobs across all active postings for that (org, role).
#     """
#     org  = serializers.CharField()
#     role = serializers.CharField()
#     n    = serializers.IntegerField()
 
 
# class BulkJobPostSerializer(serializers.Serializer):
#     """Validates the payload from PostJob.tsx"""
#     employer_id = serializers.CharField(max_length=50)
#     jobs        = JobPostingSerializer(many=True)
 
#     def create(self, validated_data):
#         eid  = validated_data['employer_id']
#         objs = [
#             JobPosting(employer_id=eid, **j)   # type: ignore[name-defined]
#             for j in validated_data['jobs']
#         ]
#         return JobPosting.objects.bulk_create(objs)   # type: ignore[name-defined]



from rest_framework import serializers
from .models import (
    ITI,
    UG_Courses,
    PG_Courses,
    Intermediate_Courses,
    Vocational_Courses,
    Polytechnic,
    Degree,
    StudentProfile,
    InterviewQuestion,
    HR,
    University,
    Employer,
    IndustrySector,
    JobPosting,
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


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'


class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestion
        fields = ['question']


# ✅ Single definition — no duplicate
class StudentProfileSerializer(serializers.ModelSerializer):

    questions = InterviewQuestionSerializer(many=True, read_only=True)
    hr_name   = serializers.SerializerMethodField()
    hr_id     = serializers.SerializerMethodField()

    class Meta:
        model  = StudentProfile
        fields = '__all__'

    def get_hr_name(self, obj):
        if obj.hr:
            first = obj.hr.first_name or ""
            last  = obj.hr.last_name  or ""
            return f"{first} {last}".strip()
        return ""

    def get_hr_id(self, obj):
        if obj.hr:
            return obj.hr.hr_id
        return ""


class HRSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HR
        fields = '__all__'


class HRProfileSerializer(serializers.ModelSerializer):

    hr_name = serializers.SerializerMethodField()

    class Meta:
        model  = HR
        fields = [
            'hr_id', 'first_name', 'last_name', 'hr_name',
            'email', 'phone', 'college_name', 'college_code',
            'current_year', 'college_state', 'college_city',
            'roll_number', 'created_at',
        ]

    def get_hr_name(self, obj):
        first = obj.first_name or ""
        last  = obj.last_name  or ""
        return f"{first} {last}".strip()


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = University
        fields = '__all__'


class IndustrySectorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = IndustrySector
        fields = ['id', 'name']


class EmployerSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Employer
        fields = [
            'name', 'designation', 'contact_number', 'email',
            'password', 'company_name', 'company_industry',
            'company_address_line1', 'company_address_line2',
            'company_city', 'company_state', 'company_pincode',
            'manufacturing_activity',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_contact_number(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("Contact number must be 10 digits")
        return value

    def validate_company_pincode(self, value):
        if len(value) != 6:
            raise serializers.ValidationError("Pincode must be 6 digits")
        return value



# class JobPostingSerializer(serializers.ModelSerializer):
#     available_jobs = serializers.IntegerField(write_only=True, required=False)

#     class Meta:
#         model  = JobPosting
#         fields = ['id', 'employer', 'org', 'role', 'vacancies', 'available_jobs', 'is_active', 'created_at']
#         read_only_fields = ['id', 'created_at', 'employer']

#     def validate(self, data):
#         # Map available_jobs → vacancies if frontend sends available_jobs
#         if 'available_jobs' in data and 'vacancies' not in data:
#             data['vacancies'] = data.pop('available_jobs')
#         elif 'available_jobs' in data:
#             data.pop('available_jobs')
#         return data

#     def validate_vacancies(self, value):
#         if value < 1:
#             raise serializers.ValidationError("Must have at least 1 vacancy.")
#         return value
    
class JobInputSerializer(serializers.Serializer):
    org            = serializers.CharField(max_length=255)
    role           = serializers.CharField(max_length=255)
    location       = serializers.CharField(max_length=255, required=False, allow_blank=True)
    salary         = serializers.CharField(max_length=100, required=False, allow_blank=True)
    available_jobs = serializers.IntegerField(min_value=1, default=1)
    description    = serializers.CharField(required=False, allow_blank=True)

# class BulkJobPostSerializer(serializers.Serializer):
#     employer_id = serializers.CharField(max_length=50)
#     jobs        = JobPostingSerializer(many=True)


#     def create(self, validated_data):
#         eid = validated_data['employer_id']
        
#         try:
#             employer = Employer.objects.get(employer_id=eid)
#         except Employer.DoesNotExist:
#             raise serializers.ValidationError(
#                 {"employer_id": f"No employer found with ID '{eid}'."}
#             )
        
#         objs = [
#             JobPosting(
#                 employer=employer,
#                 org=job['org'],
#                 role=job['role'],
#                 vacancies=job.get('vacancies', job.get('available_jobs', 1)),  # handles both
#             )
#             for job in validated_data['jobs']
#         ]
#         return JobPosting.objects.bulk_create(objs)
        

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = JobPosting
        fields = ['id', 'employer', 'org', 'role', 'vacancies', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at', 'employer']


class BulkJobPostSerializer(serializers.Serializer):
    employer_id = serializers.CharField(max_length=50)
    jobs        = JobInputSerializer(many=True)          # ← was JobPostingSerializer

    def create(self, validated_data):
        eid = validated_data['employer_id']
        try:
            employer = Employer.objects.get(employer_id=eid)
        except Employer.DoesNotExist:
            raise serializers.ValidationError(
                {"employer_id": f"No employer found with ID '{eid}'."}
            )

        objs = [
            JobPosting(
                employer=employer,
                org=job['org'],
                role=job['role'],
                vacancies=job.get('available_jobs', 1),
            )
            for job in validated_data['jobs']
        ]
        return JobPosting.objects.bulk_create(objs)
    


class JobBoardSerializer(serializers.Serializer):
    org  = serializers.CharField()
    role = serializers.CharField()
    n    = serializers.IntegerField()