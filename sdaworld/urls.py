"""sdaworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from accounts.views import SubmittableLoginView, SignUpView
from blog.views import PostView, PostNew, PostUpdate
from courses.models import Course, Technology
from courses.views import hello, CourseCreateView, CourseView
from blog.models import Post, Comment
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(Technology)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', PostView.as_view(), name='index'),
    path('post/create', PostNew.as_view(), name='post_new'),
    path('update/<pk>', PostUpdate.as_view(), name='post_update'),
    path('course/create', CourseCreateView.as_view(), name='course_create'),
    path('course/view', CourseView.as_view(), name='course_list'),
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
