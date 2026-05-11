from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import (
    ITI,
    UG_Courses,
    PG_Courses,
    Intermediate_Courses,
    Vocational_Courses
)
from .serializers import (
    ITISerializer,
    UGCoursesSerializer,
    PGCoursesSerializer,
    IntermediateCoursesSerializer,
    VocationalCoursesSerializer
)

# ITI
class ITIListCreateView(generics.ListCreateAPIView):
    queryset = ITI.objects.all()
    serializer_class = ITISerializer

class ITIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ITI.objects.all()
    serializer_class = ITISerializer


# UG
class UGListCreateView(generics.ListCreateAPIView):
    queryset = UG_Courses.objects.all()
    serializer_class = UGCoursesSerializer

class UGDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UG_Courses.objects.all()
    serializer_class = UGCoursesSerializer


# PG
class PGListCreateView(generics.ListCreateAPIView):
    queryset = PG_Courses.objects.all()
    serializer_class = PGCoursesSerializer

class PGDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PG_Courses.objects.all()
    serializer_class = PGCoursesSerializer

#polytechnic
from rest_framework import generics
from .models import Polytechnic
from .serializers import PolytechnicSerializer


class PolytechnicListCreateView(generics.ListCreateAPIView):
    queryset = Polytechnic.objects.all()
    serializer_class = PolytechnicSerializer


class PolytechnicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polytechnic.objects.all()
    serializer_class = PolytechnicSerializer

# Intermediate
class IntermediateListCreateView(generics.ListCreateAPIView):
    queryset = Intermediate_Courses.objects.all()
    serializer_class = IntermediateCoursesSerializer

class IntermediateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intermediate_Courses.objects.all()
    serializer_class = IntermediateCoursesSerializer


# Vocational
class VocationalListCreateView(generics.ListCreateAPIView):
    queryset = Vocational_Courses.objects.all()
    serializer_class = VocationalCoursesSerializer

class VocationalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vocational_Courses.objects.all()
    serializer_class = VocationalCoursesSerializer


from .models import Degree
from .serializers import DegreeSerializer


class DegreeListCreateView(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


class DegreeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer



from rest_framework import viewsets
from .models import StudentProfile
from .serializers import StudentProfileSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all().order_by('-created_at')
    serializer_class = StudentProfileSerializer




from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import StudentProfile, InterviewQuestion
from .serializers import StudentProfileSerializer
from .ai_utils import generate_ai_questions


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    @action(detail=True, methods=['get'])
    def generate_questions(self, request, pk=None):
        student = self.get_object()

        # delete old questions
        InterviewQuestion.objects.filter(student=student).delete()

        # ✅ correct function call
        questions = generate_ai_questions(student)

        # save new questions
        for q in questions:
            InterviewQuestion.objects.create(student=student, question=q)

        return Response({
            "student_id": student.id,
            "student_name": student.name,
            "questions": questions
        })
    




import random

from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import HR
from .serializers import HRSignupSerializer


class HRSignupView(APIView):

    def post(self, request):

        data = request.data

        # generate otp
        otp = str(random.randint(100000, 999999))

        # save user
        hr = HR.objects.create(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            dob=data.get("dob"),
            college_code=data.get("college_code"),
            college_name=data.get("college_name"),
            roll_number=data.get("roll_number"),
            current_year=data.get("current_year"),
            college_state=data.get("college_state"),
            college_city=data.get("college_city"),
            phone=data.get("phone"),
            email=data.get("email"),
            password=data.get("password"),
            otp=otp,
        )

        # send otp mail
        send_mail(
            subject="Your OTP Verification Code",
            message=f"Your OTP is: {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[hr.email],
            fail_silently=False,
        )

        return Response(
            {
                "message": "Signup successful. OTP sent to email.",
                "email": hr.email
            },
            status=status.HTTP_201_CREATED
        )


class VerifyOTPView(APIView):

    def post(self, request):

        email = request.data.get("email")
        otp = request.data.get("otp")

        try:
            hr = HR.objects.get(email=email)

            if hr.otp == otp:
                hr.is_verified = True
                hr.otp = ""
                hr.save()

                return Response(
                    {"message": "Email verified successfully"},
                    status=status.HTTP_200_OK
                )

            return Response(
                {"error": "Invalid OTP"},
                status=status.HTTP_400_BAD_REQUEST
            )

        except HR.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import University
from .serializers import UniversitySerializer


@api_view(["GET"])
def get_universities(request):

    state = request.GET.get("state")

    if state:
        universities = University.objects.filter(state=state).order_by("name")
    else:
        universities = University.objects.all().order_by("name")

    serializer = UniversitySerializer(universities, many=True)

    return Response(serializer.data)