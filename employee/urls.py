from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/createData/', views.createData, name='createData'),
    path('delete/<int:empID>', views.delete, name='delete'),
    path('update/<int:empID>', views.update, name='update'),
    path('update/updateData/<int:empID>', views.updateData, name='updateData'),
    path('test/', views.test, name='test')
]