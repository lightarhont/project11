from django.urls import path
from .views import PageView, PagesView 

# app_name will help us do a reverse look-up latter.
urlpatterns = [path('page/<int:item>', PageView.as_view()),
               path('pages/<int:offset>/<int:limit>/', PagesView.as_view()),]