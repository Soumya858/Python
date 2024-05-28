from django.urls import path
from members import views

urlpatterns = [
    path('createpost/',views.createpost,name='createpost'),
]