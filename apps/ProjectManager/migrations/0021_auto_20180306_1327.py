# Generated by Django 2.0.2 on 2018-03-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0020_incepmakeexectask_sql_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incepmakeexectask',
            name='make_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='生成时间'),
        ),
    ]