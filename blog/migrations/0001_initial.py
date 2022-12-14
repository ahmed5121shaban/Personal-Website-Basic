# Generated by Django 4.1 on 2022-08-15 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=10000)),
                ('imag', models.ImageField(upload_to='post/%y/%m/%d')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
