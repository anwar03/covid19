from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contact.serializers import ContactSerializer
from user.models import User
from utils.urls.names import url_employee_contact, url_employee_home, url_employee_contact_edit


class UserContactApiView(APIView):
    template_name = 'company/user/contact/contact.html'

    def get(self, request):
        user = User.objects.get(username=request.user)
        return Response({'contact': user.contact})


class UserContactAddApiView(APIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    template_name = 'company/user/contact/contact_add.html'

    def get(self, request):
        contact = ContactSerializer()
        return Response({'serializer': contact})

    def post(self, request):
        user = User.objects.get(username=self.request.user)
        serializer = ContactSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'serializer': serializer})

        contact = serializer.save()
        user.contact = contact
        user.save()
        return redirect(reverse_lazy(url_employee_contact))


class UserContactEditApiView(RetrieveUpdateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    template_name = 'company/user/contact/contact.html'
    queryset = serializer_class.Meta.model.objects.all()

    def get(self, request):
        user = User.objects.get(username=request.user)
        serializer = ContactSerializer(instance=user.contact)
        return Response({'serializer': serializer})

    def post(self, request):
        user = User.objects.get(username=request.user)
        serializer = ContactSerializer(data=request.data)

        serializer.update(instance=user.contact, validated_data=request.data)
        return redirect(reverse_lazy(url_employee_contact))

