from django.shortcuts import render
from .models import BankDetails
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class ViewBankFromIFSC(View):
# ?ifsc=ifsc query string
    def get(self, request):
        if request.GET.get('ifsc'):
            ifsc = request.GET.get('ifsc')
            bank = BankDetails.objects.filter(bank_ifsc=ifsc)
            try:
                bank = bank[0]
            except:
                return JsonResponse({ 'error': 'Invalid IFSC code' })

            result = {}
            for key, value in vars(bank).items():
                if key[0] != '_': # ignore _state key, value pair 
                    result[key[5:]] = value
            return JsonResponse(result)
            
        else:
            return JsonResponse({ 'error': 'Please provide IFSC code' })


class ViewBranchesInCity(View):
# ?city=city&bank=name query string
    def get(self, request):
        if request.GET.get('city') and request.GET.get('bank'):
            city = request.GET.get('city')
            name = request.GET.get('bank')
            banks = BankDetails.objects.filter(bank_city=city, bank_name=name)
            try:
                temp = banks[0]
            except:
                return JsonResponse({ 'error': 'No branches found' })
            res = []
            for bank in banks:
                result = {}
                for key, value in vars(bank).items():
                    if key[0] != '_': # ignore _state key, value pair 
                        result[key[5:]] = value
                res.append(result)
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse({ 'error': 'Please provide bank name and city' })