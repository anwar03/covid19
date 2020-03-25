from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from project.models import Project
# from project.serializers import UserProjectSerializer
# from reporting.serializers import ReportedHoursCreateSerializer
from user.models import User
from user.serializers import UserSerializer, UserUpdateSerializer, ChangePasswordSerializer
from utils.urls.names import url_employee_profile, url_login


class UserProfileApiView(APIView):
    serializer_class = UserSerializer
    permission_classes = ()
    template_name = 'company/user/profile.html'

    def get(self, request):
        user = User.objects.get(username=self.request.user)
        return Response({'user': user})


class UserProfileUpdateApiView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    template_name = 'company/user/profile_edit.html'
    queryset = serializer_class.Meta.model.objects.all()

    def get(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserUpdateSerializer(instance=user)

        style = {'class': 'form-control', 'type': 'text'}
        return Response({'serializer': serializer, 'style': style})

    def post(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserUpdateSerializer(data=request.data)

        serializer.update(instance=user, validated_data=request.data)
        return redirect(reverse_lazy(url_employee_profile))


# class UserProjectListApiView(ListAPIView):
#     serializer_class = UserProjectSerializer
#     permission_classes = ()
#     filter_fields = ('name',)
#     template_name = 'company/user/list.html'
#
#     def get_queryset(self):
#         projects = Project.objects.filter(company__employees__user=self.request.user,
#                                           project_employees__employee__user=self.request.user)
#         return projects
#
#     def list(self, request, *args, **kwargs):
#         projects = super().list(request, args, kwargs)
#         serializer = ReportedHoursCreateSerializer()
#         return Response({
#             'projects': projects.data,
#             'project_list': self.get_queryset,
#             'serializer': serializer,
#             'query_params': request.query_params
#         })
#

class ChangePasswordApiView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    template_name = 'company/user/changed_password.html'

    def get(self, request, *args, **kwargs):
        return Response({'serializer': self.get_serializer_class()})

    def get_object(self):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "Old password are Wrong password.", 'serializer': serializer},
                                status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return redirect(reverse_lazy(url_login))
        return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)
