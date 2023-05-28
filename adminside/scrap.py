from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from accounts.models import User
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema



