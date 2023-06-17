from django.http import HttpResponse
from django.shortcuts import render
from .form import MyForm


def greet():
    return HttpResponse("Hello There ! ")


def home(request):
    return render(request, 'home.html')


def child(request):
    return render(request, 'child.html')


def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            member_id = form.cleaned_data['member_id']
            member_email = form.cleaned_data['member_email']
            course = form.cleaned_data['course']
            staff = form.cleaned_data['staff']

            # Redirect to a success page
            return render(request, 'success.html')
    else:
        form = MyForm()

    return render(request, 'my_form.html', {'form': form})
