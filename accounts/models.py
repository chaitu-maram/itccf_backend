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
    # hr_photo = models.ImageField(upload_to='hr_photos/', blank=True, null=True)

    # Candidate Details
    surname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    father_mother_name = models.CharField(max_length=150, blank=True, null=True)

    dob = models.DateField(blank=True, null=True)

    regn_no = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    # photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

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
    # digital_signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    hr_photo = models.ImageField(upload_to='hr_photos/', blank=True, null=True)

    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    digital_signature = models.ImageField(upload_to='signatures/', blank=True, null=True)
    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    questions_ready = models.BooleanField(default=False)

    score = models.FloatField(default=0)

    hr = models.ForeignKey(
    "HR",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="students"
)
    pincode = models.CharField(max_length=6, blank=True, null=True)

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


from django.db import models
from django.utils import timezone


class HR(models.Model):

    CURRENT_YEAR_CHOICES = [
        ("1st Year", "1st Year"),
        ("2nd Year", "2nd Year"),
        ("3rd Year", "3rd Year"),
        ("4th Year", "4th Year"),
        ("5th Year", "5th Year"),
        ("Graduated", "Graduated"),
    ]

    # CUSTOM HR ID
    hr_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

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

    email = models.EmailField(
        unique=True,
        blank=True,
        null=True
    )

    password = models.CharField(max_length=255, blank=True, null=True)

    # OTP
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    university = models.ForeignKey(
        "University",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def otp_is_valid(self):
        if not self.otp or not self.otp_created_at:
            return False
        from datetime import timedelta
        from django.utils import timezone
        return timezone.now() <= self.otp_created_at + timedelta(minutes=5)

    def save(self, *args, **kwargs):

        # GENERATE HR ID ONLY IF EMPTY
        if not self.hr_id:

            today = timezone.now().strftime("%d%m%y")

            # COUNT TODAY'S RECORDS
            today_count = HR.objects.filter(
                created_at__date=timezone.now().date()
            ).count() + 1

            # FORMAT:
            # HR1205260001
            self.hr_id = f"HR{today}{today_count:04d}"
        if self.password and not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
    

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hr_id} - {self.first_name} {self.last_name}"
    


from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import timedelta


class IndustrySector(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name





from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import timedelta


class Employer(models.Model):

    # =========================
    # EMPLOYER ID
    # =========================
    employer_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    name = models.CharField(max_length=255)

    designation = models.CharField(max_length=255)

    contact_number = models.CharField(max_length=10)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)

    company_name = models.CharField(max_length=255)

    company_industry = models.ForeignKey(
        IndustrySector,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    company_address_line1 = models.TextField()

    company_address_line2 = models.TextField(
        blank=True,
        null=True
    )

    company_city = models.CharField(max_length=255)

    company_state = models.CharField(max_length=255)

    company_pincode = models.CharField(max_length=6)

    manufacturing_activity = models.TextField(
        blank=True,
        null=True
    )

    otp = models.CharField(
        max_length=6,
        blank=True,
        null=True
    )

    otp_created_at = models.DateTimeField(
        blank=True,
        null=True
    )

    is_email_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    # =========================
    # SAVE METHOD
    # =========================
    def save(self, *args, **kwargs):

        # =========================
        # GENERATE EMPLOYER ID
        # =========================
        if not self.employer_id:

            today = timezone.now().strftime("%d%m%y")

            # COUNT TODAY RECORDS
            today_count = Employer.objects.filter(
                created_at__date=timezone.now().date()
            ).count() + 1

            # FORMAT:
            # EM1605260001
            self.employer_id = f"EM{today}{today_count:04d}"

        # =========================
        # HASH PASSWORD
        # =========================
        if self.password and not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    # =========================
    # OTP VALIDATION
    # =========================
    def otp_is_valid(self):

        if not self.otp or not self.otp_created_at:
            return False

        expiry_time = self.otp_created_at + timedelta(minutes=5)

        return timezone.now() <= expiry_time

    def __str__(self):
        return f"{self.employer_id} - {self.company_name}"
    

# models.py
class Payment(models.Model):
    employer    = models.ForeignKey(Employer, on_delete=models.CASCADE)
    student     = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    amount      = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("success", "Success"), ("failed", "Failed")],
        default="success"   # set to "pending" if you want manual confirmation
    )

class JobPosting(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name="job_postings",
        null=True,      # add this
        blank=True      # add this
    )
    role = models.CharField(max_length=150)
    org = models.CharField(max_length=150)
    vacancies = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} at {self.org}"