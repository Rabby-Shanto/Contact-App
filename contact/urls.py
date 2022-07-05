from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add-contact/',views.add_contact,name="add_contact"),
    path('profile/<str:pk>',views.contact_profile,name="profile"),
    path('edit-contact/<str:pk>',views.editContact,name="edit"),
    path('delete/<str:pk>',views.deleteContact,name="delete")
    
]
