# Generated by Django 3.2.24 on 2024-03-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='portafolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]