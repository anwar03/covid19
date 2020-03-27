from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum
from .models import Covid
from .serializers import Covid19Serializer, CountryWiseSerializer


class Dashboard(APIView):
    """ load dashboard view for Novel Coronavirus (COVID-19) Situation visual information."""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        # cause of filtering specific day I have not updated data after 2020-03-23
        day = '2020-03-23'
        # filter covid19 information for specific day
        queryset = Covid.objects.filter(created_at=day)
        # get total confirmed, death and recovered information from queryset
        dashboard = queryset.aggregate(Sum('confirmed'), Sum('death'), Sum('recovered'))
        # count distinct country from queryset
        countries_count = queryset.values('country_id').distinct().count()

        confirmed = 0 if dashboard['confirmed__sum'] is None else dashboard['confirmed__sum']
        death = 0 if dashboard['death__sum'] is None else dashboard['death__sum']
        recovered = 0 if dashboard['recovered__sum'] is None else dashboard['recovered__sum']
        countries = 0 if countries_count is None else countries_count

        return Response({'confirmed': confirmed, 'death': death, 'recovered': recovered, 'countries': countries})


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
