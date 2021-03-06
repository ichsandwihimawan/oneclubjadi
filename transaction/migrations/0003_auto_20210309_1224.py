# Generated by Django 3.1.7 on 2021-03-09 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_auto_20210309_1224'),
        ('transaction', '0002_auto_20210309_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invest',
            name='nama_bank',
        ),
        migrations.RemoveField(
            model_name='invest',
            name='nama_pemilik_rekening',
        ),
        migrations.RemoveField(
            model_name='invest',
            name='no_rekening',
        ),
        migrations.RemoveField(
            model_name='invest',
            name='status_invest',
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal', models.FloatField(blank=True, null=True)),
                ('nama_bank', models.CharField(blank=True, max_length=20, null=True)),
                ('nama_pemilik_rekening', models.CharField(blank=True, max_length=100, null=True)),
                ('no_rekening', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.data_user')),
            ],
        ),
        migrations.CreateModel(
            name='Bonus_Roi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roi', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.data_user')),
            ],
        ),
        migrations.CreateModel(
            name='Bonus_Generasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus', models.FloatField(blank=True, null=True)),
                ('generasi', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.data_user')),
            ],
        ),
    ]
