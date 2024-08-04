from django.contrib import admin  # Djangoのadminモジュールをインポート
from .models import CustomUser  # CustomUserモデルをインポート

# CustomUserモデルを管理サイトでカスタマイズするためのクラスを定義
class CustomUserAdmin(admin.ModelAdmin):
    # 管理画面のリスト表示で表示するフィールドを指定
    list_display = ('id', 'username')
    # リスト表示でリンクとして表示するフィールドを指定
    list_display_links = ('id', 'username')

# CustomUserモデルを管理サイトに登録し、CustomUserAdminを適用
admin.site.register(CustomUser, CustomUserAdmin)
