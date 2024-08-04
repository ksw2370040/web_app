from django.apps import AppConfig  # Djangoアプリの設定をインポート

# ゲーム情報アプリの設定を定義するクラス
class GameappConfig(AppConfig):
    # モデルの自動生成に使用されるフィールドのタイプを指定
    default_auto_field = 'django.db.models.BigAutoField'
    # アプリケーションの名前を指定
    name = 'gameapp'
