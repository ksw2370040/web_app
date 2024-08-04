from django.forms import ModelForm  # Djangoのモデルフォームをインポート
from .models import GamePost, Comment  # GamePostとCommentモデルをインポート

# ゲーム情報投稿フォームを定義するクラス
class GamePostForm(ModelForm):
    class Meta:
        model = GamePost  # フォームが対象とするモデルを指定
        fields = ['category', 'title', 'contents', 'image1', 'image2']  # フォームで表示するフィールドを指定

# コメントフォームを定義するクラス
class CommentForm(ModelForm):
    class Meta:
        model = Comment  # フォームが対象とするモデルを指定
        exclude = ('post', 'created_at')  # フォームで除外するフィールドを指定

from django import forms  # Djangoのフォームをインポート

# お問い合わせフォームを定義するクラス
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')  # 名前入力欄を定義
    email = forms.EmailField(label='メールアドレス')  # メールアドレス入力欄を定義
    title = forms.CharField(label='件名')  # 件名入力欄を定義
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)  # メッセージ入力欄を定義

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # プレースホルダーとCSSクラスを設定
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'
