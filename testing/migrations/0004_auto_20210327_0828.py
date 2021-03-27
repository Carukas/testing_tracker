# Generated by Django 3.1.6 on 2021-03-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_auto_20210327_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipas', models.CharField(max_length=300)),
                ('value', models.CharField(max_length=300)),
                ('dienu_skaicius', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='tipas',
            field=models.CharField(default='00000', max_length=300),
        ),
        migrations.AlterField(
            model_name='tracking_entry',
            name='asmens_kodas',
            field=models.CharField(default='00000', max_length=20),
        ),
    ]