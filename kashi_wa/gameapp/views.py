from django.shortcuts import redirect, get_object_or_404  # Djangoのビュー関数をインポート
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, FormView  # Djangoの汎用ビューをインポート
from django.urls import reverse_lazy  # DjangoのURL逆引きをインポート
from .forms import GamePostForm, CommentForm, ContactForm  # カスタムフォームをインポート
from django.utils.decorators import method_decorator  # メソッドデコレータをインポート
from django.contrib.auth.decorators import login_required  # ログイン必須デコレータをインポート
from .models import GamePost, Comment  # カスタムモデルをインポート
from django.contrib import messages  # Djangoのメッセージフレームワークをインポート
from django.core.mail import EmailMessage  # Djangoのメール送信機能をインポート

# インデックスページのビュー関数
class IndexView(ListView):
    template_name ='index.html'  # テンプレート名を指定
    context_object_name = 'orderby_records'  # コンテキスト変数名を指定
    queryset = GamePost.objects.order_by('-posted_at')  # クエリセットを指定
    paginate_by = 4  # ページネーション数を指定

# ゲーム情報投稿ページのビュー関数
@method_decorator(login_required, name='dispatch')
class CreateGameView(CreateView):
    form_class = GamePostForm  # フォームクラスを指定
    template_name = 'post_game.html'  # テンプレート名を指定
    success_url = reverse_lazy('gameapp:post_done')  # 成功時のURLを指定
    def form_valid(self, form) :
        postdate = form.save(commit=False)
        postdate.user = self.request.user
        postdate.save()
        return super().form_valid(form)

# 投稿成功ページのビュー関数
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'  # テンプレート名を指定

# カテゴリごとのゲーム情報一覧ページのビュー関数
class CategoryView(ListView):
    template_name = 'category.html'  # テンプレート名を指定
    paginate_by = 9  # ページネーション数を指定
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = GamePost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories

# ユーザーごとのゲーム情報一覧ページのビュー関数
class UserView(ListView):
    template_name = 'category.html'  # テンプレート名を指定
    paginate_by = 9  # ページネーション数を指定
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = GamePost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list

# ゲーム情報詳細ページのビュー関数
class DetailView(DetailView):
    template_name='detail.html'  # テンプレート名を指定
    model = GamePost  # モデルを指定

# コメント投稿ページのビュー関数
class CreateCommentView(CreateView):
    form_class = CommentForm  # フォームクラスを指定
    template_name = 'comment.html'  # テンプレート名を指定
    model = Comment  # モデルを指定

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(GamePost, pk=post_pk)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('gameapp:game_detail', pk=post_pk)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(GamePost, pk=self.kwargs['pk'])
        return context

# マイページのビュー関数
class MypageView(ListView):
    template_name ='mypage.html'  # テンプレート名を指定
    paginate_by = 9  # ページネーション数を指定
    def get_queryset(self):
        queryset = GamePost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

# ゲーム情情報削除ページのビュー関
class GameDeleteView(DeleteView):
    model=GamePost
    template_name = 'game_delete.html'
    success_url= reverse_lazy('gameapp:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ContactView(FormView):
    template_name ='contact.html'  # テンプレート名を指定
    form_class = ContactForm  # フォームクラスを指定
    success_url = reverse_lazy('gameapp:contact')  # 送信成功後のリダイレクト先を指定

    def form_valid(self, form):  
        name = form.cleaned_data['name']  # フォームから名前を取得
        email = form.cleaned_data['email']  # フォームからメールアドレスを取得
        title = form.cleaned_data['title']  # フォームから件名を取得
        message = form.cleaned_data['message']  # フォームからメッセージを取得
        subject = 'お問い合わせ: {}'.format(title)  # 件名を作成
        message = '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        from_email = 'blogapp.2370040@gmail.com'  # 送信元メールアドレスを設定
        to_list = ['blogapp.2370040@gmail.com']  # 送信先メールアドレスを設定
        message = EmailMessage(subject=subject,  # メールメッセージを作成
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               ) 
        try:
            message.send()  # メールを送信
            messages.success(self.request, "送信完了")  # 送信完了メッセージを表示
        except Exception as e:
            messages.error(self.request, f"送信失敗:{e}")  # 送信失敗メッセージを表示
        return super().form_valid(form)  # フォームのバリデーションに成功した場合の処理
