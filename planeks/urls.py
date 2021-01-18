"""planeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from dummy_gen.views import *
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('do/<int:id>/', login_required(do)),
    path('create/', login_required(scheme_create)),
    path('list/', login_required(scheme_list)),
    path('edit/<int:id>/', login_required(scheme_edit.as_view())),
    path('delete/<int:id>/', login_required(scheme_delete.as_view())),
    path('celery-progress/', include('celery_progress.urls')),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html')),
    path('accounts/profile/', RedirectView.as_view(url='/./list/', permanent=False))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
