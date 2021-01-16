from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    """
    モデルフォーム構成クラス
    ・公式 モデルからフォームを作成する
    https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/
    """

    class Meta:
        model = Item
        fields = '__all__'

        # 以下のフィールド以外が入力フォームに表示される
        # AutoField
        # auto_now=True
        # auto_now_add=Ture
        # editable=False

#★★★★★駐車場管理アプリ★★★★★#
##################################
#      画面の入力欄を作成する      #
##################################

# 新規登録画面-入力欄
class NewRegistForm(forms.Form):
    pa_code  = forms.CharField()
    pa_place = forms.CharField()
    name_1   = forms.CharField()
    name_2   = forms.CharField()
    pa_fee_1 = forms.IntegerField()

#class ViewInformation(froms.Form):
    