# Generated by Django 5.0.4 on 2024-05-15 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_post_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscriber',
        ),
    ]
