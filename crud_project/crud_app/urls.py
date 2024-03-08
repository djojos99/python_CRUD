from django.urls import path
from .views import insert_emp, show_emp, edit_emp, delete_emp, essai

urlpatterns = [

    path('', insert_emp, name='insert_emp'),
    path('show/', show_emp, name='show_emp'),
    path('edit/<int:pk>', edit_emp, name='edit_emp'),
    path('delete/<int:pk>', delete_emp, name='delete_emp'),
    path('essai/', essai, name='essai')
]