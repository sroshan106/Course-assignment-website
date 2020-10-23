from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Examinations(models.Model):
    Name=models.CharField(max_length=50)
    questions=models.ManyToManyField('Questions')
    slug = models.SlugField(unique=True)

    def get_abs_url(self):
        return reverse(viewname="Tester:exam-page",
                       kwargs={
                           'slug': self.slug
                       })
class Questions(models.Model):
    ques=models.TextField(max_length=1000)
    answer=models.TextField(max_length=1000)
    option1=models.TextField(max_length=1000)
    option2=models.TextField(max_length=1000)
    option3=models.TextField(max_length=1000)
    option4=models.TextField(max_length=1000)
    correct=models.BooleanField(default=False)
    wrong=models.BooleanField(default=False)
    slug=models.SlugField(unique=True)
#     Answer_check=models.ForeignKey('Answer_Checkbox',on_delete=models.CASCADE,blank=True,null=True)
#     Answer_radio = models.ForeignKey('Answer_Radio', on_delete=models.CASCADE, blank=True, null=True)
#
# class Answer_Checkbox(models.Model):
#
# class Answer_Radio(models.Model):
#     pass