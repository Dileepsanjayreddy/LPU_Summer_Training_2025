from django.urls import path

from librarymgnt import views


urlpatterns = {
    path('', views.BookListView.as_view(), name='listallbooks'),
    path('addbook/', views.BookCreateView.as_view(), name='addnewbook'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='addnewbook'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='modifybook'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='deletebook'),
}