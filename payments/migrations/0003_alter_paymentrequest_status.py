# Generated by Django 4.1.9 on 2024-05-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrequest',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled'), ('REFUNDED', 'Refunded'), ('EXPIRED', 'Expired')], default='PENDING', max_length=20),
        ),
    ]