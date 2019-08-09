from django.shortcuts import render
from django.http import HttpResponse
from .forms import inputForm

# Create your views here.

def tracker(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = inputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            new = form.save()
            # redirect to a new URL:
            return HttpResponse('<h1>Done</h1><a href="/">go back</a>')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = inputForm()

    return render(request, 'index.html', {'form': form})

def add(request):
    return HttpResponse('<h1>Done</h1><a href="/">go back</a>')