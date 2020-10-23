from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager
class MyAccountManager(BaseUserManager):


    def create_user(self,username,roll_no,dob,email,password=None):

        if not username :
            raise ValueError('You have entered invalid details !')

        user = self.model(      # here we called self.model
            username= username,
            roll_no = roll_no,
            dob=dob,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,roll_no,dob,email,password):
        user = self.create_user(
            username= username,
            roll_no=roll_no,
            dob=dob,
            email=email,
            password=password,
        )
        user.is_admin =True
        user.is_staff = True
        user.is_superuser=True
        user.is_student = True
        user.is_teacher = True
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    username = models.CharField(max_length=30)
    roll_no=models.IntegerField()
    dob=models.DateField(verbose_name='Date_of_Birth')
    email=models.EmailField(blank=True,null=True,unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','dob','roll_no']

    objects = MyAccountManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True