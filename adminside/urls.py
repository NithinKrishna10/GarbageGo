from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView,UserApi
from . import views
from .scrap import ScrapListAPIView,ScrapCategoryView
from . import scrap

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('userlist',views.userlist),
    path('logout', LogoutView.as_view()),
    path('userapi',UserApi.as_view()),
    path('block_user/<int:id>/', views.block_user, name='block_user'),
    path('unblock_user/<int:id>/', views.unblock_user, name='block_user'),
    path('addcat',views.category_list,name="addcat"),


    path('scrap_category',ScrapCategoryView.as_view(),name='scrap-list'),
    path('scraps/', ScrapListAPIView.as_view(), name='scrap-list'),
    path('scrapp/<int:pk>/', scrap.ScrapEditAPIView, name='scrap-detail'),
    # path('scraps/<int:pk>/', ScrapRetrieveUpdateDestroyAPIView.as_view(), name='scrap-detail'),   

        

]