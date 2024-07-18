from django.apps import AppConfig

# アプリケーションの設定を定義するクラス
class AccountsConfig(AppConfig):
    # モデルの自動生成に使用されるフィールドのタイプを指定
    default_auto_field = 'django.db.models.BigAutoField'
    # アプリケーションの名前を指定
    name = 'accounts'
