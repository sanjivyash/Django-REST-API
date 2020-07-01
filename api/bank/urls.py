from django.urls import path, include
from .views import ViewBranchesInCity, ViewBankFromIFSC
import rest_framework as rest

urlpatterns = [
    path('ifsc/', ViewBankFromIFSC.as_view(), name='IFSC'),
    path('branches/', ViewBranchesInCity.as_view(), name='branches')
]