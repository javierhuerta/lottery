from django.shortcuts import render


def home(request):
    return render(request, 'lottery_app/base.html')