# Generated by Django 2.2.12 on 2020-09-10 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=10, verbose_name='商品名')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('category', models.CharField(max_length=10, verbose_name='商品类别')),
                ('description', models.TextField(verbose_name='商品描述')),
            ],
        ),
        migrations.CreateModel(
            name='Commodity_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bimages', models.ImageField(null=True, upload_to='', verbose_name='商品图片')),
                ('com', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commodity.Commodity')),
            ],
        ),
    ]
