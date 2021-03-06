# Generated by Django 3.2.6 on 2021-08-23 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('shipment_address', models.CharField(max_length=4)),
                ('amount', models.FloatField()),
                ('pending_amount', models.FloatField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación de la orden')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización de la orden')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.stateproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_value', models.FloatField()),
                ('datetime_payment', models.DateTimeField()),
                ('paymentmethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.paymentmethod')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordermanagement.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordermanagement.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordermanagement.order')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordermanagement.payment')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_product',
            field=models.ManyToManyField(through='ordermanagement.OrderProduct', to='ordermanagement.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.paymentmethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.stateorder'),
        ),
    ]
