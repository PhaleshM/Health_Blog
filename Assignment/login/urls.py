from django.urls import path
from .views import UserProfile, SignUpView ,user_login, UserLogoutView


urlpatterns = [
    path("profile/",UserProfile,name="profile"),
    path('login/', user_login, name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
