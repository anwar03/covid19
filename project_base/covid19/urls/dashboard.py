from django.urls import path

from .. import views
from utils.urls.names import dashboard

urlpatterns = [
    path('', views.Dashboard.as_view(), name=dashboard),
]
