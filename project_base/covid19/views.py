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
        confirmed = Covid.objects.filter(created_at='2020-03-23').aggregate(Sum('confirmed'))['confirmed__sum']
        death = Covid.objects.filter(created_at='2020-03-23').aggregate(Sum('death'))['death__sum']
        recovered = Covid.objects.filter(created_at='2020-03-23').aggregate(Sum('recovered'))['recovered__sum']
        countries = Covid.objects.values('country_id').distinct().count()

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
