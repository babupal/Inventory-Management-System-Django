# Generated by Django 3.0.5 on 2020-06-09 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Account_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('credit_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('balance_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=150)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Client')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Transaction')),
            ],
        ),
    ]
