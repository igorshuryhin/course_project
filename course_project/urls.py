"""
URL configuration for course_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from courses.viewsets import CourseViewSet
from orders.viewsets import OrderViewSet
from homework.viewsets import HomeworkViewSet
from lesson.viewsets import LessonViewSet, AttendanceViewSet
from awards.viewsets import AwardViewSet
from vacancies.viewsets import VacancyViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'homeworks', HomeworkViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'vacancies', VacancyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', authtoken_views.obtain_auth_token),
]
