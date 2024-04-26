from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DepositOptions, DepositProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
import requests

api_key = settings.API_KEY
api_url = settings.API_URL
# 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(api_url, params=params).json().get('result')
    
    for base_item in response.get('baseList'):
        fin_prdt_cd = base_item.get('fin_prdt_cd')

        for key, value in base_item.items():
            if not value:
                if key == 'join_deny':
                    base_item[key] = -1
                else:
                    base_item[key] = ''

        deposit_product, created = DepositProducts.objects.update_or_create(
            fin_prdt_cd=fin_prdt_cd,
            defaults={
                'kor_co_nm': base_item.get('kor_co_nm'),
                'fin_prdt_nm': base_item.get('fin_prdt_nm'),
                'etc_note': base_item.get('etc_note'),
                'join_deny': int(base_item.get('join_deny')),
                'join_member': base_item.get('join_member'),
                'join_way': base_item.get('join_way'),
                'spcl_cnd': base_item.get('spcl_cnd'),
            }
        )

        options = [opt for opt in response.get('optionList') if opt['fin_prdt_cd'] == fin_prdt_cd]

        for option in options:
            for key, value in option.items():
                if not value:
                    if key in ('fin_prdt_cd', 'intr_rate_type_nm'):
                        option[key] == ''
                    else:
                        option[key] = -1

            DepositOptions.objects.create(
                product=deposit_product,
                fin_prdt_cd=fin_prdt_cd,
                intr_rate_type_nm=option.get('intr_rate_type_nm'),
                intr_rate=option.get('intr_rate'),
                intr_rate2=option.get('intr_rate2'),
                save_trm=option.get('save_trm'),
            )

    return JsonResponse({'message':'okay'})

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    try:
        options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(options, many=True)
        return Response(serializer.data)
    except DepositOptions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def top_rate(request):
    try:
        top_option = DepositOptions.objects.latest('intr_rate2')

        top_product = DepositProducts.objects.get(fin_prdt_cd=top_option.fin_prdt_cd)

        product_serializer = DepositProductsSerializer(top_product)
        option_serializer = DepositOptionsSerializer(top_option)

        response_data = {
            'product': product_serializer.data,
            'option': option_serializer.data
        }
        return Response(response_data)
    except DepositOptions.DoesNotExist:
        return Response({'message': 'No deposit products found'}, status=status.HTTP_404_NOT_FOUND)