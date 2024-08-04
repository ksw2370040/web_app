from django.urls import path  # DjangoのURLパスをインポート
from . import views  # viewsモジュールをインポート

# URLパターンの名前空間を定義
app_name = 'gameapp'

# URLパターンを登録するリスト
urlpatterns = [
    # ホームページへのアクセスはIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    # ゲーム情報詳細ページへのアクセスはDetailViewを実行
    path('game-detail/<int:pk>',
         views.DetailView.as_view(),
         name='game_detail'
         ),
    # ゲーム情報投稿ページへのアクセスはCreateGameViewを実行
    path('post/', views.CreateGameView.as_view(), name='post'),
    # 投稿成功ページへのアクセスはPostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    # カテゴリごとのゲーム情報一覧ページへのアクセスはCategoryViewを実行
    path('games/<int:category>',
         views.CategoryView.as_view(),
         name='games_cat'
         ),
    # ユーザーごとのゲーム情報一覧ページへのアクセスはUserViewを実行
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'
         ),
    # マイページへのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    # ゲーム削除ページへのアクセスはGameDeleteViewを実行
    path('game/<int:pk>/delete/', views.GameDeleteView.as_view(), name='game_delete'),
    # お問い合わせページへのアクセスはContactViewを実行
    path('contact/', views.ContactView.as_view(), name='contact'),
    # コメント投稿ページへのアクセスはCreateCommentViewを実行
    path('comment/<int:pk>', views.CreateCommentView.as_view(), name='comments'),
]
