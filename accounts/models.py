from django.db import models

# Create your models here.
from django.db import models

class ITI(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class UG_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class PG_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class Intermediate_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"


class Vocational_Courses(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"
    


class Degree(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()
    sub_course = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization} - {self.sub_course}"
    

class Polytechnic(models.Model):
    academic = models.CharField(max_length=100)
    specialization = models.TextField()

    def __str__(self):
        return f"{self.academic} - {self.specialization}"
    



from django.db import models

class StudentProfile(models.Model):

    # HR Information
    hr_name = models.CharField(max_length=100, blank=True, null=True)
    id_no = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    logins_count = models.IntegerField(blank=True, null=True)
    percentage_obtained = models.FloatField(blank=True, null=True)
    success_rate = models.FloatField(blank=True, null=True)
    hr_photo = models.ImageField(upload_to='hr_photos/', blank=True, null=True)

    # Candidate Details
    surname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    father_mother_name = models.CharField(max_length=150, blank=True, null=True)

    dob = models.DateField(blank=True, null=True)

    regn_no = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    # Qualification
    academic = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=150, blank=True, null=True)
    extra_curricular = models.CharField(max_length=100, blank=True, null=True)
    additional_qualification = models.CharField(max_length=150, blank=True, null=True)
    driving_licence = models.CharField(max_length=50, blank=True, null=True)

    # Contact & Identity
    aadhar_no = models.CharField(max_length=14, blank=True, null=True)
    mobile_personal = models.CharField(max_length=15, blank=True, null=True)
    mobile_reference = models.CharField(max_length=15, blank=True, null=True)

    # Address
    h_no = models.CharField(max_length=50, blank=True, null=True)
    street_colony = models.CharField(max_length=150, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    house_own_rent = models.CharField(max_length=20, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    reservation = models.CharField(max_length=50, blank=True, null=True)

    # Physical Info
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    eye_site = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    any_job = models.CharField(max_length=10, blank=True, null=True)

    # Experience
    experience_years = models.CharField(max_length=20, blank=True, null=True)
    experience_months = models.CharField(max_length=20, blank=True, null=True)

    company_name = models.CharField(max_length=150, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    last_salary = models.CharField(max_length=50, blank=True, null=True)
    reason_leaving = models.TextField(blank=True, null=True)
    job_type = models.CharField(max_length=50, blank=True, null=True)
    tech_stack = models.TextField(blank=True, null=True)

    # Job Preferences
    core_spec_checked = models.BooleanField(default=False)
    core_spec_v1 = models.CharField(max_length=150, blank=True, null=True)
    core_spec_v2 = models.CharField(max_length=150, blank=True, null=True)

    technical_checked = models.BooleanField(default=False)
    technical_v1 = models.CharField(max_length=150, blank=True, null=True)
    technical_v2 = models.CharField(max_length=150, blank=True, null=True)

    non_tech_checked = models.BooleanField(default=False)
    non_tech_v1 = models.CharField(max_length=150, blank=True, null=True)
    non_tech_v2 = models.CharField(max_length=150, blank=True, null=True)

    general_cat_checked = models.BooleanField(default=False)
    general_cat_v1 = models.CharField(max_length=150, blank=True, null=True)
    general_cat_v2 = models.CharField(max_length=150, blank=True, null=True)

    job_nature_checked = models.BooleanField(default=False)
    job_nature_v1 = models.CharField(max_length=150, blank=True, null=True)
    job_nature_v2 = models.CharField(max_length=150, blank=True, null=True)

    # Signature
    digital_signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    questions_ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name or 'No Name'} ({self.regn_no or 'No Reg'})"
    
    


class InterviewQuestion(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()

    def __str__(self):
        return self.question[:50]
    



class University(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
from django.db import models


class HR(models.Model):
    CURRENT_YEAR_CHOICES = [
        ("1st Year", "1st Year"),
        ("2nd Year", "2nd Year"),
        ("3rd Year", "3rd Year"),
        ("4th Year", "4th Year"),
        ("5th Year", "5th Year"),
        ("Graduated", "Graduated"),
    ]

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    # DD-MM-YYYY
    dob = models.CharField(max_length=20, blank=True, null=True)

    college_code = models.CharField(max_length=100, blank=True, null=True)
    college_name = models.CharField(max_length=255, blank=True, null=True)

    roll_number = models.CharField(max_length=100, blank=True, null=True)

    current_year = models.CharField(
        max_length=20,
        choices=CURRENT_YEAR_CHOICES,
        blank=True,
        null=True
    )

    college_state = models.CharField(max_length=100, blank=True, null=True)
    college_city = models.CharField(max_length=100, blank=True, null=True)

    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    password = models.CharField(max_length=255, blank=True, null=True)

    # OTP
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey(
        University,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

