from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookForm
from .models import Book
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')


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


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace 'book_list' with the URL name of your book list view
    else:
        form = BookForm()

    context = {
        'form': form
    }

    return render(request, 'first/book_form.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

