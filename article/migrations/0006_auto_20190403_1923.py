# Generated by Django 2.0.3 on 2019-04-03 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]