from django.urls import path

from .. import views
from utils.urls import names


urlpatterns = [
    # Retrieve list of country wise information
    path('', views.CountryWiseListAPIView.as_view(), name=names.country_wise_data),
    # Retrieve, update and delete specific country information by id
    path('<int:pk>/', views.Covid19CountryDataUpdateApiView.as_view(), name=names.update_covid19_data),
    # store new information for country
    path('create/', views.Covid19CreateAPIView.as_view(), name=names.store_covie19_data),
    path('newcase/', views.NewCaseListAPIView.as_view(), name=names.new_cases),
]
