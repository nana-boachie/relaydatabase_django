# Generated by Django 5.0.7 on 2024-08-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relays', '0002_rename_relays_relay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relay',
            name='manufacturer',
            field=models.CharField(choices=[('sel', 'SEL'), ('micom', 'MiCOM')], default='sel', max_length=30),
        ),
    ]
