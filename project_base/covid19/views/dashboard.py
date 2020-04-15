from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from django.db.models import Sum, Count
from ..models import Covid

from ..debugger.decorators import query_debugger


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

    @query_debugger
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

        """
        section 1 
        # deprecated this section because of this section hit 2 times in database 
        
        # get total confirmed, death and recovered information from queryset
        dashboard = queryset.aggregate(confirmed = Sum('confirmed'), death=  Sum('death'),recovered = Sum('recovered'))
        # count distinct country from queryset
        countries_count = queryset.values('country_id').distinct().count()
        """

        # section 2 using this section because of this query only 1 time hit in database
        dashboard = queryset.aggregate(confirmed = Sum('confirmed'),death= Sum('death'),recovered = Sum('recovered'), countries = Count('country_id'))

        confirmed = 0 if dashboard['confirmed'] is None else dashboard['confirmed']
        death = 0 if dashboard['death'] is None else dashboard['death']
        recovered = 0 if dashboard['recovered'] is None else dashboard['recovered']
        countries = 0 if dashboard['countries'] is None else dashboard['countries']
        # countries = 0 if countries_count is None else countries_count

        return Response({'confirmed': confirmed, 'death': death, 'recovered': recovered, 'countries': countries})
