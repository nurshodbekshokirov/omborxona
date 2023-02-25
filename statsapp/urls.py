from django.urls import path
from .views import *

urlpatterns = [
    path('', Statsview.as_view(), name='stats'),
    path('stats_del<int:pk>/', Statsviewdelete.as_view(), name='stats-del'),
    path('stats_update<int:pk>/', Statsviewupdate.as_view(), name='stats-update'),

]