from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('doc/contract/', contract, name='contract'),
    path('doc/instruction/', instruction, name='instruction'),
    path('doc/rules/', rules, name='rules'),
    path('information/', information, name='information'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    # path('login/', LoginUser.as_view(), name='login'),
    path('bookingapier/', bookingapier, name='bookingapier'),
    # path('api/v1/bookingpier/', bookingapier, name='bookingapier'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    #    path('pier/<int:pier_id>/', pier),
    #    path('filter/<int:pk>/', views.index, name='index'),
]
