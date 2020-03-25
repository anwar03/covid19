from django.urls import path

from contact.views import UserContactAddApiView, UserContactApiView, UserContactEditApiView
from user.views import UserProfileApiView, UserProfileUpdateApiView, ChangePasswordApiView
from utils.urls import names

urlpatterns = [
    # path('', UserProjectListApiView.as_view(), name=names.url_employee_home),
    path('changed_password/', ChangePasswordApiView.as_view(), name=names.url_changed_password),
    # path('test/', UserProjectListApiViewTest.as_view(), name=names.url_employee_home_test),
    path('profile/', UserProfileApiView.as_view(), name=names.url_employee_profile),
    path('profile/edit/', UserProfileUpdateApiView.as_view(), name=names.url_employee_profile_update),
    path('contact/', UserContactApiView.as_view(), name=names.url_employee_contact),
    path('contact/add/', UserContactAddApiView.as_view(), name=names.url_employee_contact_add),
    path('contact/edit/', UserContactEditApiView.as_view(), name=names.url_employee_contact_edit),
]
