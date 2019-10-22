from django.urls import path, include, re_path
from rest_auth.views import PasswordResetConfirmView

from . import views

urlpatterns = [
    path('blog/', views.BlogList.as_view()),
    path('blog/<int:pk>/', views.BlogDetail.as_view()),
    path('account/', include('rest_auth.urls')),
    path('account/register/', include('rest_auth.registration.urls')),
    re_path('account/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
]
