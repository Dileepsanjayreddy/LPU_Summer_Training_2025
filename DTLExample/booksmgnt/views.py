from django.shortcuts import render

# Create your views here.
def book_list(request):
    books=[
        {'title': 'c Pgm', 'author': 'ABC', 'available': False},
        {'title': 'c++ Pgm', 'author': 'XYZ', 'available': True},
        {'title': 'Java Pgm', 'author': 'MNO', 'available': False},
        {'title': 'Python Pgm', 'author': 'QWE', 'available': True},
    ]
    return render(request,'booksmgnt/book_list.html',{'books':books})
