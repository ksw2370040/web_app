from django.contrib import admin  # Djangoの管理サイトをインポート
from .models import Category, GamePost  # CategoryとGamePostモデルをインポート

# Categoryモデル用の管理サイトのカスタム設定を定義
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # 管理画面で表示するフィールドを指定
    list_display_links = ('id', 'title')  # リスト表示でリンクとして表示するフィールドを指定

# GamePostモデル用の管理サイトのカスタム設定を定義
class GamePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # 管理画面で表示するフィールドを指定
    list_display_links = ('id', 'title')  # リスト表示でリンクとして表示するフィールドを指定

# CategoryモデルとCategoryAdmin設定を管理サイトに登録
admin.site.register(Category, CategoryAdmin)
# GamePostモデルとGamePostAdmin設定を管理サイトに登録
admin.site.register(GamePost, GamePostAdmin)
