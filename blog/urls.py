from django.urls import path
from blog import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="registration_view"),
    path('blog/', views.BlogBaseApiView.as_view(), name="blog_list_view"),
    path('blog/<str:pk>/', views.BlogDetailApiView.as_view(), name="blog_detail_view"),
]