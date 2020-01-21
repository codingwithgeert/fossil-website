# Generated by Django 2.0.2 on 2020-01-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=250)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='EUR Order Total')),
                ('email', models.EmailField(blank=True, max_length=250, verbose_name='Email Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billing_name', models.CharField(blank=True, max_length=250)),
                ('billing_address1', models.CharField(blank=True, max_length=250)),
                ('billing_city', models.CharField(blank=True, max_length=250)),
                ('billing_postcode', models.CharField(blank=True, max_length=250)),
                ('billing_country', models.CharField(blank=True, max_length=250)),
                ('shipping_name', models.CharField(blank=True, max_length=250)),
                ('shipping_adress1', models.CharField(blank=True, max_length=250)),
                ('shipping_city', models.CharField(blank=True, max_length=250)),
                ('shipping_postcode', models.CharField(blank=True, max_length=250)),
                ('shipping_country', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
    ]
