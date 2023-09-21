# Generated by Django 4.2.5 on 2023-09-21 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_section_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='book',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='books.book'),
        ),
        migrations.AlterField(
            model_name='section',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='books.section'),
        ),
    ]
