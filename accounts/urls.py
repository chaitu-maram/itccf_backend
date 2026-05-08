from django.urls import path
from .views import *

urlpatterns = [

    # ITI
    path('iti/', ITIListCreateView.as_view()),
    path('iti/<int:pk>/', ITIDetailView.as_view()),

    # UG
    path('ug/', UGListCreateView.as_view()),
    path('ug/<int:pk>/', UGDetailView.as_view()),

    # PG
    path('pg/', PGListCreateView.as_view()),
    path('pg/<int:pk>/', PGDetailView.as_view()),

    #polytechnic
    path('polytechnic/', PolytechnicListCreateView.as_view()),
    path('polytechnic/<int:pk>/', PolytechnicDetailView.as_view()),
    
    # Intermediate
    path('intermediate/', IntermediateListCreateView.as_view()),
    path('intermediate/<int:pk>/', IntermediateDetailView.as_view()),

    # Vocational
    path('vocational/', VocationalListCreateView.as_view()),
    path('vocational/<int:pk>/', VocationalDetailView.as_view()),

    #degree
    path('degree/', DegreeListCreateView.as_view()),
    path('degree/<int:pk>/', DegreeDetailView.as_view()),
]