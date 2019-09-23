# Generated by Django 2.2.1 on 2019-05-24 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecomapp', '0004_auto_20190520_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='ecomapp.CartItem'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('buying_type', models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], max_length=40)),
                ('comments', models.TextField()),
                ('status', models.CharField(choices=[('Оплачен', 'Оплачен'), ('Выполняется', 'Выполняется'), ('Принят в обработку', 'Принят в обработку')], max_length=100)),
                ('items', models.ManyToManyField(to='ecomapp.Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
