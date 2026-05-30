# from django.shortcuts import render


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .serializers import HRProfileSerializer
# from .models import HR
# # Create your views here.
# from rest_framework import generics
# from .models import (
#     ITI,
#     UG_Courses,
#     PG_Courses,
#     Intermediate_Courses,
#     Vocational_Courses
# )
# from .serializers import (
#     ITISerializer,
#     UGCoursesSerializer,
#     PGCoursesSerializer,
#     IntermediateCoursesSerializer,
#     VocationalCoursesSerializer
# )

# # ITI
# class ITIListCreateView(generics.ListCreateAPIView):
#     queryset = ITI.objects.all()
#     serializer_class = ITISerializer

# class ITIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ITI.objects.all()
#     serializer_class = ITISerializer


# # UG
# class UGListCreateView(generics.ListCreateAPIView):
#     queryset = UG_Courses.objects.all()
#     serializer_class = UGCoursesSerializer

# class UGDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UG_Courses.objects.all()
#     serializer_class = UGCoursesSerializer


# # PG
# class PGListCreateView(generics.ListCreateAPIView):
#     queryset = PG_Courses.objects.all()
#     serializer_class = PGCoursesSerializer

# class PGDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PG_Courses.objects.all()
#     serializer_class = PGCoursesSerializer

# #polytechnic
# from rest_framework import generics
# from .models import Polytechnic
# from .serializers import PolytechnicSerializer


# class PolytechnicListCreateView(generics.ListCreateAPIView):
#     queryset = Polytechnic.objects.all()
#     serializer_class = PolytechnicSerializer


# class PolytechnicDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Polytechnic.objects.all()
#     serializer_class = PolytechnicSerializer

# # Intermediate
# class IntermediateListCreateView(generics.ListCreateAPIView):
#     queryset = Intermediate_Courses.objects.all()
#     serializer_class = IntermediateCoursesSerializer

# class IntermediateDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Intermediate_Courses.objects.all()
#     serializer_class = IntermediateCoursesSerializer


# # Vocational
# class VocationalListCreateView(generics.ListCreateAPIView):
#     queryset = Vocational_Courses.objects.all()
#     serializer_class = VocationalCoursesSerializer

# class VocationalDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vocational_Courses.objects.all()
#     serializer_class = VocationalCoursesSerializer


# from .models import Degree
# from .serializers import DegreeSerializer


# class DegreeListCreateView(generics.ListCreateAPIView):
#     queryset = Degree.objects.all()
#     serializer_class = DegreeSerializer


# class DegreeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Degree.objects.all()
#     serializer_class = DegreeSerializer



# from rest_framework import viewsets
# from .models import StudentProfile
# from .serializers import StudentProfileSerializer

# class StudentProfileViewSet(viewsets.ModelViewSet):
#     queryset = StudentProfile.objects.all().order_by('-created_at')
#     serializer_class = StudentProfileSerializer







# import random

# from django.core.mail import send_mail
# from django.conf import settings

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import HR
# from .serializers import HRSignupSerializer




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from django.core.mail import send_mail
# from django.conf import settings

# from .models import HR, University

# import random



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from django.core.mail import send_mail
# from django.conf import settings

# from .models import HR, University

# import random


# # =========================================================
# # HR SIGNUP
# # =========================================================
# class HRSignupView(APIView):

#     def post(self, request):

#         try:

#             data = request.data

#             # =========================
#             # GET EMAIL
#             # =========================
#             email = data.get("email")

#             if not email:
#                 return Response(
#                     {
#                         "message": "Email is required"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # =========================
#             # CHECK EMAIL EXISTS
#             # =========================
#             existing_hr = HR.objects.filter(email=email).first()

#             if existing_hr:

#                 # if already verified
#                 if existing_hr.is_verified:

#                     return Response(
#                         {
#                             "message": "Email already registered and verified"
#                         },
#                         status=status.HTTP_400_BAD_REQUEST
#                     )

#                 # if not verified -> resend new otp
#                 otp = str(random.randint(100000, 999999))

#                 existing_hr.otp = otp
#                 existing_hr.save()

#                 send_mail(
#                     subject="Your OTP Verification Code",

#                     message=f"""
# Hello {existing_hr.first_name},

# Your new OTP verification code is:

# {otp}

# Your HR ID is:
# {existing_hr.hr_id}

# Thank You
#                     """,

#                     from_email=settings.EMAIL_HOST_USER,

#                     recipient_list=[existing_hr.email],

#                     fail_silently=False,
#                 )

#                 return Response(
#                     {
#                         "message": "User already exists but not verified. New OTP sent.",
#                         "email": existing_hr.email,
#                         "hr_id": existing_hr.hr_id,
#                         "otp_sent": True
#                     },
#                     status=status.HTTP_200_OK
#                 )

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

#                 is_verified=False,

#                 university=university,
#             )

#             # =========================
#             # SEND OTP EMAIL
#             # =========================
#             send_mail(
#                 subject="Your OTP Verification Code",

#                 message=f"""
# Hello {hr.first_name},

# Your OTP verification code is:

# {otp}

# Your HR ID is:
# {hr.hr_id}

# Thank You
#                 """,

#                 from_email=settings.EMAIL_HOST_USER,

#                 recipient_list=[hr.email],

#                 fail_silently=False,
#             )

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

#         try:

#             # =========================
#             # GET DATA
#             # =========================
#             email = request.data.get("email", "").strip()
#             otp = request.data.get("otp", "").strip()

#             # =========================
#             # VALIDATION
#             # =========================
#             if not email or not otp:

#                 return Response(
#                     {
#                         "error": "Email and OTP are required"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # =========================
#             # FIND HR ACCOUNT
#             # =========================
#             hr = HR.objects.filter(
#                 email__iexact=email
#             ).order_by("-id").first()

#             if not hr:

#                 return Response(
#                     {
#                         "error": "User not found"
#                     },
#                     status=status.HTTP_404_NOT_FOUND
#                 )

#             # =========================
#             # DEBUG
#             # =========================
#             print("DATABASE OTP :", hr.otp)
#             print("ENTERED OTP  :", otp)
#             print("BEFORE VERIFY:", hr.is_verified)

#             # =========================
#             # VERIFY OTP
#             # =========================
#             if str(hr.otp).strip() != str(otp).strip():

#                 return Response(
#                     {
#                         "error": "Invalid OTP"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # =========================
#             # UPDATE DIRECTLY IN DATABASE
#             # =========================
#             HR.objects.filter(id=hr.id).update(
#                 is_verified=True,
#                 otp=""
#             )

#             # REFRESH OBJECT
#             hr.refresh_from_db()

#             print("AFTER VERIFY :", hr.is_verified)

#             # =========================
#             # SUCCESS RESPONSE
#             # =========================
#             return Response(
#                 {
#                     "message": "Email verified successfully",
#                     "verified": hr.is_verified,
#                     "hr_id": hr.hr_id
#                 },
#                 status=status.HTTP_200_OK
#             )

#         except Exception as e:

#             print("VERIFY OTP ERROR:", str(e))

#             return Response(
#                 {
#                     "message": "OTP verification failed",
#                     "error": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
        
# # =========================================================
# # RESEND OTP
# # =========================================================
# class HRResendOTPView(APIView):

#     def post(self, request):

#         try:

#             email = request.data.get("email")

#             if not email:

#                 return Response(
#                     {
#                         "error": "Email is required"
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
#             # GENERATE NEW OTP
#             # =========================
#             otp = str(random.randint(100000, 999999))

#             hr.otp = otp
#             hr.save()

#             # =========================
#             # SEND EMAIL
#             # =========================
#             send_mail(
#                 subject="Resend OTP Verification Code",

#                 message=f"""
# Hello {hr.first_name},

# Your new OTP verification code is:

# {otp}

# Your HR ID is:
# {hr.hr_id}

# Thank You
#                 """,

#                 from_email=settings.EMAIL_HOST_USER,

#                 recipient_list=[hr.email],

#                 fail_silently=False,
#             )

#             return Response(
#                 {
#                     "message": "OTP resent successfully",
#                     "otp_sent": True
#                 },
#                 status=status.HTTP_200_OK
#             )

#         except Exception as e:

#             return Response(
#                 {
#                     "message": "Failed to resend OTP",
#                     "error": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import University
# from .serializers import UniversitySerializer


# @api_view(["GET"])
# def get_universities(request):

#     state = request.GET.get("state")

#     if state:
#         universities = University.objects.filter(state=state).order_by("name")
#     else:
#         universities = University.objects.all().order_by("name")

#     serializer = UniversitySerializer(universities, many=True)

#     return Response(serializer.data)


# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

# from rest_framework.parsers import MultiPartParser, FormParser

# from .models import StudentProfile, InterviewQuestion
# from .serializers import StudentProfileSerializer
# from .ai_utils import generate_ai_questions
# from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# from .models import HR
# class StudentProfileViewSet(viewsets.ModelViewSet):

#     queryset = StudentProfile.objects.all()

#     serializer_class = StudentProfileSerializer

#     parser_classes = [MultiPartParser, FormParser]

#     @action(detail=True, methods=['patch'], parser_classes=[JSONParser])
#     def submit_score(self, request, pk=None):
#         student = self.get_object()
#         score = request.data.get('score')
#         if score is None:
#             return Response({'error': 'score is required'}, status=400)
#         try:
#             student.score = float(score)
#             student.save(update_fields=['score'])
#         except (ValueError, TypeError):
#             return Response({'error': 'Invalid score value'}, status=400)
#         return Response({'student_id': student.id, 'score': student.score})



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

#         serializer_class = StudentProfileSerializer

#     def get_queryset(self):

#         hr_id = self.request.query_params.get("hr_id")

#         if hr_id:
#             return StudentProfile.objects.filter(
#                 id_no=hr_id
#             )

#         return StudentProfile.objects.all()
#     def perform_create(self, serializer):

#         hr_id = self.request.data.get("hr_id")

#         if hr_id:

#             hr = HR.objects.filter(hr_id=hr_id).first()

#             if hr:

#                 serializer.save(
#                     hr=hr,
#                     hr_name=f"{hr.first_name} {hr.last_name}",
#                     id_no=hr.hr_id
#                 )

#                 return

#         serializer.save()


# import random

# from django.conf import settings
# from django.core.mail import send_mail
# from django.utils import timezone

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Employer, IndustrySector

# from .serializers import (
#     EmployerSignupSerializer,
#     IndustrySectorSerializer
# )


# class SendOTPView(APIView):

#     def post(self, request):

#         email = request.data.get("email")

#         if not email:
#             return Response(
#                 {"error": "Email is required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         otp = str(random.randint(100000, 999999))

#         employer, created = Employer.objects.get_or_create(
#             email=email,
#             defaults={
#                 "name": "",
#                 "designation": "",
#                 "contact_number": "",
#                 "password": "",
#                 "company_name": "",
#                 "company_address_line1": "",
#                 "company_city": "",
#                 "company_state": "",
#                 "company_pincode": "",
#             }
#         )

#         employer.otp = otp
#         employer.otp_created_at = timezone.now()

#         employer.save()

#         send_mail(
#             subject="Employer Registration OTP",
#             # message=f"Your OTP is {otp}",
#             message=f"""
# Your OTP is {otp}

# Your Employer ID is {employer.employer_id}

# Thank You
# """,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[email],
#             fail_silently=False
#         )

#         return Response({
#             "message": "OTP sent successfully"
#         })


# class EmployerVerifyOTPView(APIView):

#     def post(self, request):

#         try:

#             # =========================
#             # GET DATA
#             # =========================
#             email = request.data.get("email")
#             otp = request.data.get("otp")

#             # =========================
#             # VALIDATION
#             # =========================
#             if not email or not otp:

#                 return Response(
#                     {
#                         "error": "Email and OTP are required"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # =========================
#             # FIND EMPLOYER
#             # =========================
#             employer = Employer.objects.filter(
#                 email__iexact=email.strip()
#             ).first()

#             if not employer:

#                 return Response(
#                     {
#                         "error": "Employer not found"
#                     },
#                     status=status.HTTP_404_NOT_FOUND
#                 )

#             # =========================
#             # CHECK OTP EXPIRY
#             # =========================
#             if not employer.otp_is_valid():

#                 return Response(
#                     {
#                         "error": "OTP expired"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # =========================
#             # CHECK OTP MATCH
#             # =========================
#             if str(employer.otp).strip() != str(otp).strip():

#                 return Response(
#                     {
#                         "error": "Invalid OTP"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # =========================
#             # VERIFY EMPLOYER
#             # =========================
#             employer.is_email_verified = True
#             employer.otp = None
#             employer.otp_created_at = None

#             employer.save()

#             # =========================
#             # SUCCESS RESPONSE
#             # =========================
#             return Response(
#                 {
#                     "message": "Employer email verified successfully",

#                     "verified": True,

#                     "employer_id": employer.employer_id,

#                     "email": employer.email
#                 },
#                 status=status.HTTP_200_OK
#             )

#         except Exception as e:

#             return Response(
#                 {
#                     "error": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        

# class HRVerifyOTPView(APIView):

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

#             hr = HR.objects.filter(
#                 email__iexact=email.strip()
#             ).first()

#             if not hr:

#                 return Response(
#                     {
#                         "error": "HR user not found"
#                     },
#                     status=status.HTTP_404_NOT_FOUND
#                 )

#             # VERIFY OTP
#             if str(hr.otp).strip() != str(otp).strip():

#                 return Response(
#                     {
#                         "error": "Invalid OTP"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             # UPDATE VERIFIED
#             HR.objects.filter(id=hr.id).update(
#                 is_verified=True,
#                 otp=""
#             )

#             return Response(
#                 {
#                     "message": "HR email verified successfully",
#                     "verified": True
#                 },
#                 status=status.HTTP_200_OK
#             )

#         except Exception as e:

#             return Response(
#                 {
#                     "error": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Employer
# from .serializers import EmployerSignupSerializer


# class EmployerSignupView(APIView):

#     def post(self, request):

#         email = request.data.get("email")

#         if not email:
#             return Response(
#                 {"error": "Email is required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             employer = Employer.objects.get(email=email)

#         except Employer.DoesNotExist:
#             return Response(
#                 {"error": "Please verify email first"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         # =========================
#         # CHECK EMAIL VERIFIED
#         # =========================
#         if not employer.is_email_verified:
#             return Response(
#                 {"error": "Email is not verified"},
#                 status=status.HTTP_400_BAD_REQUEST
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
#                 "id": employer.id,
#                 "employer_id": employer.employer_id
#             })

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
    

    
# class IndustrySectorListView(APIView):

#     def get(self, request):

#         industries = IndustrySector.objects.all()

#         serializer = IndustrySectorSerializer(
#             industries,
#             many=True
#         )

#         return Response(serializer.data)
    

# from django.contrib.auth.hashers import check_password
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from .models import HR, Employer


# @api_view(["POST"])
# def signin(request):

#     identifier = request.data.get("identifier", "").strip()
#     password = request.data.get("password", "").strip()

#     # =========================
#     # VALIDATION
#     # =========================
#     if not identifier or not password:
#         return Response(
#             {
#                 "error": "ID/email and password are required."
#             },
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     identifier_upper = identifier.upper()

#     # =========================================================
#     # LOGIN WITH HR ID
#     # =========================================================
#     if identifier_upper.startswith("HR"):

#         try:
#             hr = HR.objects.get(hr_id__iexact=identifier)

#         except HR.DoesNotExist:
#             return Response(
#                 {
#                     "error": "Invalid HR ID or password."
#                 },
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         # account verification check
#         if not hr.is_verified:
#             return Response(
#                 {
#                     "error": "HR account not verified."
#                 },
#                 status=status.HTTP_403_FORBIDDEN
#             )

#         # password check
#         if not check_password(password, hr.password):
#             return Response(
#                 {
#                     "error": "Invalid HR ID or password."
#                 },
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         return Response(
#             {
#                 "success": True,
#                 "role": "hr",

#                 "hr_id": hr.hr_id,
#                 "name": f"{hr.first_name} {hr.last_name}",
#                 "email": hr.email,

#                 "message": "HR login successful."
#             },
#             status=status.HTTP_200_OK
#         )

#     # =========================================================
#     # LOGIN WITH EMPLOYER ID
#     # =========================================================
#     elif identifier_upper.startswith("EM"):

#         try:
#             employer = Employer.objects.get(
#                 employer_id__iexact=identifier
#             )

#         except Employer.DoesNotExist:
#             return Response(
#                 {
#                     "error": "Invalid Employer ID or password."
#                 },
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         # verification check
#         if not employer.is_email_verified:
#             return Response(
#                 {
#                     "error": "Employer account not verified."
#                 },
#                 status=status.HTTP_403_FORBIDDEN
#             )

#         # password check
#         if not check_password(password, employer.password):
#             return Response(
#                 {
#                     "error": "Invalid Employer ID or password."
#                 },
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         return Response(
#             {
#                 "success": True,
#                 "role": "employer",

#                 "employer_id": employer.employer_id,
#                 "name": employer.name,
#                 "email": employer.email,
#                 "company_name": employer.company_name,

#                 "message": "Employer login successful."
#             },
#             status=status.HTTP_200_OK
#         )

#     # =========================================================
#     # LOGIN WITH EMAIL
#     # =========================================================
#     else:

#         # ---------- TRY HR EMAIL ----------
#         hr = HR.objects.filter(email__iexact=identifier).first()

#         if hr:

#             if not hr.is_verified:
#                 return Response(
#                     {
#                         "error": "HR account not verified."
#                     },
#                     status=status.HTTP_403_FORBIDDEN
#                 )

#             if not check_password(password, hr.password):
#                 return Response(
#                     {
#                         "error": "Invalid email or password."
#                     },
#                     status=status.HTTP_401_UNAUTHORIZED
#                 )

#             return Response(
#                 {
#                     "success": True,
#                     "role": "hr",

#                     "hr_id": hr.hr_id,
#                     "name": f"{hr.first_name} {hr.last_name}",
#                     "email": hr.email,

#                     "message": "HR login successful."
#                 },
#                 status=status.HTTP_200_OK
#             )

#         # ---------- TRY EMPLOYER EMAIL ----------
#         employer = Employer.objects.filter(
#             email__iexact=identifier
#         ).first()

#         if employer:

#             if not employer.is_email_verified:
#                 return Response(
#                     {
#                         "error": "Employer account not verified."
#                     },
#                     status=status.HTTP_403_FORBIDDEN
#                 )

#             if not check_password(password, employer.password):
#                 return Response(
#                     {
#                         "error": "Invalid email or password."
#                     },
#                     status=status.HTTP_401_UNAUTHORIZED
#                 )

#             return Response(
#                 {
#                     "success": True,
#                     "role": "employer",

#                     "employer_id": employer.employer_id,
#                     "name": employer.name,
#                     "email": employer.email,
#                     "company_name": employer.company_name,

#                     "message": "Employer login successful."
#                 },
#                 status=status.HTTP_200_OK
#             )

#         return Response(
#             {
#                 "error": "Account not found."
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
    

# class HRProfileView(APIView):

#     def get(self, request, hr_id):

#         try:

#             hr = HR.objects.get(hr_id=hr_id)

#             serializer = HRProfileSerializer(hr)

#             return Response(
#                 {
#                     "success": True,
#                     "data": serializer.data
#                 },
#                 status=status.HTTP_200_OK
#             )

#         except HR.DoesNotExist:

#             return Response(
#                 {
#                     "error": "HR not found"
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         except Exception as e:

#             return Response(
#                 {
#                     "error": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        



# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import HR

# class HRDetailView(APIView):

#     def get(self, request, hr_id):

#         hr = get_object_or_404(HR, hr_id=hr_id)

#         students_count = hr.students.count()

#         return Response({
#             "hr_id": hr.hr_id,
#             "first_name": hr.first_name,
#             "last_name": hr.last_name,
#             "email": hr.email,
#             "phone": hr.phone,
#             "students_count": students_count,
#         })
    



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import StudentProfile, Employer, Payment
# from .serializers import StudentProfileSerializer

# class StudentListView(APIView):
#     def get(self, request):

#         employer_id = request.query_params.get("employer_id")

#         if not employer_id:
#             return Response(
#                 {"error": "Employer not identified."},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         try:
#             employer = Employer.objects.get(employer_id=employer_id)
#         except Employer.DoesNotExist:
#             return Response(
#                 {"error": "Employer not found."},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         # Match StudentProfile.pincode with Employer.company_pincode
#         students = StudentProfile.objects.filter(
#             pincode=employer.company_pincode
#         )

#         # Get student IDs this employer has already paid for
#         # (no status field on Payment model — all payment records = paid)
#         paid_student_ids = set(
#             Payment.objects.filter(
#                 employer=employer
#             ).values_list("student_id", flat=True)
#         )

#         serializer = StudentProfileSerializer(
#             students,
#             many=True,
#             context={"request": request}
#         )

#         data = []
#         for student, row in zip(students, serializer.data):
#             row = dict(row)
#             row["is_unlocked"] = student.id in paid_student_ids
#             data.append(row)

#         response_payload = {
#             "employer": {
#                 "employer_id":  employer.employer_id,
#                 "name":         employer.name,
#                 "company_name": employer.company_name,
#             },
#             "students": data,
#         }

#         return Response(response_payload)


# from .models import StudentProfile, Employer, Payment

# class PaymentConfirmView(APIView):
#     def post(self, request):

#         print("REQUEST DATA:", request.data)

#         employer_id  = request.data.get("employer_id")
#         reference_id = request.data.get("reference_id")
#         student_ids  = request.data.get("student_ids", [])

#         if not employer_id:
#             return Response(
#                 {"error": "employer_id is required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         if not reference_id:
#             return Response(
#                 {"error": "reference_id is required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         if not student_ids:
#             return Response(
#                 {"error": "student_ids is required."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             employer = Employer.objects.get(employer_id=employer_id)
#         except Employer.DoesNotExist:
#             return Response(
#                 {"error": "Employer not found."},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         created_count = 0
#         for sid in student_ids:
#             try:
#                 student = StudentProfile.objects.get(id=sid)
#                 # avoid duplicate payment records for same employer+student
#                 _, created = Payment.objects.get_or_create(
#                     employer=employer,
#                     student=student,
#                     defaults={
#                         "amount": 50,  # adjust if RATE_PER_PERSON differs
#                     }
#                 )
#                 if created:
#                     created_count += 1
#             except StudentProfile.DoesNotExist:
#                 continue  # skip invalid student IDs silently

#         return Response({
#             "success": True,
#             "message": f"{created_count} payment record(s) created.",
#             "employer_id": employer_id,
#             "reference_id": reference_id,
#             "student_ids": student_ids,
#         }, status=status.HTTP_201_CREATED)
    

 
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import StudentProfile, Employer, Payment
# from .serializers import StudentProfileSerializer
 
 
# def get_unlocked_ids(employer_id: str) -> set:
#     """Return the set of student PKs this employer has already paid for."""
#     try:
#         employer = Employer.objects.get(employer_id=employer_id)
#     except Employer.DoesNotExist:
#         return set()
#     return set(
#         Payment.objects
#         .filter(employer=employer)
#         .values_list("student_id", flat=True)
#     )
 
 
# # /api/students/filter/  — students matching employer's pincode
# class StudentListView(APIView):
#     def get(self, request):
 
#         employer_id = request.query_params.get("employer_id")
 
#         if not employer_id:
#             return Response(
#                 {"error": "Employer not identified."},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )
 
#         try:
#             employer = Employer.objects.get(employer_id=employer_id)
#         except Employer.DoesNotExist:
#             return Response(
#                 {"error": "Employer not found."},
#                 status=status.HTTP_404_NOT_FOUND
#             )
 
#         # Students in employer's pincode area
#         students = StudentProfile.objects.filter(
#             pincode=employer.company_pincode
#         )
 
#         # All student IDs this employer has paid for (across ALL students, not just pincode)
#         paid_student_ids = get_unlocked_ids(employer_id)
 
#         serializer = StudentProfileSerializer(
#             students,
#             many=True,
#             context={"request": request}
#         )
 
#         data = []
#         for student, row in zip(students, serializer.data):
#             row = dict(row)
#             row["is_unlocked"] = student.id in paid_student_ids
#             data.append(row)
 
#         return Response({
#             "employer": {
#                 "employer_id":  employer.employer_id,
#                 "name":         employer.name,
#                 "company_name": employer.company_name,
#             },
#             "students": data,
#         })
 
 
# # /api/students/  — ALL students across all locations
# class StudentListAllView(APIView):
#     def get(self, request):
 
#         # WITH this:
#         employer_id = request.query_params.get("employer_id")
#         hr_id       = request.query_params.get("hr_id")

#         if not employer_id and not hr_id:
#             return Response(
#                 {"error": "employer_id or hr_id is required."},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         students = StudentProfile.objects.all().order_by("-created_at")

#         # Unlock logic only applies to employers — HR sees all data unlocked
#         if employer_id:
#             try:
#                 Employer.objects.get(employer_id=employer_id)
#             except Employer.DoesNotExist:
#                 return Response({"error": "Employer not found."}, status=status.HTTP_404_NOT_FOUND)
#             paid_student_ids = get_unlocked_ids(employer_id)
#         else:
#             # HR users only see their own registered students
#             try:
#                 hr = HR.objects.get(hr_id=hr_id)
#             except HR.DoesNotExist:
#                 return Response({"error": "HR not found."}, status=status.HTTP_404_NOT_FOUND)
#             students = StudentProfile.objects.filter(id_no=hr_id).order_by("-created_at")
#             paid_student_ids = set(students.values_list("id", flat=True))  # all unlocked for HR

            
#         serializer = StudentProfileSerializer(
#             students,
#             many=True,
#             context={"request": request}
#         )
 
#         data = []
#         for student, row in zip(students, serializer.data):
#             row = dict(row)
#             row["is_unlocked"] = student.id in paid_student_ids
#             data.append(row)
 
#         return Response(data)
 
 
# # /api/hr/payment-confirm/
# class PaymentConfirmView(APIView):
#     def post(self, request):
 
#         print("REQUEST DATA:", request.data)
 
#         employer_id  = request.data.get("employer_id")
#         reference_id = request.data.get("reference_id")
#         student_ids  = request.data.get("student_ids", [])
 
#         if not employer_id:
#             return Response({"error": "employer_id is required."}, status=status.HTTP_400_BAD_REQUEST)
#         if not reference_id:
#             return Response({"error": "reference_id is required."}, status=status.HTTP_400_BAD_REQUEST)
#         if not student_ids:
#             return Response({"error": "student_ids is required."}, status=status.HTTP_400_BAD_REQUEST)
 
#         try:
#             employer = Employer.objects.get(employer_id=employer_id)
#         except Employer.DoesNotExist:
#             return Response({"error": "Employer not found."}, status=status.HTTP_404_NOT_FOUND)
 
#         created_count = 0
#         for sid in student_ids:
#             try:
#                 student = StudentProfile.objects.get(id=sid)
#                 _, created = Payment.objects.get_or_create(
#                     employer=employer,
#                     student=student,
#                     defaults={"amount": 50},
#                 )
#                 if created:
#                     created_count += 1
#             except StudentProfile.DoesNotExist:
#                 continue
 
#         return Response({
#             "success":      True,
#             "message":      f"{created_count} payment record(s) created.",
#             "employer_id":  employer_id,
#             "reference_id": reference_id,
#             "student_ids":  student_ids,
#         }, status=status.HTTP_201_CREATED)
 


# from django.http import HttpResponse, Http404
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import mm
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
# from reportlab.lib.enums import TA_LEFT, TA_CENTER
# from io import BytesIO
# from .models import StudentProfile

# def download_student_cv(request, student_id):
#     # Only allow unlocked access — verify employer
#     employer_id = request.GET.get("employer_id")
#     if not employer_id:
#         return HttpResponse("Unauthorized", status=401)

#     try:
#         student = StudentProfile.objects.get(pk=student_id)
#     except StudentProfile.DoesNotExist:
#         raise Http404

#     # ── Build PDF in memory ──────────────────────────────────────
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(
#         buffer, pagesize=A4,
#         leftMargin=20*mm, rightMargin=20*mm,
#         topMargin=20*mm, bottomMargin=20*mm
#     )

#     styles = getSampleStyleSheet()
#     BLUE   = colors.HexColor("#1D4ED8")
#     LBLUE  = colors.HexColor("#DBEAFE")
#     GRAY   = colors.HexColor("#64748B")
#     DARK   = colors.HexColor("#1E3A5F")

#     heading_style = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=20,
#                                    textColor=DARK, spaceAfter=2)
#     sub_style     = ParagraphStyle("s", fontName="Helvetica",      fontSize=11,
#                                    textColor=GRAY, spaceAfter=6)
#     section_style = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=11,
#                                    textColor=BLUE, spaceBefore=14, spaceAfter=6)
#     body_style    = ParagraphStyle("b", fontName="Helvetica", fontSize=10,
#                                    textColor=DARK, leading=16)

#     def section(title):
#         return [
#             Paragraph(title.upper(), section_style),
#             HRFlowable(width="100%", thickness=0.5, color=LBLUE, spaceAfter=6),
#         ]

#     def row(label, value):
#         """Two-column label/value row."""
#         return Table(
#             [[Paragraph(f"<b>{label}</b>", body_style),
#               Paragraph(value or "—", body_style)]],
#             colWidths=[55*mm, 115*mm],
#             style=TableStyle([
#                 ("VALIGN", (0,0), (-1,-1), "TOP"),
#                 ("BOTTOMPADDING", (0,0), (-1,-1), 3),
#             ])
#         )

#     # ── Field helpers ────────────────────────────────────────────
#     full_name = f"{student.surname or ''} {student.name or ''}".strip() or "—"
#     field = (student.core_spec_v1 or student.technical_v1
#              or student.non_tech_v1 or student.general_cat_v1 or "—")
#     exp   = f"{student.experience_years or '0'} yrs {student.experience_months or '0'} months"

#     story = []

#     # ── Header block ─────────────────────────────────────────────
#     story.append(Paragraph(full_name, heading_style))
#     # story.append(Paragraph(
#     #     f"{student.designation or 'Candidate'}  ·  {student.company_name or 'Fresher'}",
#     #     sub_style
#     # ))
#     story.append(Spacer(1, 4*mm))

#     # ── Personal details ─────────────────────────────────────────
#     story += section("Personal Details")
#     story.append(row("Date of Birth",   str(student.dob) if student.dob else "—"))
#     story.append(row("Father / Mother", student.father_mother_name))
#     story.append(row("Blood Group",     student.blood_group))
#     story.append(row("Address",
#         ", ".join(filter(None, [
#             student.h_no, student.street_colony,
#             student.area, student.district,
#             student.pincode
#         ])) or "—"
#     ))
#     story.append(row("Mobile",          student.mobile_personal))
#     story.append(row("Email",           student.email))

#     # ── Qualification ────────────────────────────────────────────
#     story += section("Qualification")
#     story.append(row("Academic",           student.academic))
#     story.append(row("Specialization",     student.specialization))
#     story.append(row("Additional Qual.",   student.additional_qualification))
#     story.append(row("Driving Licence",    student.driving_licence))
#     story.append(row("Extra Curricular",   student.extra_curricular))

#     # ── Experience ───────────────────────────────────────────────
#     story += section("Work Experience")
#     story.append(row("Experience",         exp))
#     story.append(row("Company",            student.company_name))
#     story.append(row("Designation",        student.designation))
#     story.append(row("Last Salary",        student.last_salary))
#     story.append(row("Reason for Leaving", student.reason_leaving))
#     story.append(row("Tech Stack",         student.tech_stack))

#     # ── Job Preferences ──────────────────────────────────────────
#     story += section("Job Preferences")
#     story.append(row("Interested Field",   field))
#     story.append(row("Job Type",           student.job_type))
#     story.append(row("Core Spec.",         student.core_spec_v1))
#     story.append(row("Technical",          student.technical_v1))
#     story.append(row("Non-Technical",      student.non_tech_v1))
#     story.append(row("Job Nature",         student.job_nature_v1))

#     doc.build(story)

#     buffer.seek(0)
#     safe_name = full_name.replace(" ", "_")
#     response = HttpResponse(buffer, content_type="application/pdf")
#     response["Content-Disposition"] = f'attachment; filename="CV_{safe_name}.pdf"'
#     return response







from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.hashers import check_password

import random
from io import BytesIO

from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

from .models import (
    ITI,
    UG_Courses,
    PG_Courses,
    Intermediate_Courses,
    Vocational_Courses,
    Polytechnic,
    Degree,
    HR,
    University,
    StudentProfile,
    InterviewQuestion,
    Employer,
    IndustrySector,
    Payment,
)
from .serializers import (
    ITISerializer,
    UGCoursesSerializer,
    PGCoursesSerializer,
    IntermediateCoursesSerializer,
    VocationalCoursesSerializer,
    PolytechnicSerializer,
    DegreeSerializer,
    HRProfileSerializer,
    HRSignupSerializer,
    StudentProfileSerializer,
    UniversitySerializer,
    EmployerSignupSerializer,
    IndustrySectorSerializer,
)
from .ai_utils import generate_ai_questions


# =========================================================
# COURSE VIEWS — ITI / UG / PG / POLYTECHNIC / INTERMEDIATE
#                VOCATIONAL / DEGREE
# =========================================================

class ITIListCreateView(generics.ListCreateAPIView):
    queryset = ITI.objects.all()
    serializer_class = ITISerializer

class ITIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ITI.objects.all()
    serializer_class = ITISerializer


class UGListCreateView(generics.ListCreateAPIView):
    queryset = UG_Courses.objects.all()
    serializer_class = UGCoursesSerializer

class UGDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UG_Courses.objects.all()
    serializer_class = UGCoursesSerializer


class PGListCreateView(generics.ListCreateAPIView):
    queryset = PG_Courses.objects.all()
    serializer_class = PGCoursesSerializer

class PGDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PG_Courses.objects.all()
    serializer_class = PGCoursesSerializer


class PolytechnicListCreateView(generics.ListCreateAPIView):
    queryset = Polytechnic.objects.all()
    serializer_class = PolytechnicSerializer

class PolytechnicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polytechnic.objects.all()
    serializer_class = PolytechnicSerializer


class IntermediateListCreateView(generics.ListCreateAPIView):
    queryset = Intermediate_Courses.objects.all()
    serializer_class = IntermediateCoursesSerializer

class IntermediateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intermediate_Courses.objects.all()
    serializer_class = IntermediateCoursesSerializer


class VocationalListCreateView(generics.ListCreateAPIView):
    queryset = Vocational_Courses.objects.all()
    serializer_class = VocationalCoursesSerializer

class VocationalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vocational_Courses.objects.all()
    serializer_class = VocationalCoursesSerializer


class DegreeListCreateView(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer

class DegreeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


# =========================================================
# STUDENT PROFILE VIEWSET  (single, fixed definition)
# =========================================================
from rest_framework.permissions import AllowAny

class StudentProfileViewSet(viewsets.ModelViewSet):

    queryset = StudentProfile.objects.all().order_by('-created_at')
    serializer_class = StudentProfileSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]  # ✅ fixes 401/403 since HR model has no token auth

    def get_queryset(self):
        hr_id = self.request.query_params.get("hr_id")
        if hr_id:
            return StudentProfile.objects.filter(hr__hr_id=hr_id).order_by('-created_at')
        return StudentProfile.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        hr_id = self.request.data.get("hr_id")
        if hr_id:
            hr = HR.objects.filter(hr_id=hr_id).first()
            if hr:
                serializer.save(
                    hr=hr,
                    hr_name=f"{hr.first_name} {hr.last_name}",
                    id_no=hr.hr_id
                )
                return
        serializer.save()

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
        InterviewQuestion.objects.filter(student=student).delete()
        questions = generate_ai_questions(student)
        for q in questions:
            InterviewQuestion.objects.create(student=student, question=q)
        return Response({
            "student_id": student.id,
            "student_name": student.name,
            "questions": questions
        })


# =========================================================
# HR SIGNUP / OTP / VERIFY
# =========================================================

class HRSignupView(APIView):

    def post(self, request):
        try:
            data = request.data
            email = data.get("email")

            if not email:
                return Response(
                    {"message": "Email is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            existing_hr = HR.objects.filter(email=email).first()

            if existing_hr:
                if existing_hr.is_verified:
                    return Response(
                        {"message": "Email already registered and verified"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                otp = str(random.randint(100000, 999999))
                existing_hr.otp = otp
                existing_hr.save()

                send_mail(
                    subject="Your OTP Verification Code",
                    message=f"""Hello {existing_hr.first_name},

Your new OTP verification code is: {otp}

Your HR ID is: {existing_hr.hr_id}

Thank You""",
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

            otp = str(random.randint(100000, 999999))

            university = None
            university_id = data.get("university")
            if university_id:
                university = University.objects.filter(id=university_id).first()

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

            send_mail(
                subject="Your OTP Verification Code",
                message=f"""Hello {hr.first_name},

Your OTP verification code is: {otp}

Your HR ID is: {hr.hr_id}

Thank You""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[hr.email],
                fail_silently=False,
            )

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
                {"message": "Signup failed", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class VerifyOTPView(APIView):

    def post(self, request):
        try:
            email = request.data.get("email", "").strip()
            otp   = request.data.get("otp",   "").strip()

            if not email or not otp:
                return Response(
                    {"error": "Email and OTP are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            hr = HR.objects.filter(email__iexact=email).order_by("-id").first()

            if not hr:
                return Response(
                    {"error": "User not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            print("DATABASE OTP :", hr.otp)
            print("ENTERED OTP  :", otp)
            print("BEFORE VERIFY:", hr.is_verified)

            if str(hr.otp).strip() != str(otp).strip():
                return Response(
                    {"error": "Invalid OTP"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            HR.objects.filter(id=hr.id).update(is_verified=True, otp="")
            hr.refresh_from_db()

            print("AFTER VERIFY :", hr.is_verified)

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
                {"message": "OTP verification failed", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class HRResendOTPView(APIView):

    def post(self, request):
        try:
            email = request.data.get("email")

            if not email:
                return Response(
                    {"error": "Email is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            hr = HR.objects.filter(email=email).first()

            if not hr:
                return Response(
                    {"error": "User not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            otp = str(random.randint(100000, 999999))
            hr.otp = otp
            hr.save()

            send_mail(
                subject="Resend OTP Verification Code",
                message=f"""Hello {hr.first_name},

Your new OTP verification code is: {otp}

Your HR ID is: {hr.hr_id}

Thank You""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[hr.email],
                fail_silently=False,
            )

            return Response(
                {"message": "OTP resent successfully", "otp_sent": True},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"message": "Failed to resend OTP", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class HRVerifyOTPView(APIView):

    def post(self, request):
        try:
            email = request.data.get("email")
            otp   = request.data.get("otp")

            if not email or not otp:
                return Response(
                    {"error": "Email and OTP are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            hr = HR.objects.filter(email__iexact=email.strip()).first()

            if not hr:
                return Response(
                    {"error": "HR user not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            if str(hr.otp).strip() != str(otp).strip():
                return Response(
                    {"error": "Invalid OTP"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            HR.objects.filter(id=hr.id).update(is_verified=True, otp="")

            return Response(
                {"message": "HR email verified successfully", "verified": True},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# =========================================================
# UNIVERSITIES
# =========================================================

@api_view(["GET"])
def get_universities(request):
    state = request.GET.get("state")
    if state:
        universities = University.objects.filter(state=state).order_by("name")
    else:
        universities = University.objects.all().order_by("name")
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data)


# =========================================================
# EMPLOYER — SEND OTP / VERIFY OTP / SIGNUP
# =========================================================

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
            message=f"""Your OTP is {otp}

Your Employer ID is {employer.employer_id}

Thank You""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )

        return Response({"message": "OTP sent successfully"})


class EmployerVerifyOTPView(APIView):

    def post(self, request):
        try:
            email = request.data.get("email")
            otp   = request.data.get("otp")

            if not email or not otp:
                return Response(
                    {"error": "Email and OTP are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            employer = Employer.objects.filter(email__iexact=email.strip()).first()

            if not employer:
                return Response(
                    {"error": "Employer not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            if not employer.otp_is_valid():
                return Response(
                    {"error": "OTP expired"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if str(employer.otp).strip() != str(otp).strip():
                return Response(
                    {"error": "Invalid OTP"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            employer.is_email_verified = True
            employer.otp = None
            employer.otp_created_at = None
            employer.save()

            return Response(
                {
                    "message": "Employer email verified successfully",
                    "verified": True,
                    "employer_id": employer.employer_id,
                    "email": employer.email
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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

        if not employer.is_email_verified:
            return Response(
                {"error": "Email is not verified"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmployerSignupSerializer(employer, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Employer account created successfully",
                "id": employer.id,
                "employer_id": employer.employer_id
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndustrySectorListView(APIView):

    def get(self, request):
        industries = IndustrySector.objects.all()
        serializer = IndustrySectorSerializer(industries, many=True)
        return Response(serializer.data)


# =========================================================
# SIGNIN  (HR / Employer — by ID or email)
# =========================================================

@api_view(["POST"])
def signin(request):
    identifier = request.data.get("identifier", "").strip()
    password   = request.data.get("password",   "").strip()

    if not identifier or not password:
        return Response(
            {"error": "ID/email and password are required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    identifier_upper = identifier.upper()

    # ── HR ID ────────────────────────────────────────────
    if identifier_upper.startswith("HR"):
        try:
            hr = HR.objects.get(hr_id__iexact=identifier)
        except HR.DoesNotExist:
            return Response(
                {"error": "Invalid HR ID or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not hr.is_verified:
            return Response(
                {"error": "HR account not verified."},
                status=status.HTTP_403_FORBIDDEN
            )

        if not check_password(password, hr.password):
            return Response(
                {"error": "Invalid HR ID or password."},
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

    # ── Employer ID ──────────────────────────────────────
    elif identifier_upper.startswith("EM"):
        try:
            employer = Employer.objects.get(employer_id__iexact=identifier)
        except Employer.DoesNotExist:
            return Response(
                {"error": "Invalid Employer ID or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not employer.is_email_verified:
            return Response(
                {"error": "Employer account not verified."},
                status=status.HTTP_403_FORBIDDEN
            )

        if not check_password(password, employer.password):
            return Response(
                {"error": "Invalid Employer ID or password."},
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

    # ── Email fallback ───────────────────────────────────
    else:
        hr = HR.objects.filter(email__iexact=identifier).first()

        if hr:
            if not hr.is_verified:
                return Response(
                    {"error": "HR account not verified."},
                    status=status.HTTP_403_FORBIDDEN
                )
            if not check_password(password, hr.password):
                return Response(
                    {"error": "Invalid email or password."},
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

        employer = Employer.objects.filter(email__iexact=identifier).first()

        if employer:
            if not employer.is_email_verified:
                return Response(
                    {"error": "Employer account not verified."},
                    status=status.HTTP_403_FORBIDDEN
                )
            if not check_password(password, employer.password):
                return Response(
                    {"error": "Invalid email or password."},
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
            {"error": "Account not found."},
            status=status.HTTP_404_NOT_FOUND
        )


# =========================================================
# HR PROFILE / DETAIL
# =========================================================

class HRProfileView(APIView):

    def get(self, request, hr_id):
        try:
            hr = HR.objects.get(hr_id=hr_id)
            serializer = HRProfileSerializer(hr)
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except HR.DoesNotExist:
            return Response({"error": "HR not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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


# =========================================================
# STUDENT LIST VIEWS  (single definition each)
# =========================================================

def get_unlocked_ids(employer_id: str) -> set:
    """Return the set of student PKs this employer has already paid for."""
    try:
        employer = Employer.objects.get(employer_id=employer_id)
    except Employer.DoesNotExist:
        return set()
    return set(
        Payment.objects
        .filter(employer=employer, status="success")
        .values_list("student_id", flat=True)
    )


# /api/students/filter/  — students matching employer's pincode
class StudentListView(APIView):

    def get(self, request):
        employer_id = request.query_params.get("employer_id")

        if not employer_id:
            return Response(
                {"error": "Employer not identified."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            employer = Employer.objects.get(employer_id=employer_id)
        except Employer.DoesNotExist:
            return Response(
                {"error": "Employer not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        students = StudentProfile.objects.filter(pincode=employer.company_pincode)
        paid_student_ids = get_unlocked_ids(employer_id)

        serializer = StudentProfileSerializer(
            students, many=True, context={"request": request}
        )

        data = []
        for student, row in zip(students, serializer.data):
            row = dict(row)
            row["is_unlocked"] = student.id in paid_student_ids
            data.append(row)

        return Response({
            "employer": {
                "employer_id":  employer.employer_id,
                "name":         employer.name,
                "company_name": employer.company_name,
            },
            "students": data,
        })


class StudentListAllView(APIView):

    def get(self, request):
        employer_id = request.query_params.get("employer_id")
        hr_id       = request.query_params.get("hr_id")

        if not employer_id and not hr_id:
            return Response(
                {"error": "employer_id or hr_id is required."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        employer = None  # ← always initialise so the final return never crashes

        if employer_id:
            try:
                employer = Employer.objects.get(employer_id=employer_id)
            except Employer.DoesNotExist:
                return Response(
                    {"error": "Employer not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            students = StudentProfile.objects.all().order_by("-created_at")

            paid_student_ids = set(
                Payment.objects.filter(
                    employer=employer,       # ← use object not pk, both work but this is cleaner
                    status="success"
                ).values_list("student_id", flat=True)
            )

            print(f"[DEBUG] employer={employer.employer_id}")
            print(f"[DEBUG] paid_student_ids={paid_student_ids}")

        else:
            try:
                hr = HR.objects.get(hr_id=hr_id)
            except HR.DoesNotExist:
                return Response(
                    {"error": "HR not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            students = StudentProfile.objects.filter(id_no=hr_id).order_by("-created_at")
            paid_student_ids = set(students.values_list("id", flat=True))

        serializer = StudentProfileSerializer(
            students, many=True, context={"request": request}
        )

        data = []
        for student, row in zip(students, serializer.data):
            row = dict(row)
            row["is_unlocked"] = student.id in paid_student_ids
            print(f"[DEBUG] student.id={student.id}  unlocked={row['is_unlocked']}")
            data.append(row)

        # just before return Response(...)
        print(f"[DEBUG] FINAL RESPONSE students count: {len(data)}")
        for row in data:
            if row["id"] in [128, 133]:
                print(f"[DEBUG] FINAL ROW: id={row['id']} is_unlocked={row['is_unlocked']}")

        # ── Same shape as StudentListView so frontend json.students parsing works ──
        return Response({
            "employer": {
                "employer_id":  employer.employer_id  if employer else "",
                "name":         employer.name         if employer else "",
                "company_name": employer.company_name if employer else "",
            },
            "students": data,
        })

# =========================================================
# PAYMENT CONFIRM  (single definition)
# =========================================================

class PaymentConfirmView(APIView):

    def post(self, request):
        print("REQUEST DATA:", request.data)

        employer_id  = request.data.get("employer_id")
        reference_id = request.data.get("reference_id")
        student_ids  = request.data.get("student_ids", [])
        

        if not employer_id:
            return Response({"error": "employer_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not reference_id:
            return Response({"error": "reference_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not student_ids:
            return Response({"error": "student_ids is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            employer = Employer.objects.get(employer_id=employer_id)
        except Employer.DoesNotExist:
            return Response({"error": "Employer not found."}, status=status.HTTP_404_NOT_FOUND)

        created_count = 0
        for sid in student_ids:
            try:
                student = StudentProfile.objects.get(id=sid)
                _, created = Payment.objects.get_or_create(
                    employer=employer,
                    student=student,
                    defaults={"amount": 50, "status": "success"},
                )
                if created:
                    created_count += 1
            except StudentProfile.DoesNotExist:
                continue

        return Response(
            {
                "success":      True,
                "message":      f"{created_count} payment record(s) created.",
                "employer_id":  employer_id,
                "reference_id": reference_id,
                "student_ids":  student_ids,
            },
            status=status.HTTP_201_CREATED
        )


# =========================================================
# STUDENT CV DOWNLOAD (PDF)
# =========================================================

def download_student_cv(request, student_id):
    employer_id = request.GET.get("employer_id")
    if not employer_id:
        return HttpResponse("Unauthorized", status=401)

    try:
        student = StudentProfile.objects.get(pk=student_id)
    except StudentProfile.DoesNotExist:
        raise Http404

    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=20*mm, bottomMargin=20*mm
    )

    styles = getSampleStyleSheet()
    BLUE  = colors.HexColor("#1D4ED8")
    LBLUE = colors.HexColor("#DBEAFE")
    GRAY  = colors.HexColor("#64748B")
    DARK  = colors.HexColor("#1E3A5F")

    heading_style = ParagraphStyle("h",   fontName="Helvetica-Bold", fontSize=20,
                                   textColor=DARK, spaceAfter=2)
    sub_style     = ParagraphStyle("s",   fontName="Helvetica",      fontSize=11,
                                   textColor=GRAY, spaceAfter=6)
    section_style = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=11,
                                   textColor=BLUE, spaceBefore=14, spaceAfter=6)
    body_style    = ParagraphStyle("b",   fontName="Helvetica",      fontSize=10,
                                   textColor=DARK, leading=16)

    def section(title):
        return [
            Paragraph(title.upper(), section_style),
            HRFlowable(width="100%", thickness=0.5, color=LBLUE, spaceAfter=6),
        ]

    def row(label, value):
        return Table(
            [[Paragraph(f"<b>{label}</b>", body_style),
              Paragraph(value or "—", body_style)]],
            colWidths=[55*mm, 115*mm],
            style=TableStyle([
                ("VALIGN",        (0, 0), (-1, -1), "TOP"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ])
        )

    full_name = f"{student.surname or ''} {student.name or ''}".strip() or "—"
    field = (student.core_spec_v1 or student.technical_v1
             or student.non_tech_v1 or student.general_cat_v1 or "—")
    exp   = f"{student.experience_years or '0'} yrs {student.experience_months or '0'} months"

    story = []

    story.append(Paragraph(full_name, heading_style))
    story.append(Spacer(1, 4*mm))

    story += section("Personal Details")
    story.append(row("Date of Birth",   str(student.dob) if student.dob else "—"))
    story.append(row("Father / Mother", student.father_mother_name))
    story.append(row("Blood Group",     student.blood_group))
    story.append(row("Address",
        ", ".join(filter(None, [
            student.h_no, student.street_colony,
            student.area, student.district,
            student.pincode
        ])) or "—"
    ))
    story.append(row("Mobile", student.mobile_personal))
    story.append(row("Email",  student.email))

    story += section("Qualification")
    story.append(row("Academic",           student.academic))
    story.append(row("Specialization",     student.specialization))
    story.append(row("Additional Qual.",   student.additional_qualification))
    story.append(row("Driving Licence",    student.driving_licence))
    story.append(row("Extra Curricular",   student.extra_curricular))

    story += section("Work Experience")
    story.append(row("Experience",         exp))
    story.append(row("Company",            student.company_name))
    story.append(row("Designation",        student.designation))
    story.append(row("Last Salary",        student.last_salary))
    story.append(row("Reason for Leaving", student.reason_leaving))
    story.append(row("Tech Stack",         student.tech_stack))

    story += section("Job Preferences")
    story.append(row("Interested Field", field))
    story.append(row("Job Type",         student.job_type))
    story.append(row("Core Spec.",       student.core_spec_v1))
    story.append(row("Technical",        student.technical_v1))
    story.append(row("Non-Technical",    student.non_tech_v1))
    story.append(row("Job Nature",       student.job_nature_v1))

    doc.build(story)

    buffer.seek(0)
    safe_name = full_name.replace(" ", "_")
    response = HttpResponse(buffer, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="CV_{safe_name}.pdf"'
    return response



from django.db.models import Sum

from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import status
from rest_framework.permissions import AllowAny

from .models import JobPosting
from .serializers import (
    BulkJobPostSerializer,
    JobBoardSerializer,
    JobPostingSerializer,
)


class PostJobsView(APIView):
    """
    POST /api/jobs/post/
    Body: { employer_id, jobs: [ {org, role, location, salary, available_jobs, description} ] }
    """
    permission_classes = [AllowAny]   # FIX: was IsAuthenticated → caused 403

    def post(self, request):
        print("REQUEST DATA:", request.data)
        ser = BulkJobPostSerializer(data=request.data)
        if not ser.is_valid():
            print("VALIDATION ERRORS:", ser.errors)
            return Response(
                {'error': ser.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
    

        # Optional guard: if a token employer_id exists, it must match payload
        payload_eid = ser.validated_data['employer_id']
        token_eid   = getattr(request.user, 'employer_id', None)
        if token_eid and str(token_eid) != str(payload_eid):
            return Response(
                {'error': 'Employer ID mismatch.'},
                status=status.HTTP_403_FORBIDDEN
            )

        created = ser.save()
        return Response(
            {
                'message': f'{len(created)} job(s) posted successfully.',
                'count': len(created)
            },
            status=status.HTTP_201_CREATED,
        )
    

class JobBoardView(APIView):
    """
    GET /api/jobs/board/
    Returns aggregated (org, role, n) list for the Index page JobGrid.
    Public – no auth required.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        qs = (
            JobPosting.objects
            .filter(is_active=True)
            .values('org', 'role')
            .annotate(n=Sum('vacancies'))
            .order_by('role', 'org')
        )
        ser = JobBoardSerializer(qs, many=True)
        return Response(ser.data)


class EmployerJobsView(APIView):
    """
    GET    /api/jobs/my/?employer_id=EM123   → list employer's own postings
    DELETE /api/jobs/my/<id>/                → deactivate a posting
    """
    permission_classes = [AllowAny]   # FIX: was IsAuthenticated → caused 403

    def get(self, request):
        eid = request.query_params.get('employer_id') or getattr(request.user, 'employer_id', None)

        if not eid:
            return Response(
                {'error': 'employer_id is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        qs  = JobPosting.objects.filter(employer_id=eid, is_active=True)
        ser = JobPostingSerializer(qs, many=True)
        return Response(ser.data)

    def delete(self, request, pk):
        try:
            jp = JobPosting.objects.get(pk=pk, is_active=True)
        except JobPosting.DoesNotExist:
            return Response(
                {'error': 'Not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Only block if a token employer_id exists AND it mismatches
        token_eid = str(getattr(request.user, 'employer_id', ''))
        if token_eid and token_eid != str(jp.employer_id):
            return Response(
                {'error': 'Forbidden.'},
                status=status.HTTP_403_FORBIDDEN
            )

        jp.is_active = False
        jp.save()
        return Response({'message': 'Job posting deactivated.'})



def perform_create(self, serializer):
    hr_id = self.request.data.get("hr_id")
    print("👉 hr_id received:", hr_id)  # ← add this
    print("👉 all data:", self.request.data)  # ← add this
    if hr_id:
        hr = HR.objects.filter(hr_id=hr_id).first()
        print("👉 HR found:", hr)
        if hr:
            serializer.save(
                hr=hr,
                hr_name=f"{hr.first_name} {hr.last_name}",
                id_no=hr.hr_id
            )
            return
    serializer.save()






import random
import string
import uuid
from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import HR, Employer

import json
from django.http import JsonResponse


_RESET_TOKENS: dict[str, dict] = {}


def _mask_email(email: str) -> str:
    try:
        local, domain = email.split("@", 1)
        masked_local = local[0] + "***" if len(local) > 1 else "***"
        return f"{masked_local}@{domain}"
    except Exception:
        return "***"


def _generate_otp(length: int = 6) -> str:
    return "".join(random.choices(string.digits, k=length))


def _find_user(identifier: str):
    identifier = identifier.strip()
    if identifier.upper().startswith("HR"):
        hr = HR.objects.filter(hr_id__iexact=identifier).first()
        if hr:
            return hr, "hr"
    if identifier.upper().startswith("EM"):
        emp = Employer.objects.filter(employer_id__iexact=identifier).first()
        if emp:
            return emp, "employer"
    hr = HR.objects.filter(email__iexact=identifier).first()
    if hr:
        return hr, "hr"
    emp = Employer.objects.filter(email__iexact=identifier).first()
    if emp:
        return emp, "employer"
    return None, None


def _send_otp_email(to_email: str, otp: str, user_type: str) -> None:
    label = "HR Portal" if user_type == "hr" else "Employer Portal"
    subject = "[HR Network] Your OTP for Password Reset"
    message = (
        f"Hello,\n\n"
        f"Your One-Time Password (OTP) for resetting your {label} account password is:\n\n"
        f"    {otp}\n\n"
        f"This OTP is valid for 5 minutes. Do not share it with anyone.\n\n"
        f"If you did not request this, please ignore this email.\n\n"
        f"— HR Network Team"
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@hrnetwork.com"),
        recipient_list=[to_email],
        fail_silently=False,
    )


@csrf_exempt
@require_POST
def send_otp(request):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)

    identifier = body.get("identifier", "").strip()
    if not identifier:
        return JsonResponse({"error": "identifier is required."}, status=400)

    user, user_type = _find_user(identifier)
    if user is None:
        return JsonResponse({"error": "No account found with that ID or email."}, status=404)

    email = getattr(user, "email", None)
    if not email:
        return JsonResponse({"error": "No email address associated with this account."}, status=400)

    otp = _generate_otp()
    user.otp = otp
    user.otp_created_at = timezone.now()
    user.save(update_fields=["otp", "otp_created_at"])

    try:
        _send_otp_email(email, otp, user_type)
    except Exception as exc:
        return JsonResponse({"error": f"Failed to send OTP email: {str(exc)}"}, status=500)

    return JsonResponse({
        "message": "OTP sent successfully.",
        "masked_email": _mask_email(email),
    })


@csrf_exempt
@require_POST
def verify_otp(request):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)

    identifier = body.get("identifier", "").strip()
    otp_input  = body.get("otp", "").strip()

    if not identifier or not otp_input:
        return JsonResponse({"error": "identifier and otp are required."}, status=400)

    user, user_type = _find_user(identifier)
    if user is None:
        return JsonResponse({"error": "Account not found."}, status=404)

    if not user.otp or user.otp != otp_input:
        return JsonResponse({"error": "Invalid OTP. Please try again."}, status=400)

    if not user.otp_is_valid():
        return JsonResponse({"error": "OTP has expired. Please request a new one."}, status=400)

    token = str(uuid.uuid4())
    _RESET_TOKENS[token] = {
        "identifier": identifier,
        "expires_at": timezone.now() + timedelta(minutes=10),
    }

    user.otp = None
    user.otp_created_at = None
    user.save(update_fields=["otp", "otp_created_at"])

    return JsonResponse({"message": "OTP verified.", "reset_token": token})


@csrf_exempt
@require_POST
def reset_password(request):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)

    identifier   = body.get("identifier", "").strip()
    reset_token  = body.get("reset_token", "").strip()
    new_password = body.get("new_password", "")

    if not identifier or not reset_token or not new_password:
        return JsonResponse({"error": "identifier, reset_token, and new_password are required."}, status=400)

    if len(new_password) < 6:
        return JsonResponse({"error": "Password must be at least 6 characters."}, status=400)

    token_data = _RESET_TOKENS.get(reset_token)
    if token_data is None:
        return JsonResponse({"error": "Invalid or expired reset token."}, status=400)

    if token_data["identifier"] != identifier:
        return JsonResponse({"error": "Token does not match the provided identifier."}, status=400)

    if timezone.now() > token_data["expires_at"]:
        _RESET_TOKENS.pop(reset_token, None)
        return JsonResponse({"error": "Reset token has expired. Please start over."}, status=400)

    user, user_type = _find_user(identifier)
    if user is None:
        return JsonResponse({"error": "Account not found."}, status=404)

    user.password = make_password(new_password)
    user.save(update_fields=["password"])

    _RESET_TOKENS.pop(reset_token, None)

    return JsonResponse({"message": "Password reset successfully."})

