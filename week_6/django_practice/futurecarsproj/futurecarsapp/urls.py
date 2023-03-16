from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.newmake, name='newmake'),
    path('<int:id>/', views.makeid, name='makeid'),
    path('<int:id>/edit/', views.edit, name='makeedit'),
    path('<int:id>/cars/', views.cars, name='cars'),
    path('<int:id>/cars/new/', views.newcar, name='newcar'),
    path('<int:id>/cars/<int:model_id>', views.modelid, name='modelid'),
    path('<int:id>/cars/<int:model_id>/edit', views.modeledit, name='modeledit'),
]
