from django.urls import path
from .views import *
urlpatterns = [
    path('', Bolimlarview.as_view())

]