# Generated by Django 4.2.7 on 2023-11-26 11:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('biograph', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='books/')),
                ('info', models.TextField(verbose_name="Info's book")),
                ('price', models.FloatField()),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_auther', to='temp.auther')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_review', to='temp.books')),
            ],
        ),
    ]