from django.urls import path
from . import views


app_name = 'Zoom_App'

urlpatterns = [
    path('form', views.FormView.as_view(),name="form"),
    path('', views.LessonList.as_view(), name='list'),
    path('form2/<int:pk>/',views.Form2.as_view(),name='form2'),
    path("ajax/", views.zoom, name="zoom"),
    path('update/<int:pk>/',views.Update.as_view(), name="update"),
    path('delete/<int:pk>/',views.DeleteView.as_view(), name="delete")
]