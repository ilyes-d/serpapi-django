from django.urls import path
from .views import *


urlpatterns = [
    path('', index ),
    path('profile/', get_author_profile , name='author-profile'),
]
