from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('forms/',views.forms,name="forms"),
    path('detail/<id>',views.details,name="detail"),
    # path('annonce/',views.Annonce,name="annonce"),
     path('contact_form/', views.contact_form, name='contact_form'),
]