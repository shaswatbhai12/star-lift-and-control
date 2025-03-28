# Generated by Django 5.1.6 on 2025-03-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_whychooseus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/')),
                ('feedback', models.TextField()),
                ('rating', models.IntegerField(default=5)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
