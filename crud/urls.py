from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit/update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete')
    
]