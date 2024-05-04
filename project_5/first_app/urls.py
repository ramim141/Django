# from django.urls import path, include
# from .import views

# urlpatterns = [
#     path('', views.index, name = 'home'),
#     path('about/', views.about, name = 'about'),
#     path('form/', views.submit_form, name = 'submit_form'),
#     path('django_form/', views.Djangoform, name = 'django_form'),
#     path('student/', views.StudentForm, name = 'student'),
#     # path('student/', views.StudentForm, name='student'),
#     # path('student/', student_view, name='student')

    
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.submit_form, name='submit_form'),
    path('django_form/', views.Djangoform, name='django_form'),
    # path('student/', views.student_form_view, name='student_form'),
    path('student/', views.PasswordForm, name='student_form'),
]
