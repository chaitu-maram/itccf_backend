# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from threading import Thread

# from .models import StudentProfile, InterviewQuestion
# from .ai_utils import generate_questions


# def generate_and_save(student):
#     # delete old questions
#     InterviewQuestion.objects.filter(student=student).delete()

#     questions = generate_questions(student)

#     for q in questions:
#         InterviewQuestion.objects.create(student=student, question=q)


# @receiver(post_save, sender=StudentProfile)
# def auto_generate_questions(sender, instance, created, **kwargs):
#     # run in background so API is fast
#     Thread(target=generate_and_save, args=(instance,)).start()