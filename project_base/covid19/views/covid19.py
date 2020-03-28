from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum
from ..models import Covid
from ..serializers import Covid19Serializer, CountryWiseSerializer, CountrySerializer


class Covid19CreateAPIView( CreateAPIView ):
    """ Covid19CreateAPIView Created for creating everyday country-wise information."""
    permission_classes = (IsAuthenticated, )
    serializer_class = Covid19Serializer

    def perform_create(self, serializer):
        return super(Covid19CreateAPIView, self).perform_create(serializer)


class Covid19CountryDataUpdateApiView( RetrieveUpdateDestroyAPIView ):
    """ Covid19CountryDataUpdateApiView created for  updating specific  information."""
    permission_classes = ( IsAuthenticated, )
    serializer_class = Covid19Serializer

    def get_queryset(self):
        # filter covid19 information for specific country
        queryset = Covid.objects.filter(id=self.kwargs['pk'])
        return queryset


class CountryWiseListAPIView( ListAPIView ):
    """ CountryWiseListAPIView API created to retrieving all countries' specific information."""
    permission_classes = (AllowAny, )
    serializer_class = CountryWiseSerializer

    def get_queryset(self):
        # cause of filtering specific day I have not updated data after 2020-03-23
        day = '2020-03-23'
        # filter covid19 information for specific day
        queryset = Covid.objects.filter(created_at=day)
        return queryset


class NewCaseListAPIView( APIView ):
    permission_classes = (AllowAny, )

    def get(self, request):
        previous_value = 0
        new_cases = list()
        # get country from query params
        country = self.request.query_params.get('country', None)
        queryset = Covid.objects.all()
        if country is not None:
            queryset = queryset.filter(country__name__iexact=country)

        queryset = queryset.values('created_at').order_by('created_at').annotate(confirmed=Sum('confirmed'))

        for item in queryset:
            new_cases.append({ 'created_at': item['created_at'], 'confirmed': item['confirmed'] - previous_value})
            previous_value = item['confirmed']

        return Response(new_cases)


class TotalCasesOfCountryListAPIView( ListAPIView ):
    permission_classes = (AllowAny, )
    serializer_class = CountrySerializer

    def get_queryset(self):
        day = '2020-03-23'
        queryset = Covid.objects.all()
        queryset = queryset.filter(created_at=day).order_by('-confirmed')
        return queryset
