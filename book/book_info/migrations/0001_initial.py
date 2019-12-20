import book_info.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类名称',
                'verbose_name_plural': '分类名称',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='图书名称')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('price', models.FloatField(verbose_name='价格')),
                ('picture', models.ImageField(null=True, upload_to=book_info.models.get_img_path, verbose_name='图书封面')),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_info.Cate', verbose_name='分类')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
    ]
