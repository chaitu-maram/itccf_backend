# # from django.urls import path
# # from .views import *
# # from rest_framework.routers import DefaultRouter
# # from .views import StudentProfileViewSet
# # from django.urls import include
# # from .views import HRSignupView, VerifyOTPView, get_universities, signin
# # from .views import (
# #     SendOTPView,
# #     VerifyOTPView,
# #     EmployerSignupView,
# #     IndustrySectorListView
# # )

# # router = DefaultRouter()
# # router.register(r'students', StudentProfileViewSet)



# # from rest_framework.routers import DefaultRouter
# # from .views import StudentProfileViewSet

# # router = DefaultRouter()
# # router.register(r'students', StudentProfileViewSet)

# # urlpatterns = router.urls

# # urlpatterns = [

# #     # ITI
# #     path('iti/', ITIListCreateView.as_view()),
# #     path('iti/<int:pk>/', ITIDetailView.as_view()),

# #     # UG
# #     path('ug/', UGListCreateView.as_view()),
# #     path('ug/<int:pk>/', UGDetailView.as_view()),

# #     # PG
# #     path('pg/', PGListCreateView.as_view()),
# #     path('pg/<int:pk>/', PGDetailView.as_view()),

# #     #polytechnic
# #     path('polytechnic/', PolytechnicListCreateView.as_view()),
# #     path('polytechnic/<int:pk>/', PolytechnicDetailView.as_view()),

# #     # Intermediate
# #     path('intermediate/', IntermediateListCreateView.as_view()),
# #     path('intermediate/<int:pk>/', IntermediateDetailView.as_view()),

# #     # Vocational
# #     path('vocational/', VocationalListCreateView.as_view()),
# #     path('vocational/<int:pk>/', VocationalDetailView.as_view()),

# #     #degree
# #     path('degree/', DegreeListCreateView.as_view()),
# #     path('degree/<int:pk>/', DegreeDetailView.as_view()),

# #     path('', include(router.urls)),


# #     path("hr/signup/", HRSignupView.as_view()),
# #     path("hr/verify-otp/", VerifyOTPView.as_view()),
# #     path("universities/", get_universities),
# #     path(
# #         "hr/resend-otp/",
# #         HRResendOTPView.as_view(),
# #         name="resend-otp"
# #     ),



# #     path(
# #         "employer/send-otp/",
# #         SendOTPView.as_view()
# #     ),

# #     path(
# #         "employer/verify-otp/",
# #         VerifyOTPView.as_view()
# #     ),

# #     path(
# #         "employer/signup/",
# #         EmployerSignupView.as_view()
# #     ),

# #     path(
# #         "industries/",
# #         IndustrySectorListView.as_view()
# #     ),
# #     path("signin/", signin, name="signin"),

    
# # ]



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from .views import *

# # =========================
# # ROUTER
# # =========================
# router = DefaultRouter()
# router.register(r"students", StudentProfileViewSet)

# # =========================
# # URL PATTERNS
# # =========================
# urlpatterns = [

#     path("students/filter/", StudentListView.as_view(), name="student-list-filtered"),


#     # =========================
#     # STUDENTS
#     # =========================
#     path("", include(router.urls)),

#     # =========================
#     # ITI
#     # =========================
#     path("iti/", ITIListCreateView.as_view()),
#     path("iti/<int:pk>/", ITIDetailView.as_view()),

#     # =========================
#     # UG
#     # =========================
#     path("ug/", UGListCreateView.as_view()),
#     path("ug/<int:pk>/", UGDetailView.as_view()),

#     # =========================
#     # PG
#     # =========================
#     path("pg/", PGListCreateView.as_view()),
#     path("pg/<int:pk>/", PGDetailView.as_view()),

#     # =========================
#     # POLYTECHNIC
#     # =========================
#     path("polytechnic/", PolytechnicListCreateView.as_view()),
#     path("polytechnic/<int:pk>/", PolytechnicDetailView.as_view()),

#     # =========================
#     # INTERMEDIATE
#     # =========================
#     path("intermediate/", IntermediateListCreateView.as_view()),
#     path("intermediate/<int:pk>/", IntermediateDetailView.as_view()),

#     # =========================
#     # VOCATIONAL
#     # =========================
#     path("vocational/", VocationalListCreateView.as_view()),
#     path("vocational/<int:pk>/", VocationalDetailView.as_view()),

#     # =========================
#     # DEGREE
#     # =========================
#     path("degree/", DegreeListCreateView.as_view()),
#     path("degree/<int:pk>/", DegreeDetailView.as_view()),

#     # =========================================================
#     # HR ROUTES
#     # =========================================================
#     path(
#         "hr/signup/",
#         HRSignupView.as_view(),
#         name="hr-signup"
#     ),

#     path(
#         "hr/verify-otp/",
#         HRVerifyOTPView.as_view(),
#         name="hr-verify-otp"
#     ),

#     path(
#         "hr/resend-otp/",
#         HRResendOTPView.as_view(),
#         name="hr-resend-otp"
#     ),

#     # =========================================================
#     # EMPLOYER ROUTES
#     # =========================================================
#     path(
#         "employer/send-otp/",
#         SendOTPView.as_view(),
#         name="employer-send-otp"
#     ),

#     path(
#         "employer/verify-otp/",
#         EmployerVerifyOTPView.as_view(),
#         name="employer-verify-otp"
#     ),

#     path(
#         "employer/signup/",
#         EmployerSignupView.as_view(),
#         name="employer-signup"
#     ),

#     # =========================================================
#     # COMMON
#     # =========================================================
#     path(
#         "universities/",
#         get_universities,
#         name="universities"
#     ),

#     path(
#         "industries/",
#         IndustrySectorListView.as_view(),
#         name="industries"
#     ),

#     path(
#         "signin/",
#         signin,
#         name="signin"
#     ),
#     path(
#     "hr/profile/<str:hr_id>/",
#     HRProfileView.as_view(),
# ),
# path("hr/<str:hr_id>/", HRDetailView.as_view()),
# path(
#     "hr/<str:hr_id>/",
#     HRDetailView.as_view(),
#     name="hr-detail"
# ),
# path("api/hr/payment-confirm/", PaymentConfirmView.as_view()),
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# =========================
# ROUTER
# =========================
router = DefaultRouter()
router.register(r"students", StudentProfileViewSet)

# =========================
# URL PATTERNS
# =========================
urlpatterns = [

    # =========================
    # STUDENTS
    # =========================
    path("students/filter/", StudentListView.as_view(), name="student-list-filtered"),
    path("", include(router.urls)),

    # =========================
    # ITI
    # =========================
    path("iti/", ITIListCreateView.as_view()),
    path("iti/<int:pk>/", ITIDetailView.as_view()),

    # =========================
    # UG
    # =========================
    path("ug/", UGListCreateView.as_view()),
    path("ug/<int:pk>/", UGDetailView.as_view()),

    # =========================
    # PG
    # =========================
    path("pg/", PGListCreateView.as_view()),
    path("pg/<int:pk>/", PGDetailView.as_view()),

    # =========================
    # POLYTECHNIC
    # =========================
    path("polytechnic/", PolytechnicListCreateView.as_view()),
    path("polytechnic/<int:pk>/", PolytechnicDetailView.as_view()),

    # =========================
    # INTERMEDIATE
    # =========================
    path("intermediate/", IntermediateListCreateView.as_view()),
    path("intermediate/<int:pk>/", IntermediateDetailView.as_view()),

    # =========================
    # VOCATIONAL
    # =========================
    path("vocational/", VocationalListCreateView.as_view()),
    path("vocational/<int:pk>/", VocationalDetailView.as_view()),

    # =========================
    # DEGREE
    # =========================
    path("degree/", DegreeListCreateView.as_view()),
    path("degree/<int:pk>/", DegreeDetailView.as_view()),

    # =========================================================
    # HR ROUTES — specific paths MUST come before hr/<str:hr_id>/
    # =========================================================
    path("hr/signup/",        HRSignupView.as_view(),      name="hr-signup"),
    path("hr/verify-otp/",    HRVerifyOTPView.as_view(),   name="hr-verify-otp"),
    path("hr/resend-otp/",    HRResendOTPView.as_view(),   name="hr-resend-otp"),
    path("hr/profile/<str:hr_id>/", HRProfileView.as_view(), name="hr-profile"),

    # ↓↓↓ payment-confirm MUST be before hr/<str:hr_id>/ catch-all ↓↓↓
    path("hr/payment-confirm/", PaymentConfirmView.as_view(), name="hr-payment-confirm"),

    # ↓ catch-all — always keep this LAST among hr/ routes ↓
    path("hr/<str:hr_id>/",   HRDetailView.as_view(),      name="hr-detail"),

    # =========================================================
    # EMPLOYER ROUTES
    # =========================================================
    path("employer/send-otp/",   SendOTPView.as_view(),           name="employer-send-otp"),
    path("employer/verify-otp/", EmployerVerifyOTPView.as_view(), name="employer-verify-otp"),
    path("employer/signup/",     EmployerSignupView.as_view(),    name="employer-signup"),

    # =========================================================
    # COMMON
    # =========================================================
    path("universities/", get_universities,              name="universities"),
    path("industries/",   IndustrySectorListView.as_view(), name="industries"),
    path("signin/",       signin,                        name="signin"),
]