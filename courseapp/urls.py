from django.urls import path,include
from .import views
urlpatterns = [
      path('',views.home,name='home'),
      path('course/',views.course,name='course'),

      path('add_course/',views.add_course,name='add_course'),
      path('add_student/',views.add_student,name='add_student'),
      path('add_studentdb',views.add_studentdb,name='add_studentdb'),
      path('show_details',views.show_details,name='show_details'),
      path('edit/<int:pk>',views.edit,name='edit'),
      path('edit_details/<int:pk>',views.edit_details,name='edit_details'),
      path('delete/<int:pk>',views.delete,name='delete'),
      path('back',views.back,name='back')
      
  
]

