# Generated by Django 4.0.6 on 2022-07-25 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='first_kin_address',
            field=models.CharField(default='osun', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='first_kin_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_kin_number',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_kin_relation',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lga',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nin_number',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='second_kin_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='second_kin_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='second_kin_number',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='second_kin_relation',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
