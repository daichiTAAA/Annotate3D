from django.urls import path, include

urlpatterns = [
    path("dash/", include("django_plotly_dash.urls")),
]
