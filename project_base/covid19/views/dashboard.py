from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from django.db.models import Sum
from ..models import Covid

class Dashboard(APIView):
    """ load dashboard view for Novel Coronavirus (COVID-19) Situation visual information."""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard/dashboard.html'
    permission_classes = (AllowAny, )

    def get(self, request):
        # only load dashboard tamplete
        title = "Covid19 Dashboard"
        return Response({ 'title': title })

class DashboardInfo(APIView):
    """ load dashboard view for Novel Coronavirus (COVID-19) Situation visual information."""

    def get(self, request):
        # cause of filtering specific day I have not updated data after 2020-03-23
        day = '2020-03-23'
        # get country from query params
        country = self.request.query_params.get('country', None)
        queryset = Covid.objects.all()
        if country is not None:
            queryset = queryset.filter(country__name__iexact=country)
        # filter covid19 information for specific day
        queryset = queryset.filter(created_at=day)
        # get total confirmed, death and recovered information from queryset
        dashboard = queryset.aggregate(Sum('confirmed'), Sum('death'), Sum('recovered'))
        # count distinct country from queryset
        countries_count = queryset.values('country_id').distinct().count()

        confirmed = 0 if dashboard['confirmed__sum'] is None else dashboard['confirmed__sum']
        death = 0 if dashboard['death__sum'] is None else dashboard['death__sum']
        recovered = 0 if dashboard['recovered__sum'] is None else dashboard['recovered__sum']
        countries = 0 if countries_count is None else countries_count

        return Response({'confirmed': confirmed, 'death': death, 'recovered': recovered, 'countries': countries})
