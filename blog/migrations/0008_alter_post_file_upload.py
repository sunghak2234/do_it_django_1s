# Generated by Django 3.2.7 on 2021-09-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d/'),
        ),
    ]
