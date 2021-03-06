# Generated by Django 2.1.2 on 2020-10-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pa_code', models.CharField(max_length=3, verbose_name='駐車コード')),
                ('pa_place', models.CharField(max_length=20, verbose_name='駐車場所')),
                ('pa_no', models.IntegerField(verbose_name='駐車位置番号')),
                ('name_1', models.CharField(max_length=1000, verbose_name='氏名_1')),
                ('name_2', models.CharField(blank=True, max_length=1000, null=True, verbose_name='氏名_2')),
                ('pa_fee_1', models.IntegerField(blank=True, null=True, verbose_name='駐車代_2')),
                ('color_1', models.CharField(blank=True, max_length=10, null=True, verbose_name='色_1')),
                ('color_2', models.CharField(blank=True, max_length=10, null=True, verbose_name='色_2')),
                ('rem', models.TextField(blank=True, max_length=500, null=True, verbose_name='備考')),
                ('light_car_flg', models.IntegerField(default=0, verbose_name='軽自動車フラグ')),
            ],
        ),
        migrations.CreateModel(
            name='User_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='氏名')),
                ('co_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='会社名')),
                ('disp_name', models.CharField(max_length=16, verbose_name='表示名')),
                ('abbreviation', models.CharField(max_length=14, verbose_name='略称')),
                ('addres', models.TextField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('tel', models.IntegerField(blank=True, null=True, verbose_name='電話番号')),
                ('pa_code_1', models.CharField(max_length=3, verbose_name='駐車コード_1')),
                ('pa_code_2', models.CharField(max_length=3, verbose_name='駐車コード_2')),
                ('pa_code_3', models.CharField(max_length=3, verbose_name='駐車コード_3')),
                ('pa_code_4', models.CharField(max_length=3, verbose_name='駐車コード_4')),
                ('pa_code_5', models.CharField(max_length=3, verbose_name='駐車コード_5')),
                ('pa_place_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='駐車場所_1')),
                ('pa_place_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='駐車場所_2')),
                ('pa_place_3', models.CharField(blank=True, max_length=20, null=True, verbose_name='駐車場所_3')),
                ('pa_place_4', models.CharField(blank=True, max_length=20, null=True, verbose_name='駐車場所_4')),
                ('pa_place_5', models.CharField(blank=True, max_length=20, null=True, verbose_name='駐車場所_5')),
                ('pa_fee_1', models.IntegerField(blank=True, null=True, verbose_name='駐車代_1')),
                ('pa_fee_2', models.IntegerField(blank=True, null=True, verbose_name='駐車代_2')),
                ('pa_fee_3', models.IntegerField(blank=True, null=True, verbose_name='駐車代_3')),
                ('pa_fee_4', models.IntegerField(blank=True, null=True, verbose_name='駐車代_4')),
                ('pa_fee_5', models.IntegerField(blank=True, null=True, verbose_name='駐車代_5')),
                ('car_model_1', models.CharField(blank=True, max_length=30, null=True, verbose_name='車種_1')),
                ('car_model_2', models.CharField(blank=True, max_length=30, null=True, verbose_name='車種_2')),
                ('car_model_3', models.CharField(blank=True, max_length=30, null=True, verbose_name='車種_3')),
                ('car_model_4', models.CharField(blank=True, max_length=30, null=True, verbose_name='車種_4')),
                ('car_model_5', models.CharField(blank=True, max_length=30, null=True, verbose_name='車種_5')),
                ('number_plate_2', models.CharField(blank=True, max_length=5, null=True, verbose_name='ナンバープレート_2')),
                ('number_plate_3', models.CharField(blank=True, max_length=5, null=True, verbose_name='ナンバープレート_3')),
                ('number_plate_4', models.CharField(blank=True, max_length=5, null=True, verbose_name='ナンバープレート_4')),
                ('number_plate_1', models.CharField(blank=True, max_length=5, null=True, verbose_name='ナンバープレート_1')),
                ('ag_start_date', models.DateField(blank=True, null=True, verbose_name='契約開始日')),
                ('ag_end_date', models.DateField(blank=True, null=True, verbose_name='契約終了日')),
                ('ag_period', models.IntegerField(blank=True, null=True, verbose_name='契約期間')),
                ('ag_upd_cnt', models.IntegerField(default=0, verbose_name='契約更新回数')),
                ('rem', models.TextField(blank=True, null=True, verbose_name='備考')),
                ('pay_upfront_money', models.IntegerField(blank=True, null=True, verbose_name='まとめ先払い金額')),
                ('pay_upfront_flg', models.IntegerField(default=0, verbose_name='まとめ先払いフラグ')),
            ],
        ),
    ]
