from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理者ページ
    path('', include('gameapp.urls')),  # ゲームアプリのURL
    path('', include('accounts.urls')),  # アカウントアプリのURL
    path('password_reset/',  # パスワードリセット用のURL
         auth_views.PasswordResetView.as_view(
             template_name="password_reset.html"),
             name='password_reset'),
    path('password_reset/done/',  # パスワードリセット完了用のURL
         auth_views.PasswordResetDoneView.as_view(
         template_name = "password_reset_sent.html"),
            name ='password_reset_done'),

    path('reset/<uidb64>/<token>',  # パスワードリセット確認用のURL
         auth_views.PasswordResetConfirmView.as_view(
            template_name = "password_reset_form.html"),
            name = 'password_reset_confirm'),
    path('reset/done/',  # パスワードリセット完了用のURL
         auth_views.PasswordResetCompleteView.as_view( 
             template_name = "password_reset_done.html"), 
             name ='password_reset_complete'),
]
urlpatterns += static(  # メディアファイルのURL
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
