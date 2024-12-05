from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path("<int:pk>/", views.PostDetailView.as_view(), name='detail') # <int:pk> means the domain name and then /
]