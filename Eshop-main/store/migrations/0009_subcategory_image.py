# Generated by Django 4.2.7 on 2023-12-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]
