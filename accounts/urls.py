from django.urls import path
from .views import (RegisterView,
                    logout_view,
                    Login,
                    UpdateUserInfo,
                    SetImageUserOrUpdateUserImage,
                    UserPasswordChangeView
                    )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('general-update/', UpdateUserInfo.as_view(), name='general_update_info'),
    path('image/', SetImageUserOrUpdateUserImage.as_view(), name='set_image'),
    path('password-chenage/', UserPasswordChangeView.as_view(), name='user_password_change')
]
