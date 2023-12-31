from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # //User Login
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    #     Other Views
    path("list", views.ProductGetView.as_view()),
    path("post", views.ProductPostView.as_view()),
    path("update/<int:pk>", views.ProductUpdateView.as_view()),
    path("delete/<int:pk>", views.ProductDeleteView.as_view()),
]
