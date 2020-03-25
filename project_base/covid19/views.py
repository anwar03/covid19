from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.db.models import Sum, Count
from .models import Covid


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
