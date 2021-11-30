# Generated by Django 3.1.4 on 2021-05-02 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20210106_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followings',
            name='following_user',
        ),
        migrations.AddField(
            model_name='followings',
            name='following_users',
            field=models.ManyToManyField(blank=True, related_name='following_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posting', to='network.posts')),
                ('watcher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
