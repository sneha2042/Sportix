# Generated by Django 3.2.3 on 2021-08-16 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportix', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=1000000, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=1000000, null=True),
        ),
    ]