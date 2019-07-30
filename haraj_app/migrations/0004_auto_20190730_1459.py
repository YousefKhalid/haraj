# Generated by Django 2.2.3 on 2019-07-30 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('haraj_app', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='picture',
            field=models.ImageField(default=1, upload_to='haraj_pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add',
            name='publish_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]