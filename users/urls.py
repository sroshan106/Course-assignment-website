from django.urls import path

from .views import Student_Signup_View,Teacher_Signup_View,login,logout
app_name='users'

urlpatterns=[
        path('signup-student/',Student_Signup_View.as_view(),name='Student-Signup'),
        path('signup-teacher/',Teacher_Signup_View.as_view(),name='Teacher-Signup'),
        path('login/',login,name='login'),
        path('logout/',logout,name='logout'),
]