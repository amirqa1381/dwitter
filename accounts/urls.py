from django.urls import path
from .views import (RegisterView,
                    logout_view,
                    Login,
                    UpdateUserInfo,
                    SetImageUserOrUpdateUserImage,
                    UserPasswordChangeView,
                    ContactUserView
                    )

from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView,
                                       PasswordResetConfirmView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('contact/', ContactUserView.as_view(), name='contact'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('general-update/', UpdateUserInfo.as_view(), name='general_update_info'),
    path('image/', SetImageUserOrUpdateUserImage.as_view(), name='set_image'),
    path('password-chenage/', UserPasswordChangeView.as_view(), name='user_password_change'),
    # This part is for reseting the password and create new password if you forgot the current password
    path('password_reset/', PasswordResetView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_view"),
    path("password_reset_done/", PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("password_reset_complete/",
         PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
         name="password_reset_complete")
]
