from django.urls import path

from covid19.views import Dashboard
from utils.urls.names import dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name=dashboard),
]
