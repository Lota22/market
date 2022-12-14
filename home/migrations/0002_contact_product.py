# Generated by Django 4.1.2 on 2022-10-18 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Updated', 'Updated'), ('Completed', 'Completed')], default='New', max_length=50)),
                ('sent', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_r', models.CharField(max_length=50)),
                ('img_r', models.ImageField(default='product.jpg', upload_to='Product')),
                ('price', models.FloatField()),
                ('max_quantity', models.IntegerField()),
                ('min_quantity', models.IntegerField()),
                ('size', models.IntegerField()),
                ('display', models.BooleanField()),
                ('shoes', models.BooleanField()),
                ('bags', models.BooleanField()),
                ('perfume', models.BooleanField()),
                ('cloth', models.BooleanField()),
                ('uploaded', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
                'db_table': 'product',
                'managed': True,
            },
        ),
    ]
