from django.urls import path
from .views import *
urlpatterns = [
    path('', Bolimlarview.as_view()),
    path('mahsulotlar/', Mahsulotlarview.as_view(), name='mahsulotlar'),
    path('clientlar/',Clientview.as_view(), name='clientlar')

]