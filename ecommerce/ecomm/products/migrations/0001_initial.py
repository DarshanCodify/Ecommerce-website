# Generated by Django 5.0.3 on 2024-04-10 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category_image', models.ImageField(upload_to='categories')),
            ],
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('Product_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('price', models.IntegerField()),
                ('product_description', models.TextField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('image', models.ImageField(upload_to='product')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product')),
            ],
            bases=('base.basemodel',),
        ),
    ]
