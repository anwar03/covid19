from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from .models import Covid
from .serializers import Covid19Serializer


class Dashboard(APIView):
    """ load dashboard view for Novel Coronavirus (COVID-19) Situation visual information."""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        day = '2020-03-23'
        confirmed_count = Covid.objects.filter(created_at=day).aggregate(Sum('confirmed'))['confirmed__sum']
        death_count = Covid.objects.filter(created_at=day).aggregate(Sum('death'))['death__sum']
        recovered_count = Covid.objects.filter(created_at=day).aggregate(Sum('recovered'))['recovered__sum']
        countries_count = Covid.objects.filter(created_at=day).values('country_id').distinct().count()

        confirmed = 0 if confirmed_count is None else confirmed_count
        death = 0 if death_count is None else death_count
        recovered = 0 if recovered_count is None else recovered_count
        countries = 0 if countries_count is None else countries_count

        return Response({'confirmed': confirmed, 'death': death, 'recovered': recovered, 'countries': countries})


class Covid19CreateAPIView(CreateAPIView):
    """ Covid19CreateAPIView Created for creating everyday country-wise information."""
    permission_classes = (IsAuthenticated, )
    serializer_class = Covid19Serializer

    def perform_create(self, serializer):
        return super(Covid19CreateAPIView, self).perform_create(serializer)


class Covid19CountryDataUpdateApiView(RetrieveUpdateDestroyAPIView):
    """ Covid19CountryDataUpdateApiView created for  updating specific  information."""
    permission_classes = ( IsAuthenticated, )
    serializer_class = Covid19Serializer

    def get_queryset(self):
        queryset = Covid.objects.filter(id=self.kwargs['pk'])
        return queryset
