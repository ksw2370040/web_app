from django.contrib.auth.forms import UserCreationForm  # Djangoのユーザー作成フォームをインポート
from .models import CustomUser  # CustomUserモデルをインポート

# CustomUserモデルを使用してカスタムユーザー作成フォームを定義
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # フォームが使用するモデルを指定
        fields = ('username', 'email',)  # フォームで表示するフィールドを指定
