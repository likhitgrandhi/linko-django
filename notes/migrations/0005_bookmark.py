# Generated by Django 3.0.7 on 2020-06-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=250)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]