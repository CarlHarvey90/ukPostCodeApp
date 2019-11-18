from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from App.post_code_val import postCodeVal
import requests

# Create your views here.

# post the postal code to function postCodeVal to get formated and check with regex, then if successful use that postal code in the GET below
@api_view(["POST"])
def checkPostCode(post_code_data):

    try:
        # post_code = json.loads(post_code_data.body)
        post_code_response = postCodeVal(str(post_code_data))

        return JsonResponse(post_code_response , safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


# validate the post code from the post against an API with real UK Post Codes..
@api_view(["GET"])
def validatePostCode(post_code_data):

    postcode = postCodeVal(post_code_data)
    r = requests.get('https://www.doogal.co.uk/GetPostcode.ashx/?postcode=' + postcode)

    if r.text:
        # return this info
        print(r.text)
    else:
        # return this info
        print('This UK Post Code does not exist')