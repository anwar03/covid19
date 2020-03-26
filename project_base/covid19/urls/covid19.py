from django.urls import path

from .. import views
from utils.urls import names

urlpatterns = [
    path('create/', views.Covid19CreateAPIView.as_view(), name=names.store_covie19_data),
    path('update/<int:pk>/', views.Covid19CountryDataUpdateApiView.as_view(), name=names.update_covid19_data),
]
