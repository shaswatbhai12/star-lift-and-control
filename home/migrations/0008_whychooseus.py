# Generated by Django 5.1.6 on 2025-03-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='why_choose_us/icons/')),
            ],
        ),
    ]
