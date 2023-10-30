from docs.apps import DocsConfig
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path

app_name = DocsConfig.name


schema_view = get_schema_view(
    openapi.Info(
        title="Трекер Привычек",
        default_version='v1.32',
        description="Описание эндпоинтов API трекера привычек.",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="developer@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
