from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import ScrapSerializer
# Create your views here.


class ScrapAPIView(APIView):
    def get(self, request):
        scraps = Scrap.objects.all()
        serializer = ScrapSerializer(scraps, many=True)
        return Response(serializer.data)


# /home/ubuntu/env/bin
# /home/ubuntu/GarbageGo
#
#
#
#
#
#
#
#
#
#
#
#
#
#


# server {
#     listen 80;
#     server_name 43.204.229.78;

#     location = /favicon.ico { access_log off; log_not_found off; }
#     # location /static/ {
#     #     root /home/sammy/myprojectdir;
#     # }

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/gunicorn.sock;
#     }
# }

# sudo cp /etc/nginx/sites-available/myproject /etc/nginx/sites-available/myproject.bak


# server {
#     listen 443 ssl;
#     listen [::]:443 ssl;
#     include snippets/self-signed.conf;
#     include snippets/ssl-params.conf;

# root /var/www/myproject/html;
#         index index.html index.htm index.nginx-debian.html;

#   server_name 43.204.229.78;

#   location / {
#                 try_files $uri $uri/ =404;
#         }
# }

# server {
#     listen 80;
#     listen [::]:80;

#     server_name 43.204.229.78;

#     return 302 https://$server_name$request_uri;
# }
