# Generated by Django 4.0.1 on 2022-01-23 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_data', models.DateField(auto_now_add=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_comment', to='book.book')),
            ],
        ),
    ]
