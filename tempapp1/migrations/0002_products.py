# Generated by Django 3.2.7 on 2021-10-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('unitprice', models.IntegerField(default=0)),
            ],
        ),
    ]