import datetime

from rest_framework.response import Response


class RetrieveMixin(object):

    def get(self, request, *args, **kwargs):
        if str.lower(request.accepted_renderer.format) == 'html':
            return Response({'serializer': self.get_serializer(instance=self.get_object())})
        return super().get(request, *args, **kwargs)


class DateMixin(object):
    def date(self, request):

        if request.query_params.get('days'):
            days = request.query_params.get('days')
            date_from = datetime.datetime.today() - datetime.timedelta(days=int(days))
            date_to = datetime.datetime.now()
        else:
            date_from = datetime.datetime.today() - datetime.timedelta(days=30)
            date_to = datetime.datetime.now()

        if request.query_params.get('date_from'):
            date_from = request.query_params.get('date_from', None)
            if date_from == '' or date_from is None:
                date_from = datetime.datetime.today() - datetime.timedelta(days=30)
        # else:
        #     date_from = datetime.datetime.today() - datetime.timedelta(days=30)

        if request.query_params.get('date_to'):
            date_to = request.query_params.get('date_to', None)

            if date_to == '' or date_to is None:
                date_to = datetime.datetime.now()
        # else:
        #     date_to = datetime.datetime.now()

        return date_from, date_to
