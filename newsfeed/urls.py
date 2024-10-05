from django.urls import path
from .views import newsfeed, post_product


urlpatterns = [
    path('', newsfeed, name='newsfeed'),
    path('post/', post_product, name='post_product'),
]