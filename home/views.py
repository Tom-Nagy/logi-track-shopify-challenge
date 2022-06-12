''' Views for the home/landing page '''

from django.shortcuts import render


def index(request):
    ''' A view to render the home page '''
    template = 'home/index.html'
    # context = {}
    return render(request, template)
