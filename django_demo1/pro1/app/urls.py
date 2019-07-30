from django.urls import path
from . import views
from .views import MyView

urlpatterns = [
    path('',views.display_view),
    path('viewtest',MyView.as_view())
]
