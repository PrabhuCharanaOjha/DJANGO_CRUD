from crud import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('updatestudent/<int:pk>', views.updatestudent.as_view(), name='updatestudent'),
    path('deletestudent/<int:pk>',
         views.deletestudent.as_view(), name='deletestudent'),
]
