# Generated by Django 3.0.4 on 2020-03-26 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('covid19', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='covid', to='contact.Country', verbose_name='countries'),
        ),
    ]
