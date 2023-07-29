"""linlog_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .views import UpdaterAPIView, RegisterUpdateComplete

urlpatterns = [
    path('', views.index, name='index'),
    path('how-to-use', views.htu, name='htu'),
    path('upd/<str:version_input>/<str:call_input>', views.updater, name='upd'),
    path('login', views.login, name='login'),
    path('enter', views.enter, name="enter"),
    path('logout', views.logout_view, name="logout"),
    path('api/v1/updater/<str:version_current>/<str:callsign>', UpdaterAPIView.as_view(), name="request_update"),
    path('api/v1/update-register', RegisterUpdateComplete.as_view(), name="update_complete"),
    path('api/v1/update-register/<int:pk>', RegisterUpdateComplete.as_view(), name="update_delete")


] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
