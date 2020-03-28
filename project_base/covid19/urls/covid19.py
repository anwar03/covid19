from django.urls import path

from ..views import covid19
from utils.urls import names


urlpatterns = [
    # Retrieve list of country wise information
    path('', covid19.CountryWiseListAPIView.as_view(), name=names.country_wise_data),
    # Retrieve, update and delete specific country information by id
    path('<int:pk>/', covid19.Covid19CountryDataUpdateApiView.as_view(), name=names.update_covid19_data),
    # store new information for country
    path('create/', covid19.Covid19CreateAPIView.as_view(), name=names.store_covie19_data),
    path('newcase/', covid19.NewCaseListAPIView.as_view(), name=names.new_cases),
    path('countrydata/', covid19.TotalCasesOfCountryListAPIView.as_view(), name='country-data'),
]
