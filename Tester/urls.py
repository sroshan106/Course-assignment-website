from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import  Homepage,Exampage
app_name='Tester'

urlpatterns=[
        path('',Homepage,name='Homepage'),
        path('Exampage/<slug>/',Exampage,name='exam-page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)