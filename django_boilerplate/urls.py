"""django_boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# For Swagger/Redoc
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


@api_view(["GET"])
def health_check(request):
    """
    Simple endpoint to confirm the application is running.
    """
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


# Configure the schema view for drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="SpeedAdmin API",
        default_version="v1",
        description="API documentation for SpeedAdmin",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Health check endpoint
    path("health/", health_check, name="health-check"),
    # Swagger endpoints
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "api-doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # Redoc endpoint
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
