from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TestForm
from .models import TestM
# Create your views here.


def post(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            TestName = form.cleaned_data.get('TestName')
            File = form.cleaned_data.get('File')
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            messages.success(request, 'Test {} Posted successfully'.format('TestName'))
            return redirect('TakeTest-Home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()
    return render(request, 'Test/post.html', {'form': form})
