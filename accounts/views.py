from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HRProfileSerializer
from .models import HR
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




# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

# from .models import StudentProfile, InterviewQuestion
# from .serializers import StudentProfileSerializer
# from .ai_utils import generate_ai_questions


# class StudentProfileViewSet(viewsets.ModelViewSet):
#     queryset = StudentProfile.objects.all()
#     serializer_class = StudentProfileSerializer

#     @action(detail=True, methods=['get'])
#     def generate_questions(self, request, pk=None):
#         student = self.get_object()

#         # delete old questions
#         InterviewQuestion.objects.filter(student=student).delete()

#         # ✅ correct function call
#         questions = generate_ai_questions(student)

#         # save new questions
#         for q in questions:
#             InterviewQuestion.objects.create(student=student, question=q)

#         return Response({
#             "student_id": student.id,
#             "student_name": student.name,
#             "questions": questions
#         })
    




import random

from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import HR
from .serializers import HRSignupSerializer


# class HRSignupView(APIView):

#     def post(self, request):

#         data = request.data

#         # generate otp
#         otp = str(random.randint(100000, 999999))

#         # save user
#         hr = HR.objects.create(
#             first_name=data.get("first_name"),
#             last_name=data.get("last_name"),
#             dob=data.get("dob"),
#             college_code=data.get("college_code"),
#             college_name=data.get("college_name"),
#             roll_number=data.get("roll_number"),
#             current_year=data.get("current_year"),
#             college_state=data.get("college_state"),
#             college_city=data.get("college_city"),
#             phone=data.get("phone"),
#             email=data.get("email"),
#             password=data.get("password"),
#             otp=otp,
#         )

#         # send otp mail
#         send_mail(
#             subject="Your OTP Verification Code",
#             message=f"Your OTP is: {otp}",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[hr.email],
#             fail_silently=False,
#         )

#         return Response(
#             {
#                 "message": "Signup successful. OTP sent to email.",
#                 "email": hr.email
#             },
#             status=status.HTTP_201_CREATED
#         )



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from django.conf import settings

from .models import HR, University

import random


# class HRSignupView(APIView):

#     def post(self, request):

#         try:

#             data = request.data

#             # =========================
#             # CHECK EMAIL EXISTS
#             # =========================
#             email = data.get("email")

#             if email:

#                 existing_hr = HR.objects.filter(email=email).first()

#                 if existing_hr:

#                     return Response(
#                         {
#                             "message": "Email already registered"
#                         },
#                         status=status.HTTP_400_BAD_REQUEST
#                     )

#             # =========================
#             # GENERATE OTP
#             # =========================
#             otp = str(random.randint(100000, 999999))

#             # =========================
#             # UNIVERSITY
#             # =========================
#             university = None

#             university_id = data.get("university")

#             if university_id:

#                 university = University.objects.filter(
#                     id=university_id
#                 ).first()

#             # =========================
#             # CREATE HR
#             # =========================
#             hr = HR.objects.create(

#                 first_name=data.get("first_name"),

#                 last_name=data.get("last_name"),

#                 dob=data.get("dob"),

#                 college_code=data.get("college_code"),

#                 college_name=data.get("college_name"),

#                 roll_number=data.get("roll_number"),

#                 current_year=data.get("current_year"),

#                 college_state=data.get("college_state"),

#                 college_city=data.get("college_city"),

#                 phone=data.get("phone"),

#                 email=email,

#                 password=data.get("password"),

#                 otp=otp,

#                 university=university,
#             )

#             # =========================
#             # SEND OTP EMAIL
#             # =========================
#             if hr.email:

#                 send_mail(
#                     subject="Your OTP Verification Code",

#                     message=f"""
# Hello {hr.first_name},

# Your OTP verification code is:

# {otp}

# Your HR ID is:
# {hr.hr_id}

# Thank You
#                     """,

#                     from_email=settings.EMAIL_HOST_USER,

#                     recipient_list=[hr.email],

#                     fail_silently=False,
#                 )

#             # =========================
#             # SUCCESS RESPONSE
#             # =========================
#             return Response(
#                 {
#                     "message": "Signup successful. OTP sent to email.",

#                     "hr_id": hr.hr_id,

#                     "email": hr.email,

#                     "otp_sent": True,
#                 },
#                 status=status.HTTP_201_CREATED
#             )

#         except Exception as e:

#             return Response(
#                 {
#                     "message": "Signup failed",

#                     "error": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )


# class VerifyOTPView(APIView):

#     def post(self, request):

#         email = request.data.get("email")
#         otp = request.data.get("otp")

#         try:
#             hr = HR.objects.get(email=email)

#             if hr.otp == otp:
#                 hr.is_verified = True
#                 hr.otp = ""
#                 hr.save()

#                 return Response(
#                     {"message": "Email verified successfully"},
#                     status=status.HTTP_200_OK
#                 )

#             return Response(
#                 {"error": "Invalid OTP"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         except HR.DoesNotExist:
#             return Response(
#                 {"error": "User not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from django.conf import settings

from .models import HR, University

import random


# =========================================================
# HR SIGNUP
# =========================================================
class HRSignupView(APIView):

    def post(self, request):

        try:

            data = request.data

            # =========================
            # GET EMAIL
            # =========================
            email = data.get("email")

            if not email:
                return Response(
                    {
                        "message": "Email is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # =========================
            # CHECK EMAIL EXISTS
            # =========================
            existing_hr = HR.objects.filter(email=email).first()

            if existing_hr:

                # if already verified
                if existing_hr.is_verified:

                    return Response(
                        {
                            "message": "Email already registered and verified"
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # if not verified -> resend new otp
                otp = str(random.randint(100000, 999999))

                existing_hr.otp = otp
                existing_hr.save()

                send_mail(
                    subject="Your OTP Verification Code",

                    message=f"""
Hello {existing_hr.first_name},

Your new OTP verification code is:

{otp}

Your HR ID is:
{existing_hr.hr_id}

Thank You
                    """,

                    from_email=settings.EMAIL_HOST_USER,

                    recipient_list=[existing_hr.email],

                    fail_silently=False,
                )

                return Response(
                    {
                        "message": "User already exists but not verified. New OTP sent.",
                        "email": existing_hr.email,
                        "hr_id": existing_hr.hr_id,
                        "otp_sent": True
                    },
                    status=status.HTTP_200_OK
                )

            # =========================
            # GENERATE OTP
            # =========================
            otp = str(random.randint(100000, 999999))

            # =========================
            # UNIVERSITY
            # =========================
            university = None

            university_id = data.get("university")

            if university_id:

                university = University.objects.filter(
                    id=university_id
                ).first()

            # =========================
            # CREATE HR
            # =========================
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

                email=email,

                password=data.get("password"),

                otp=otp,

                is_verified=False,

                university=university,
            )

            # =========================
            # SEND OTP EMAIL
            # =========================
            send_mail(
                subject="Your OTP Verification Code",

                message=f"""
Hello {hr.first_name},

Your OTP verification code is:

{otp}

Your HR ID is:
{hr.hr_id}

Thank You
                """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[hr.email],

                fail_silently=False,
            )

            # =========================
            # SUCCESS RESPONSE
            # =========================
            return Response(
                {
                    "message": "Signup successful. OTP sent to email.",

                    "hr_id": hr.hr_id,

                    "email": hr.email,

                    "otp_sent": True,
                },
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                {
                    "message": "Signup failed",

                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


# =========================================================
# VERIFY OTP
# =========================================================
# class VerifyOTPView(APIView):

#     def post(self, request):

#         try:

#             email = request.data.get("email")
#             otp = request.data.get("otp")

#             if not email or not otp:

#                 return Response(
#                     {
#                         "error": "Email and OTP are required"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             hr = HR.objects.filter(email=email).first()

#             if not hr:

#                 return Response(
#                     {
#                         "error": "User not found"
#                     },
#                     status=status.HTTP_404_NOT_FOUND
#                 )

#             # =========================
#             # VERIFY OTP
#             # =========================
#             if hr.otp == otp:

#                 hr.is_verified = True
#                 hr.otp = ""
#                 hr.save()

#                 return Response(
#                     {
#                         "message": "Email verified successfully",
#                         "verified": True
#                     },
#                     status=status.HTTP_200_OK
#                 )

#             return Response(
#                 {
#                     "error": "Invalid OTP"
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         except Exception as e:

#             return Response(
#                 {
#                     "message": "OTP verification failed",
#                     "error": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )




class VerifyOTPView(APIView):

    def post(self, request):

        try:

            # =========================
            # GET DATA
            # =========================
            email = request.data.get("email", "").strip()
            otp = request.data.get("otp", "").strip()

            # =========================
            # VALIDATION
            # =========================
            if not email or not otp:

                return Response(
                    {
                        "error": "Email and OTP are required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # =========================
            # FIND HR ACCOUNT
            # =========================
            hr = HR.objects.filter(
                email__iexact=email
            ).order_by("-id").first()

            if not hr:

                return Response(
                    {
                        "error": "User not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # =========================
            # DEBUG
            # =========================
            print("DATABASE OTP :", hr.otp)
            print("ENTERED OTP  :", otp)
            print("BEFORE VERIFY:", hr.is_verified)

            # =========================
            # VERIFY OTP
            # =========================
            if str(hr.otp).strip() != str(otp).strip():

                return Response(
                    {
                        "error": "Invalid OTP"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # =========================
            # UPDATE DIRECTLY IN DATABASE
            # =========================
            HR.objects.filter(id=hr.id).update(
                is_verified=True,
                otp=""
            )

            # REFRESH OBJECT
            hr.refresh_from_db()

            print("AFTER VERIFY :", hr.is_verified)

            # =========================
            # SUCCESS RESPONSE
            # =========================
            return Response(
                {
                    "message": "Email verified successfully",
                    "verified": hr.is_verified,
                    "hr_id": hr.hr_id
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:

            print("VERIFY OTP ERROR:", str(e))

            return Response(
                {
                    "message": "OTP verification failed",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
# =========================================================
# RESEND OTP
# =========================================================
class HRResendOTPView(APIView):

    def post(self, request):

        try:

            email = request.data.get("email")

            if not email:

                return Response(
                    {
                        "error": "Email is required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            hr = HR.objects.filter(email=email).first()

            if not hr:

                return Response(
                    {
                        "error": "User not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # =========================
            # GENERATE NEW OTP
            # =========================
            otp = str(random.randint(100000, 999999))

            hr.otp = otp
            hr.save()

            # =========================
            # SEND EMAIL
            # =========================
            send_mail(
                subject="Resend OTP Verification Code",

                message=f"""
Hello {hr.first_name},

Your new OTP verification code is:

{otp}

Your HR ID is:
{hr.hr_id}

Thank You
                """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[hr.email],

                fail_silently=False,
            )

            return Response(
                {
                    "message": "OTP resent successfully",
                    "otp_sent": True
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {
                    "message": "Failed to resend OTP",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
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


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser, FormParser

from .models import StudentProfile, InterviewQuestion
from .serializers import StudentProfileSerializer
from .ai_utils import generate_ai_questions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


# class StudentProfileViewSet(viewsets.ModelViewSet):

#     queryset = StudentProfile.objects.all()

#     serializer_class = StudentProfileSerializer

#     # IMPORTANT FOR IMAGE UPLOADS
#     parser_classes = [MultiPartParser, FormParser]

#     @action(detail=True, methods=['get'])
#     def generate_questions(self, request, pk=None):

#         student = self.get_object()

#         # delete old questions
#         InterviewQuestion.objects.filter(student=student).delete()

#         # generate new questions
#         questions = generate_ai_questions(student)

#         # save new questions
#         for q in questions:
#             InterviewQuestion.objects.create(
#                 student=student,
#                 question=q
#             )

#         return Response({
#             "student_id": student.id,
#             "student_name": student.name,
#             "questions": questions
#         })

class StudentProfileViewSet(viewsets.ModelViewSet):

    queryset = StudentProfile.objects.all()

    serializer_class = StudentProfileSerializer

    parser_classes = [MultiPartParser, FormParser]

    @action(detail=True, methods=['patch'], parser_classes=[JSONParser])
    def submit_score(self, request, pk=None):
        student = self.get_object()
        score = request.data.get('score')
        if score is None:
            return Response({'error': 'score is required'}, status=400)
        try:
            student.score = float(score)
            student.save(update_fields=['score'])
        except (ValueError, TypeError):
            return Response({'error': 'Invalid score value'}, status=400)
        return Response({'student_id': student.id, 'score': student.score})

    @action(detail=True, methods=['get'])
    def generate_questions(self, request, pk=None):

        student = self.get_object()

        # delete old questions
        InterviewQuestion.objects.filter(
            student=student
        ).delete()

        # generate questions
        questions = generate_ai_questions(student)

        # save questions
        for q in questions:

            InterviewQuestion.objects.create(
                student=student,
                question=q
            )

        student.questions_ready = True
        student.save()

        return Response({
            "student_id": student.id,
            "student_name": student.name,
            "questions": questions
        })
    


import random

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Employer, IndustrySector

from .serializers import (
    EmployerSignupSerializer,
    IndustrySectorSerializer
)


class SendOTPView(APIView):

    def post(self, request):

        email = request.data.get("email")

        if not email:
            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        otp = str(random.randint(100000, 999999))

        employer, created = Employer.objects.get_or_create(
            email=email,
            defaults={
                "name": "",
                "designation": "",
                "contact_number": "",
                "password": "",
                "company_name": "",
                "company_address_line1": "",
                "company_city": "",
                "company_state": "",
                "company_pincode": "",
            }
        )

        employer.otp = otp
        employer.otp_created_at = timezone.now()

        employer.save()

        send_mail(
            subject="Employer Registration OTP",
            message=f"Your OTP is {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )

        return Response({
            "message": "OTP sent successfully"
        })


# class VerifyOTPView(APIView):

#     def post(self, request):

#         email = request.data.get("email")
#         otp = request.data.get("otp")

#         if not email or not otp:
#             return Response(
#                 {"error": "Email and OTP are required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             employer = Employer.objects.get(email=email)

#         except Employer.DoesNotExist:
#             return Response(
#                 {"error": "Employer not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         if not employer.otp_is_valid():
#             return Response(
#                 {"error": "OTP expired"}
#             )

#         if employer.otp != otp:
#             return Response(
#                 {"error": "Invalid OTP"}
#             )

#         employer.is_email_verified = True

#         employer.otp = None
#         employer.otp_created_at = None

#         employer.save()

#         return Response({
#             "message": "OTP verified successfully"
#         })

class EmployerVerifyOTPView(APIView):

    def post(self, request):

        try:

            email = request.data.get("email")
            otp = request.data.get("otp")

            if not email or not otp:

                return Response(
                    {
                        "error": "Email and OTP are required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            employer = Employer.objects.filter(
                email__iexact=email.strip()
            ).first()

            if not employer:

                return Response(
                    {
                        "error": "Employer not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # OTP EXPIRED
            if not employer.otp_is_valid():

                return Response(
                    {
                        "error": "OTP expired"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # INVALID OTP
            if str(employer.otp).strip() != str(otp).strip():

                return Response(
                    {
                        "error": "Invalid OTP"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # VERIFIED
            employer.is_email_verified = True
            employer.otp = None
            employer.otp_created_at = None

            employer.save()

            return Response(
                {
                    "message": "Employer email verified successfully",
                    "verified": True
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        


class HRVerifyOTPView(APIView):

    def post(self, request):

        try:

            email = request.data.get("email")
            otp = request.data.get("otp")

            if not email or not otp:

                return Response(
                    {
                        "error": "Email and OTP are required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            hr = HR.objects.filter(
                email__iexact=email.strip()
            ).first()

            if not hr:

                return Response(
                    {
                        "error": "HR user not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # VERIFY OTP
            if str(hr.otp).strip() != str(otp).strip():

                return Response(
                    {
                        "error": "Invalid OTP"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # UPDATE VERIFIED
            HR.objects.filter(id=hr.id).update(
                is_verified=True,
                otp=""
            )

            return Response(
                {
                    "message": "HR email verified successfully",
                    "verified": True
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

# class EmployerSignupView(APIView):

#     def post(self, request):

#         email = request.data.get("email")

#         if not email:
#             return Response(
#                 {"error": "Email is required"}
#             )

#         try:
#             employer = Employer.objects.get(email=email)

#         except Employer.DoesNotExist:
#             return Response(
#                 {"error": "Please verify email first"}
#             )

#         if not employer.is_email_verified:
#             return Response(
#                 {"error": "Email is not verified"}
#             )

#         serializer = EmployerSignupSerializer(
#             employer,
#             data=request.data,
#             partial=True
#         )

#         if serializer.is_valid():

#             serializer.save()

#             return Response({
#                 "message": "Employer account created successfully",
#                 "id": employer.id
#             })

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Employer
from .serializers import EmployerSignupSerializer


class EmployerSignupView(APIView):

    def post(self, request):

        email = request.data.get("email")

        if not email:
            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            employer = Employer.objects.get(email=email)

        except Employer.DoesNotExist:
            return Response(
                {"error": "Please verify email first"},
                status=status.HTTP_404_NOT_FOUND
            )

        # =========================
        # CHECK EMAIL VERIFIED
        # =========================
        if not employer.is_email_verified:
            return Response(
                {"error": "Email is not verified"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmployerSignupSerializer(
            employer,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Employer account created successfully",
                "id": employer.id,
                "employer_id": employer.employer_id
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

    
class IndustrySectorListView(APIView):

    def get(self, request):

        industries = IndustrySector.objects.all()

        serializer = IndustrySectorSerializer(
            industries,
            many=True
        )

        return Response(serializer.data)
    

from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import HR, Employer


@api_view(["POST"])
def signin(request):

    identifier = request.data.get("identifier", "").strip()
    password = request.data.get("password", "").strip()

    # =========================
    # VALIDATION
    # =========================
    if not identifier or not password:
        return Response(
            {
                "error": "ID/email and password are required."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    identifier_upper = identifier.upper()

    # =========================================================
    # LOGIN WITH HR ID
    # =========================================================
    if identifier_upper.startswith("HR"):

        try:
            hr = HR.objects.get(hr_id__iexact=identifier)

        except HR.DoesNotExist:
            return Response(
                {
                    "error": "Invalid HR ID or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        # account verification check
        if not hr.is_verified:
            return Response(
                {
                    "error": "HR account not verified."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        # password check
        if not check_password(password, hr.password):
            return Response(
                {
                    "error": "Invalid HR ID or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {
                "success": True,
                "role": "hr",

                "hr_id": hr.hr_id,
                "name": f"{hr.first_name} {hr.last_name}",
                "email": hr.email,

                "message": "HR login successful."
            },
            status=status.HTTP_200_OK
        )

    # =========================================================
    # LOGIN WITH EMPLOYER ID
    # =========================================================
    elif identifier_upper.startswith("EM"):

        try:
            employer = Employer.objects.get(
                employer_id__iexact=identifier
            )

        except Employer.DoesNotExist:
            return Response(
                {
                    "error": "Invalid Employer ID or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        # verification check
        if not employer.is_email_verified:
            return Response(
                {
                    "error": "Employer account not verified."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        # password check
        if not check_password(password, employer.password):
            return Response(
                {
                    "error": "Invalid Employer ID or password."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {
                "success": True,
                "role": "employer",

                "employer_id": employer.employer_id,
                "name": employer.name,
                "email": employer.email,
                "company_name": employer.company_name,

                "message": "Employer login successful."
            },
            status=status.HTTP_200_OK
        )

    # =========================================================
    # LOGIN WITH EMAIL
    # =========================================================
    else:

        # ---------- TRY HR EMAIL ----------
        hr = HR.objects.filter(email__iexact=identifier).first()

        if hr:

            if not hr.is_verified:
                return Response(
                    {
                        "error": "HR account not verified."
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

            if not check_password(password, hr.password):
                return Response(
                    {
                        "error": "Invalid email or password."
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            return Response(
                {
                    "success": True,
                    "role": "hr",

                    "hr_id": hr.hr_id,
                    "name": f"{hr.first_name} {hr.last_name}",
                    "email": hr.email,

                    "message": "HR login successful."
                },
                status=status.HTTP_200_OK
            )

        # ---------- TRY EMPLOYER EMAIL ----------
        employer = Employer.objects.filter(
            email__iexact=identifier
        ).first()

        if employer:

            if not employer.is_email_verified:
                return Response(
                    {
                        "error": "Employer account not verified."
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

            if not check_password(password, employer.password):
                return Response(
                    {
                        "error": "Invalid email or password."
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            return Response(
                {
                    "success": True,
                    "role": "employer",

                    "employer_id": employer.employer_id,
                    "name": employer.name,
                    "email": employer.email,
                    "company_name": employer.company_name,

                    "message": "Employer login successful."
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "error": "Account not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )
    

class HRProfileView(APIView):

    def get(self, request, hr_id):

        try:

            hr = HR.objects.get(hr_id=hr_id)

            serializer = HRProfileSerializer(hr)

            return Response(
                {
                    "success": True,
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        except HR.DoesNotExist:

            return Response(
                {
                    "error": "HR not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        



from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HR

class HRDetailView(APIView):

    def get(self, request, hr_id):

        hr = get_object_or_404(HR, hr_id=hr_id)

        students_count = hr.students.count()

        return Response({
            "hr_id": hr.hr_id,
            "first_name": hr.first_name,
            "last_name": hr.last_name,
            "email": hr.email,
            "phone": hr.phone,
            "students_count": students_count,
        })