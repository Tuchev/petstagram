# Generated by Django 3.0.14 on 2022-04-18 08:26

from django.db import migrations, models
import petstagram.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateTimeField(auto_created=True)),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.main.validators.validate_file_max_size_in_mb])),
                ('description', models.TextField(blank=True, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='main.Pet')),
            ],
        ),
    ]