from django.urls import path
from . import views

app_name = "viacep"

urlpatterns = [
    path("", views.ViaCepFormView.as_view(), name="form"),
    path("list/", views.ViaCepListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.ViaCepDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", views.ViaCepDeleteView.as_view(), name="delete"),
]