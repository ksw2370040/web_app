from django.shortcuts import render  # Djangoのrender関数をインポート
from django.views.generic import CreateView, TemplateView  # Djangoの汎用ビューをインポート
from .forms import CustomUserCreationForm  # カスタムユーザー作成フォームをインポート
from django.urls import reverse_lazy  # URLの逆引きを行う関数をインポート

# サインアップ用のビューを定義するクラス
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # フォームに使用するクラスを指定

    template_name = 'signup.html'  # テンプレート名を指定

    success_url = reverse_lazy('accounts:signup_success')  # 成功時のリダイレクト先を指定

    # フォームが有効な場合の処理をオーバーライド
    def form_valid(self, form):
        user = form.save()  # フォームからユーザーを保存
        self.object = user
        return super().form_valid(form)  # 親クラスのメソッドを実行

# サインアップ成功時のビューを定義するクラス
class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'  # テンプレート名を指定
