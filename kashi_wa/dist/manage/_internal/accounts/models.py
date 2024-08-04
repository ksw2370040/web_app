from django.db import models  # Djangoのモデルをインポート
from django.contrib.auth.models import AbstractUser  # DjangoのAbstractUserモデルをインポート

# カスタムユーザーモデルを定義し、AbstractUserを継承
class CustomUser(AbstractUser):
    pass
