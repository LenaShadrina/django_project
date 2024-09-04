from django.shortcuts import render
from goods.models import Book, Product, Author, BookInstance
from main_refs.models import Author
from django.shortcuts import render
# from .forms import HomepageForm
from . import models
from django.http import HttpResponse


# Create your views here.


def index(request):
    text_head = "My book shop"
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact=2).count()
    num_authors = Author.objects.count()

    return render(request,'catalog/index.html', context={
        "text_head": text_head,
        "books": books,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors
    }
    )

# def image_upload_view(request):
#     if request.method == 'POST':
#         form = HomepageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = HomepageForm()
#     return render(request, 'index.html', {'form': form})
