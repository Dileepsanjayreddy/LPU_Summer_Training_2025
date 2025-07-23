#
# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views import generic
# from todolist.models import Todo
#
# # Create your views here.
# class TodoListView(generic.ListView):
#     model = Todo
#     template_name = 'list.html'
#     context_object_name = 'todos'
#
# class TodoCreateView(generic.CreateView):
#     model = Todo
#     template_name = 'create.html'
#     fields = ['title', 'description','is_active']
#     success_url = reverse_lazy('todo_view')
#
# class TodoUpdateView(generic.UpdateView):
#     model = Todo
#     template_name = 'update.html'
#     fields = ['title', 'description', 'is_active']
#     success_url = reverse_lazy('todo_view')
#
#
# class TodoDeleteView(generic.DeleteView):
#     model = Todo
#     template_name = 'delete.html'
#     fields = ['title', 'description', 'is_active']
#     success_url = reverse_lazy('todo_view')
#
#
#
