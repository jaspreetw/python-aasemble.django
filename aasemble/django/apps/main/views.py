from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated():
        return render(request, 'aasemble/dashboard.html', {})
    else:
        return render(request, 'aasemble/front.html', {})


@login_required
def profile(request):
    return render(request, 'aasemble/profile.html')
