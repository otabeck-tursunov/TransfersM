from tkinter.font import names

from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('latest-transfers/', LatestTransfersView.as_view(), name='latest-transfers'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('stats/150-accurate-predictions/', AccuratePredictions150View.as_view(), name='stats-accurate-predictions')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


