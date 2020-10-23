from django import forms

class Student_Signup(forms.Form):
    email=forms.EmailField()
    username=forms.CharField(max_length=50)
    dob= forms.DateField()
    roll_no=forms.IntegerField()
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

class Teacher_Signup(forms.Form):
    email=forms.EmailField()
    username=forms.CharField(max_length=50)
    dob= forms.DateField()
    id_number=forms.IntegerField()
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)