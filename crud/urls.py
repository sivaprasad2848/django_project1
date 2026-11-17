from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='crud'),
    path('insert_todo/',views.insert_todo,name='insert_todo'),
    path('delete_todo/<int:id>',views.delete_todo,name='delete_todo'),
    path('edit_todo/<int:id>',views.edit_todo,name='edit_todo'),
    path('update_todo/<int:id>',views.update_todo,name='update_todo')
]