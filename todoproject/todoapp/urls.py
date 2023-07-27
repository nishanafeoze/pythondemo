from django.urls import path

from todoapp import views

urlpatterns = [
      path('', views.home, name='home'),
#       path('details', views.details, name='details'),
      path('delete/<int:id>/', views.delete, name='delete'),
       path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Tasklisitview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetail'),

   path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),
]
