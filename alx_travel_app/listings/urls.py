from django.urls import path
from . import views  # or from listings import views if absolute

urlpatterns = [
    # example path
    path('', views.index, name='listings-index'),
]
