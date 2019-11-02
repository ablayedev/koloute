# Generated by Django 2.2 on 2019-10-30 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_station', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libre', models.CharField(default='yes', max_length=250)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Station')),
            ],
        ),
    ]
