from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import date


class Post(models.Model):
    YES = 'YES'
    NO = 'NO'
    YES_OR_NO_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    EXCELLENT = 'Excellent'
    VERYGOOD = 'Very Good'
    SATISFACTORY = 'Satisfactory'
    NEEDSIMPROVEMENT = 'Needs Improvement'
    STATUS_CHOICES = [
        (EXCELLENT, 'Excellent'),
        (VERYGOOD, 'Very Good'),
        (SATISFACTORY, 'Satisfactory'),
        (NEEDSIMPROVEMENT, 'Needs Improvement'),
    ]

    # Student Progress Report
    photo_main = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name="Add Photo of Student Interacting with Host Family below:", blank=True)
    coordinator = models.CharField(
        max_length=100, verbose_name="Coordinator :")

    date_of_contact = models.DateField(default=date.today)
    student_surname = models.CharField(
        max_length=100, verbose_name="Student's Surname :")
    hostfamily = models.CharField(
        max_length=100, verbose_name="Host Family Name :")
    student_eng_name = models.CharField(
        max_length=100, verbose_name="Student's English Name :")
    st_1 = models.CharField(max_length=50, choices=STATUS_CHOICES,
                            verbose_name="How are you getting along with your host family?", blank=True)
    st_1a = models.TextField(verbose_name="Comments :", blank=True)
    st_2 = models.TextField(
        verbose_name="Please Tell me about an experience you had this month at school that differs from last month (REQUIRED).", blank=True)
    st_3 = models.TextField(
        verbose_name="Please Tell me about an experience you had this month with your host family that differs from last month (REQUIRED).", blank=True)
    st_4 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Do you feel you are improving your conversational english?", blank=True)
    st_4a = models.TextField(
        blank=True, verbose_name="If yes, provide examples of how you have improved your conversational level of English:")
    st_4b = models.TextField(
        blank=True, verbose_name="If no, provide examples of areas you would like to improve upon to help strengthen your level of English:")
    st_5 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="* Have you made new American friends & interests in the community or school?", blank=True)
    st_5a = models.TextField(
        verbose_name="If yes, provide details:", blank=True)
    st_6 = models.CharField(max_length=20, choices=STATUS_CHOICES,
                            verbose_name="* How do you feel you are doing in school?", blank=True)
    st_6a = models.CharField(
        verbose_name="What is your favorite subject this month?", max_length=100, blank=True)
    st_6b = models.CharField(
        verbose_name="What subject are you having trouble with this month?", max_length=100, blank=True)
    st_7 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="* Did you experience any issues this month with your host family or at School?", blank=True)
    st_7a = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Is there anything you would like to talk about or need help with?", blank=True)
    st_7b = models.TextField(verbose_name="Student's Comments:", blank=True)
    st_coordinator_comments = models.TextField(
        verbose_name="Coordinator's comments re: Student's progress this month (REQUIRED):", blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(default=timezone.now)
    # Host Family Progress Report
    hf_hostfamily_name = models.CharField(
        max_length=100, verbose_name="HOST FAMILY'S LAST NAME", blank=True)
    hf_1 = models.CharField(max_length=20, choices=STATUS_CHOICES,
                            verbose_name="How is your relationship with your student?", blank=True)
    hf_1a = models.TextField(verbose_name="Comments :", blank=True)
    hf_2 = models.TextField(
        verbose_name="Please Tell me about an experience you had this month with your student that differs from last month (REQUIRED).", blank=True)
    hf_3 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="* Do you feel your student is improving his/her level of conversational english?", blank=True)
    hf_3a = models.TextField(
        verbose_name="If yes, provide examples of how your student has improved in this area:", blank=True)
    hf_3b = models.TextField(
        verbose_name="If no, provide examples of specific areas you feel your student can improve upon to help strengthen his/her level of English:", blank=True)
    hf_4 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Has your student interacted with your family this month?", blank=True)
    hf_4a = models.TextField(
        verbose_name="If yes, provide examples of how your student interacted with your family this month:", blank=True)
    hf_4b = models.TextField(
        verbose_name="If no, provide examples of how your student can better interact with your family:", blank=True)
    hf_5 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Has your student made plans with any American friends or shown any interest in events in the community?", blank=True)
    hf_5a = models.TextField(
        verbose_name="If yes, please provide details:", blank=True)
    hf_6 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Does your student obey the rules at home this month?", blank=True)
    hf_6a = models.TextField(
        verbose_name="If no, please provide details so MAH can counsel the student to better improve in this area:", blank=True)
    hf_7 = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name="Rate your hosting experience so far:", blank=True)
    hf_7a = models.TextField(
        verbose_name="Host Family's Comments :", blank=True)
    hf_coordinator_comments = models.TextField(
        verbose_name="Coordinator's comments re: Host Family progress this month (REQUIRED):", blank=True)
    # School Progress Report
    sch_school_name = models.CharField(
        verbose_name="SCHOOL'S NAME", max_length=50, blank=True)
    sch_student_name = models.CharField(
        verbose_name="Student's Name", max_length=100, blank=True)
    sch_1a = models.CharField(
        verbose_name="School Contact's Name:", max_length=100, blank=True)
    sch_1b = models.CharField(
        verbose_name="School Contact's Title", max_length=100, blank=True)
    sch_2 = models.CharField(max_length=20, choices=STATUS_CHOICES,
                             verbose_name="What is the school's impression of the student's academic performance this month?", blank=True)
    sch_2a = models.TextField(
        verbose_name="School's feedback about student's academic performance this month:", blank=True)
    sch_3 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Has the student had any accomplishments (e.g., honor roll, athletics, club participation)?", blank=True)
    sch_3a = models.TextField(
        verbose_name="Please list details re: accomplishments:", blank=True)
    sch_4 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Has the student missed any days from school", blank=True)
    sch_4a = models.IntegerField(default=0, verbose_name="# of Days Missed")
    sch_4b = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Were these excused absences?", blank=True)
    sch_4c = models.TextField(
        verbose_name="School's Comments re: student's attendance:", blank=True)
    sch_5 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Does the student need additional help at school, such as tutoring, or is there any area(s) MAH can counsel the student to help him/her improve in this area?", blank=True)
    sch_5a = models.CharField(
        max_length=100, verbose_name="School's Comments re:", blank=True)
    sch_6 = models.CharField(
        max_length=10, choices=YES_OR_NO_CHOICES, verbose_name="Is the student receiving a 'C' or better in each class?", blank=True)
    sch_classes_grades = models.TextField(
        verbose_name="List all classes & current grades this month below.", blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.coordinator

    def save(self):
        super().save()

        img = Image.open(self.photo_main.path)

    def get_absolute_url(self):
        return reverse('post_receipt', kwargs={'pk': self.pk})
