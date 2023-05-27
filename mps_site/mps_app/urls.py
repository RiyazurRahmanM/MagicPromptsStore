from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('sell/',views.sell_view,name='sell_view'),
    path('find/',views.find_view,name='find_view'),
    path('sell_cont_view/',views.sell_cont_view,name='sell_cont_view'),
]