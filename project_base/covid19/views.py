from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class Dashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        dashboard = 'Covid 19 Dashboard'
        return Response({'dashboard': dashboard})
