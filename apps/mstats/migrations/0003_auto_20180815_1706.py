# Generated by Django 2.0.2 on 2018-08-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mstats', '0002_auto_20180815_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLConfigSource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('host', models.CharField(max_length=32, verbose_name='地址')),
                ('port', models.IntegerField(default=3306, verbose_name='端口')),
                ('envi', models.SmallIntegerField(default=1, verbose_name='0: 线下其他环境，1：test环境，2：Staging环境 3：生产环境')),
                ('is_master', models.SmallIntegerField(default=1, verbose_name='0：从库（用于查询）， 1：主库（用于审核）')),
                ('comment', models.CharField(max_length=128, null=True, verbose_name='主机描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '数据库主机配置',
                'verbose_name_plural': '数据库主机配置',
                'db_table': 'auditsql_mysql_config',
                'default_permissions': (),
            },
        ),
        migrations.AlterField(
            model_name='mysqlschemainfo',
            name='envi',
            field=models.SmallIntegerField(default=1, verbose_name='0: 线下其他环境，1：test环境，2：Staging环境 3：生产环境'),
        ),
        migrations.AlterUniqueTogether(
            name='mysqlconfigsource',
            unique_together={('host', 'port')},
        ),
    ]