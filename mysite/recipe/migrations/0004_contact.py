# Generated by Django 4.1.2 on 2022-11-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20211101_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('Email', models.CharField(max_length=122)),
                ('Message', models.TextField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
