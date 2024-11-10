from django.urls import path
from .views import UserProfileList, UserProfileDetail, RegistrationView, CustomLoginView, UserFromTokenView

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile_list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile_detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('token_auth/', UserFromTokenView.as_view(), name='token_auth'),
]
