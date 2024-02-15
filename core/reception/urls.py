from django.urls import path
from .views import (
    ReceptionCreateView,
    ReceptionListView,
    ReceptionDetailView,
    ReceptionCreateViewUsingProfile,
)

app_name = "reception"

urlpatterns = [
    path("list/", ReceptionListView.as_view(), name="list"),
    path("detail/<int:pk>/", ReceptionDetailView.as_view(), name="detail"),
    path("create/", ReceptionCreateView.as_view(), name="create"),
    path(
        "create/<int:pk>/",
        ReceptionCreateViewUsingProfile.as_view(),
        name="reception_create_using_profile",
    ),
]