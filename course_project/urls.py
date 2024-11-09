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
from allauth.account.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import routers, permissions
from rest_framework.authtoken import views as authtoken_views

from course_project.views import index
from courses.viewsets import CourseViewSet
from orders.viewsets import OrderViewSet
from homework.viewsets import HomeworkViewSet
from lesson.viewsets import LessonViewSet, AttendanceViewSet
from awards.viewsets import AwardViewSet
from telegram.views import telegram
from vacancies.viewsets import VacancyViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="LMS API",
      default_version='v1',
      description="LMS Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="igor@igor.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


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
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('telegram', telegram),
    path("accounts/", include("allauth.urls")),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("", index, name="index"),
]
