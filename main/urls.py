from django.urls import path
from . import views  # Import the views from the same directory

urlpatterns = list({
    path('', views.home, name='home'),  # Home page (index.html)
    path('register/', views.register, name='register'),  # Register page (register.html)
    path('contact/', views.contact, name='contact'),  # Contact page
    path('login/', views.login_view, name='login'),
})
