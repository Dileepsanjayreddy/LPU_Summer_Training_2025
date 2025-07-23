from django.urls import path
import booksmgnt.views
from booksmgnt import views
urlpatterns = [
    path('',views.book_list,name='book_list')
]