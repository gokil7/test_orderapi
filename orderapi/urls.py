from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Order API",
      default_version='v1',
      description="API for ordering Food",
      terms_of_service="https://test/tcs",
      contact=openapi.Contact(email="gokil22797@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', views.orderapi, name="orderapi"),
    path('order-lists/', views.orderLists, name="order-lists"),
    path('order-details/<str:pk>/', views.orderDetails, name="order-details"),
    path('create-order/', views.createOrder, name="create-order"),
    path('update-order/<str:pk>/', views.updateOrder, name="update-order"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="delete-order"),
    # path('docs/', include_docs_urls(title='OrderAPI')),
    # path('schema-view/', get_schema_view(
    #     title="OrderAPI",
    #     description="API for ordering",
    #     version="1.0",
    # ), name="schema-view"),


    # path('swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
