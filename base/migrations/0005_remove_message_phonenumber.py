# Generated by Django 4.1.3 on 2022-12-02 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_message_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='phonenumber',
        ),
    ]
