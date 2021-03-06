# Generated by Django 2.2.4 on 2020-11-07 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0010_auto_20201002_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.CharField(max_length=30, verbose_name='Social Network')),
                ('username', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('dateCreated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='', verbose_name='default.jpg')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='tipoUser',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tipouser',
            name='user',
        ),
        migrations.DeleteModel(
            name='FollowersRelation',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='TipoUser',
        ),
    ]
