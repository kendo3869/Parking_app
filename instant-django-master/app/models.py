from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """
    
    # サンプル項目1 文字列
    sample_1 = models.CharField(
        verbose_name='サンプル項目1 文字列',
        max_length=20,
        blank=True,
        null=True,
    )

    # サンプル項目2 メモ
    sample_2 = models.TextField(
        verbose_name='サンプル項目2 メモ',
        blank=True,
        null=True,
    )

    # サンプル項目3 整数
    sample_3 = models.IntegerField(
        verbose_name='サンプル項目3 整数',
        blank=True,
        null=True,
    )

    # サンプル項目4 浮動小数点
    sample_4 = models.FloatField(
        verbose_name='サンプル項目4 浮動小数点',
        blank=True,
        null=True,
    )

    # サンプル項目5 固定小数点
    sample_5 = models.DecimalField(
        verbose_name='サンプル項目5 固定小数点',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )

    # サンプル項目6 ブール値
    sample_6 = models.BooleanField(
        verbose_name='サンプル項目6 ブール値',
    )

    # サンプル項目7 日付
    sample_7 = models.DateField(
        verbose_name='サンプル項目7 日付',
        blank=True,
        null=True,
    )

    # サンプル項目8 日時
    sample_8 = models.DateTimeField(
        verbose_name='サンプル項目8 日時',
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（固定）
    sample_9_choice = (
        (1, '選択１'),
        (2, '選択２'),
        (3, '選択３'),
    )

    sample_9 = models.IntegerField(
        verbose_name='サンプル項目9_選択肢（固定）',
        choices=sample_9_choice,
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（マスタ連動）
    sample_10 = models.ForeignKey(
        User,
        verbose_name='サンプル項目10_選択肢（マスタ連動）',
        blank=True,
        null=True,
        related_name='sample_10',
        on_delete=models.SET_NULL,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'

#★★★★★駐車場管理アプリ★★★★★#
##################################
# models.py:MVCﾓﾃﾞﾙのﾓﾃﾞﾙにあたる  #
##################################

# 駐車場情報 テーブル
class Parking_Information(models.Model):

    # 駐車コード
    pa_code = models.CharField(
        verbose_name='駐車コード',
        max_length=3,
    )

    # 駐車場所
    pa_place = models.CharField(
        verbose_name='駐車場所',
        max_length=20,
    )

    # 駐車位置番号
    pa_no = models.IntegerField(
        verbose_name='駐車位置番号',
    )

    # 氏名_1
    name_1 = models.CharField(
        verbose_name='氏名_1',
        max_length=1000,
    )

    # 氏名_2
    name_2 = models.CharField(
        verbose_name='氏名_2',
        max_length=1000,
        blank=True,
        null=True,
    )

    # 駐車代_1
    pa_fee_1 = models.IntegerField(
        verbose_name='駐車代_1',
        blank=True,
        null=True,
    )

    # 駐車代_2
    pa_fee_1 = models.IntegerField(
        verbose_name='駐車代_2',
        blank=True,
        null=True,
    )

    # 色_1
    color_1 = models.CharField(
        verbose_name='色_1',
        max_length=10,
        blank=True,
        null=True,
    )

    # 色_2
    color_2 = models.CharField(
        verbose_name='色_2',
        max_length=10,
        blank=True,
        null=True,
    )

    # 備考
    rem = models.TextField(
        verbose_name='備考',
        max_length=500,
        blank=True,
        null=True,
    )

    # 軽自動車フラグ
    light_car_flg = models.IntegerField(
        verbose_name='軽自動車フラグ',
        default=0,
    )

    class Meta:
        """
        メタ情報として、このモデルクラスに名前を付けている？？？
        """
        verbose_name = '駐車場情報'
        verbose_name_plural = '駐車場情報'


# 利用者情報 テーブル
class User_Information(models.Model):

    # 氏名
    name = models.CharField(
        verbose_name='氏名',
        max_length=1000,
    )

    # 会社名
    co_name = models.CharField(
        verbose_name='会社名',
        max_length=100,
        blank=True,
        null=True,
    )

    # 表示名
    disp_name = models.CharField(
        verbose_name='表示名',
        max_length=16,
    )

    # 略称
    abbreviation = models.CharField(
        verbose_name='略称',
        max_length=14,
    )

    # 住所
    addres = models.TextField(
        verbose_name='住所',
        max_length=100,
        blank=True,
        null=True,
    )

    # 電話番号
    tel = models.IntegerField(
        verbose_name='電話番号',
        blank=True,
        null=True,
    )

    # 駐車コード_1
    pa_code_1 = models.CharField(
        verbose_name='駐車コード_1',
        max_length=3,
    )

    # 駐車コード_2
    pa_code_2 = models.CharField(
        verbose_name='駐車コード_2',
        max_length=3,
    )

    # 駐車コード_3
    pa_code_3 = models.CharField(
        verbose_name='駐車コード_3',
        max_length=3,
    )

    # 駐車コード_4
    pa_code_4 = models.CharField(
        verbose_name='駐車コード_4',
        max_length=3,
    )

    # 駐車コード_5
    pa_code_5 = models.CharField(
        verbose_name='駐車コード_5',
        max_length=3,
    )

    # 駐車場所_1
    pa_place_1 = models.CharField(
        verbose_name='駐車場所_1',
        max_length=20,
        blank=True,
        null=True,
    )

    # 駐車場所_2
    pa_place_2 = models.CharField(
        verbose_name='駐車場所_2',
        max_length=20,
        blank=True,
        null=True,
    )   

    # 駐車場所_3
    pa_place_3 = models.CharField(
        verbose_name='駐車場所_3',
        max_length=20,
        blank=True,
        null=True,
    )

    # 駐車場所_4
    pa_place_4 = models.CharField(
        verbose_name='駐車場所_4',
        max_length=20,
        blank=True,
        null=True,
    )

    # 駐車場所_5
    pa_place_5 = models.CharField(
        verbose_name='駐車場所_5',
        max_length=20,
        blank=True,
        null=True,
    )

    # 駐車代_1
    pa_fee_1 = models.IntegerField(
        verbose_name='駐車代_1',
        blank=True,
        null=True,
    )

    # 駐車代_2
    pa_fee_2 = models.IntegerField(
        verbose_name='駐車代_2',
        blank=True,
        null=True,
    )

    # 駐車代_3
    pa_fee_3 = models.IntegerField(
        verbose_name='駐車代_3',
        blank=True,
        null=True,
    )

    # 駐車代_4
    pa_fee_4 = models.IntegerField(
        verbose_name='駐車代_4',
        blank=True,
        null=True,
    )

    # 駐車代_5
    pa_fee_5 = models.IntegerField(
        verbose_name='駐車代_5',
        blank=True,
        null=True,
    )

    # 車種_1
    car_model_1 = models.CharField(
        verbose_name='車種_1',
        max_length=30,
        blank=True,
        null=True,
    )

    # 車種_2
    car_model_2 = models.CharField(
        verbose_name='車種_2',
        max_length=30,
        blank=True,
        null=True,
    )

    # 車種_3
    car_model_3 = models.CharField(
        verbose_name='車種_3',
        max_length=30,
        blank=True,
        null=True,
    )

    # 車種_4
    car_model_4 = models.CharField(
        verbose_name='車種_4',
        max_length=30,
        blank=True,
        null=True,
    )

    # 車種_5
    car_model_5 = models.CharField(
        verbose_name='車種_5',
        max_length=30,
        blank=True,
        null=True,
    )

    # ナンバープレート_1
    number_plate_1 = models.CharField(
        verbose_name='ナンバープレート_1',
        max_length=5,
        blank=True,
        null=True,
    )

    # ナンバープレート_2
    number_plate_2 = models.CharField(
        verbose_name='ナンバープレート_2',
        max_length=5,
        blank=True,
        null=True,
    )

    # ナンバープレート_3
    number_plate_3 = models.CharField(
        verbose_name='ナンバープレート_3',
        max_length=5,
        blank=True,
        null=True,
    )

    # ナンバープレート_4
    number_plate_4 = models.CharField(
        verbose_name='ナンバープレート_4',
        max_length=5,
        blank=True,
        null=True,
    )

    # ナンバープレート_5
    number_plate_1 = models.CharField(
        verbose_name='ナンバープレート_1',
        max_length=5,
        blank=True,
        null=True,
    )

    # 契約開始日
    ag_start_date = models.DateField(
        verbose_name='契約開始日',
        blank=True,
        null=True,
    )

    # 契約終了日
    ag_end_date = models.DateField(
        verbose_name='契約終了日',
        blank=True,
        null=True,
    )

    # 契約期間
    ag_period = models.IntegerField(
        verbose_name='契約期間',
        blank=True,
        null=True,
    )

    # 契約更新回数
    ag_upd_cnt = models.IntegerField(
        verbose_name='契約更新回数',
        default=0,
    )

    # 備考
    rem = models.TextField(
        verbose_name='備考',
        blank=True,
        null=True,
    )

    # まとめ先払い金額
    pay_upfront_money = models.IntegerField(
        verbose_name='まとめ先払い金額',
        blank=True,
        null=True,
    )

    # まとめ先払いフラグ
    pay_upfront_flg = models.IntegerField(
        verbose_name='まとめ先払いフラグ',
        default=0,
    )

    class Meta:
        """
        メタ情報として、このモデルクラスに名前を付けている？？？
        """
        verbose_name = '利用者情報'
        verbose_name_plural = '利用者情報'