# Generated by Django 2.2.4 on 2020-09-29 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200928_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipoUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='users.TipoUser'),
        ),
    ]
