from django.urls import path
from .views import *
urlpatterns = [
    path('', Bolimlarview.as_view()),
    path('mahsulotlar/', Mahsulotlarview.as_view(), name='mahsulotlar'),
    path('clientlar/',Clientview.as_view(), name='clientlar'),
    path('mahsulot_del<int:pk>/', MahsulotdeleteView.as_view(), name='mahsulot-del'),
    path('client_del<int:pk>/', ClientsdeleteView.as_view(), name='client-del'),
    path('mahsulot_update<int:pk>/', MahsulotupdateView.as_view(), name='mahsulot-update'),
    path('client_update<int:pk>/', Clientupdateview.as_view(), name='client-update'),
    path('client_search/',Client_search.as_view()),
    path('product_search/', Mahsulotsearch.as_view())

]