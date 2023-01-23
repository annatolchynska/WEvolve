from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def mental(request):
    return render(request, 'mental.html', {})


def holistic(request):
    return render(request, 'holistic.html', {})


def addiction(request):
    return render(request, 'addiction.html', {})


def costs(request):
    return render(request, 'costs.html', {})
