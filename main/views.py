from django.shortcuts import render
from django.views import View
from .models import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        context = {
            'clubs': clubs
        }
        return render(request, 'clubs.html', context)


class LatestTransfersView(View):
    def get(self, request):
        transfers = Transfer.objects.filter(season=Season.objects.last()).order_by('-price')
        context = {
            'transfers': transfers
        }
        return render(request, 'latest-transfers.html', context)


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about.html')
