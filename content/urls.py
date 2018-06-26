from django.urls import path, include
from content import views
urlpatterns = [
    path('', views.home),
    path('legal/', views.LegalInfo),
    path('posting/', views.preposting, name='preposting'),
    path('payment-form/', views.payment_form, name='payment_form'),
    path('payment-form/checkout/', views.checkout, name='checkout'),
    path('about/', views.about),
]