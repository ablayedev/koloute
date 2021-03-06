# Generated by Django 2.2 on 2020-01-06 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture', models.CharField(default='', max_length=255)),
                ('zone_champ', models.CharField(default='', max_length=255)),
                ('stade', models.IntegerField(default=0)),
                ('fine', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potential_stress', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stress', models.DecimalField(decimal_places=2, max_digits=5)),
                ('acre_fine', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('acre_potential_stress', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('acre_stress', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
