# Generated by Django 5.1.6 on 2025-03-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_carouselimage_caption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimage',
            name='caption',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='image',
            field=models.ImageField(upload_to='carousel/'),
        ),
    ]
