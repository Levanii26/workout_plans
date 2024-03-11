from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Personalized Workout Plan API",
      default_version='v1',
      description="API for managing personalized workout plans",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="career.chutlshvili1@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("plans.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('plans.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]