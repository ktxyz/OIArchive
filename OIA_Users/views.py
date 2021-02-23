from django.shortcuts import render


def homepage(request):
    return render(request, 'base_layout/index.html')
