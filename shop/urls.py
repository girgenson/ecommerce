from django.urls import path
from shop import views


urlpatterns = [
    path('', views.home, name="go_to_home_page"),
    path('about_app', views.about, name="go_to_about_page")
]
