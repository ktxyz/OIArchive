from django.shortcuts import render


def indexView(request):
    """
        Index page.
        TODO: add user specific data
    """
    return render(request, 'base_layout/index.html')