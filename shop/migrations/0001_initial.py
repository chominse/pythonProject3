# Generated by Django 3.2.13 on 2022-05-30 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ca_id', models.AutoField(primary_key=True, serialize=False)),
                ('ca_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=45)),
                ('post_content', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField()),
                ('post_img', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category')),
            ],
        ),
    ]
