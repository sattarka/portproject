
from django.shortcuts import render


def alljobs(request):
    return render(request, 'jobs/alljobs.html')
