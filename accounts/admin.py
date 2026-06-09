from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    ITI,
    UG_Courses,
    PG_Courses,
    Intermediate_Courses,
    Vocational_Courses,
    Degree,
    Polytechnic,
    StudentProfile,
    InterviewQuestion,
    University,
    HR,
    IndustrySector,
    Employer,
    Payment,
    JobPosting,
)


@admin.register(ITI)
class ITIAdmin(admin.ModelAdmin):
    list_display = ("id", "academic", "specialization")
    search_fields = ("academic",)


@admin.register(UG_Courses)
class UGCoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "academic", "specialization")
    search_fields = ("academic",)


@admin.register(PG_Courses)
class PGCoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "academic", "specialization")
    search_fields = ("academic",)


@admin.register(Intermediate_Courses)
class IntermediateCoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "academic", "specialization")
    search_fields = ("academic",)


@admin.register(Vocational_Courses)
class VocationalCoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "academic", "specialization")
    search_fields = ("academic",)


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ("id", "academic", "specialization", "sub_course")
    search_fields = ("academic", "specialization")


@admin.register(Polytechnic)
class PolytechnicAdmin(admin.ModelAdmin):
    list_display = ("id", "academic", "specialization")
    search_fields = ("academic",)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "surname",
        "mobile_personal",
        "email",
        "academic",
        "specialization",
        "score",
        "created_at",
    )
    search_fields = (
        "name",
        "surname",
        "email",
        "mobile_personal",
        "regn_no",
    )
    list_filter = (
        "academic",
        "questions_ready",
        "created_at",
    )


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "question")
    search_fields = ("question",)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "state", "city")
    search_fields = ("name", "state", "city")


@admin.register(HR)
class HRAdmin(admin.ModelAdmin):
    list_display = (
        "hr_id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_verified",
        "created_at",
    )
    search_fields = (
        "hr_id",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "is_verified",
        "current_year",
        "created_at",
    )


@admin.register(IndustrySector)
class IndustrySectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "employer_id",
        "company_name",
        "name",
        "email",
        "contact_number",
        "is_email_verified",
        "created_at",
    )
    search_fields = (
        "company_name",
        "name",
        "email",
        "employer_id",
    )
    list_filter = (
        "is_email_verified",
        "created_at",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "employer",
        "student",
        "amount",
        "status",
        "created_at",
    )
    list_filter = ("status",)
    search_fields = (
        "employer__company_name",
        "student__name",
    )


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "role",
        "org",
        "vacancies",
        "location",
        "is_active",
        "created_at",
    )
    search_fields = (
        "role",
        "org",
        "location",
    )
    list_filter = (
        "is_active",
        "created_at",
    )