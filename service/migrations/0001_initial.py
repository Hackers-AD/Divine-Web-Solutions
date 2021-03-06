# Generated by Django 2.2.7 on 2020-01-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='service_files')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.FileField(upload_to='service_logos')),
                ('description', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('files', models.ManyToManyField(blank=True, to='service.Servicefile')),
            ],
        ),
    ]
