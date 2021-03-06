# Generated by Django 3.0.4 on 2020-03-25 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.IntegerField(blank=True, default=0, null=True, verbose_name='confirmed')),
                ('death', models.IntegerField(blank=True, default=0, null=True, verbose_name='death')),
                ('recovered', models.IntegerField(blank=True, default=0, null=True, verbose_name='recovered')),
                ('created_at', models.DateField(verbose_name='created at')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='longitude')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.Country')),
            ],
        ),
    ]
