from django.urls import path

from ..views.dashboard import Dashboard, DashboardInfo
from utils.urls.names import dashboard, dashboard_data

urlpatterns = [
    path('', Dashboard.as_view(), name=dashboard),
    path('dashboard/', DashboardInfo.as_view(), name=dashboard_data),
]
