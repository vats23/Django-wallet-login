# Generated by Django 3.0.8 on 2020-07-29 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_userprofileinfo_joker'),
    ]

    operations = [
        migrations.CreateModel(
            name='balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('value', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wallet.UserProfileInfo')),
            ],
        ),
    ]