from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.shortcuts import redirect, render

from .filters import ItemFilterSet
from .forms import ItemForm
from .models import Item

from django.http.response import HttpResponse

from .models import models
from app.models import User_Information

from .forms import NewRegistForm





# 未ログインのユーザーにアクセスを許可する場合は、LoginRequiredMixinを継承から外してください。
#
# LoginRequiredMixin：未ログインのユーザーをログイン画面に誘導するMixin
# 参考：https://docs.djangoproject.com/ja/2.1/topics/auth/default/#the-loginrequired-mixin

class ItemFilterView(LoginRequiredMixin, FilterView):
    """
    ビュー：一覧表示画面

    以下のパッケージを使用
    ・django-filter 一覧画面(ListView)に検索機能を追加
    https://django-filter.readthedocs.io/en/master/
    """
    model = Item

    # django-filter 設定
    filterset_class = ItemFilterSet
    # django-filter ver2.0対応 クエリ未設定時に全件表示する設定
    strict = False

    # 1ページの表示
    paginate_by = 10

    def get(self, request, **kwargs):
        """
        リクエスト受付
        セッション変数の管理:一覧画面と詳細画面間の移動時に検索条件が維持されるようにする。
        """

        # 一覧画面内の遷移(GETクエリがある)ならクエリを保存する
        if request.GET:
            request.session['query'] = request.GET
        # 詳細画面・登録画面からの遷移(GETクエリはない)ならクエリを復元する
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

    def get_queryset(self):
        """
        ソート順・デフォルトの絞り込みを指定
        """
        # デフォルトの並び順として、登録時間（降順）をセットする。
        return Item.objects.all().order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        表示データの設定
        """
        # 表示データを追加したい場合は、ここでキーを追加しテンプレート上で表示する
        # 例：kwargs['sample'] = 'sample'
        return super().get_context_data(object_list=object_list, **kwargs)


class ItemDetailView(LoginRequiredMixin, DetailView):
    """
    ビュー：詳細画面
    """
    model = Item

    def get_context_data(self, **kwargs):
        """
        表示データの設定
        """
        # 表示データの追加はここで 例：
        # kwargs['sample'] = 'sample'
        return super().get_context_data(**kwargs)


class ItemCreateView(LoginRequiredMixin, CreateView):
    """
    ビュー：登録画面
    """
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        登録処理
        """
        item = form.save(commit=False)
        item.created_by = self.request.user
        item.created_at = timezone.now()
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return HttpResponseRedirect(self.success_url)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    """
    ビュー：更新画面
    """
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        更新処理
        """
        item = form.save(commit=False)
        item.updated_by = self.request.user
        item.updated_at = timezone.now()
        item.save()

        return HttpResponseRedirect(self.success_url)


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    """
    ビュー：削除画面
    """
    model = Item
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        """
        削除処理
        """
        item = self.get_object()
        item.delete()

        return HttpResponseRedirect(self.success_url)

#★★★★★駐車場管理アプリ★★★★★#
##################################
# views.py:MVCﾓﾃﾞﾙのｺﾝﾄﾛｰﾗにあたる #
##################################

# ホーム画面表示処理 #メモ：駐車場情報テーブルからデータを取得し、Templete(html)へ渡す
class View_Home(LoginRequiredMixin, FilterView):
    """
    ビュー：一覧表示画面

    以下のパッケージを使用
    ・django-filter 一覧画面(ListView)に検索機能を追加
    https://django-filter.readthedocs.io/en/master/
    """
    model = Item

    # django-filter 設定
    filterset_class = ItemFilterSet
    # django-filter ver2.0対応 クエリ未設定時に全件表示する設定
    strict = False

    # 1ページの表示
    paginate_by = 10

    def get(self, request, **kwargs):
        """
        リクエスト受付
        セッション変数の管理:一覧画面と詳細画面間の移動時に検索条件が維持されるようにする。
        """

        # 一覧画面内の遷移(GETクエリがある)ならクエリを保存する
        if request.GET:
            request.session['query'] = request.GET
        # 詳細画面・登録画面からの遷移(GETクエリはない)ならクエリを復元する
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

    def get_queryset(self):
        """
        ソート順・デフォルトの絞り込みを指定
        """
        # デフォルトの並び順として、登録時間（降順）をセットする。
        return Item.objects.all().order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        表示データの設定
        """
        # 表示データを追加したい場合は、ここでキーを追加しテンプレート上で表示する
        # 例：kwargs['sample'] = 'sample'
####################################################編集中
        # テーブルのデータを取得
        P_Info_def = models.User_Information.all()
#####################################################
        return super().get_context_data(object_list=P_Info_def, **kwargs)
        #return super().get_context_data(object_list=object_list, **kwargs)


# 新規登録処理　#メモ：画面で入力された値を受け取り、テーブルにレコードを作成
def NewRegist(request):
    form = NewRegistForm()
    #return render(request, "NewRegist.html", {"form": form})

    # 駐車場情報テーブルにレコードを作るための入れ物を用意し、データを詰める。（インスタンス化）
    P_Info = models.Parking_Information(pa_code='a')

    # 駐車場情報テーブルにレコードを作成
    P_Info.save()

# 複数新規登録処理


# 契約更新処理


# 情報閲覧処理 #メモ：画面で選択されたアンカーを元にデータを取得し、返す。
def ViewInformation(request, id):
    
    # 選択した駐車位置ごとにidを受け取り、主キーに合わせて変換
    # 正面駐車場
    if      id==112: 'id = A12'
    elif    id==111: 'id = A11'
    elif    id==110: 'id = A10'
    elif    id==109: 'id = A09'
    elif    id==108: 'id = A08'
    elif    id==107: 'id = A07'
    elif    id==106: 'id = A06'
    elif    id==105: 'id = A05'
    elif    id==103: 'id = A03'
    elif    id==102: 'id = A02'
    elif    id==101: 'id = A01'
    elif    id==100: 'id = A00'
    
    # ロシェフォート駐車場
    elif    id==209: 'id = B09'
    elif    id==210: 'id = B10'
    elif    id==211: 'id = B11'
    elif    id==212: 'id = B12'
    elif    id==213: 'id = B13'
    elif    id==214: 'id = B14'
    elif    id==215: 'id = B15'

    # 対象のレコードを取得
    #U_Info = models.User_Information.Objects.filter(pa_code_1 = id)
    U_Info = User_Information.Objects.filter(pa_code_1 = id)

    return render(request,'view_information.html', U_Info)


