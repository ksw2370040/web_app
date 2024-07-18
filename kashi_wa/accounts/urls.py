from django.urls import path  # DjangoのURLパスをインポート
# viewsモジュール をインポート
from . import views
from django.contrib.auth import views as auth_views  # Djangoの認証ビューをインポート

app_name = 'accounts'  # アプリケーションの名前空間を定義

urlpatterns = [
    # サインアップ用のビューをsignupとして設定
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),

    # サインアップ成功時のビューをsignup_successとして設定
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),

    # ログイン用のビューをloginとして設定
    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),

    # ログアウト用のビューをlogoutとして設定
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),
]
