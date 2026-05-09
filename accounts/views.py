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