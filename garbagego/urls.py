"""
URL configuration for garbagego project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from orders.views import PlaceOrderAPIView
urlpatterns = [
    # api docs
    path("api/schema/",SpectacularAPIView.as_view(),name="schema"),
    path("api/schema/docs",SpectacularSwaggerView.as_view(url_name="schema")),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('adminside/',include('adminside.urls')),
    path('order',include('orders.urls')),
    path('place',PlaceOrderAPIView.as_view()),
    path('waste/',include('waste.urls')),
     path('scrap/',include('scrap.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)