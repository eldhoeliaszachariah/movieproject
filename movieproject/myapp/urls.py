from . import views
from django.urls import path
app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movieid>/',views.details,name='details'),
    path('add/',views.addmovie,name='addmovie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
