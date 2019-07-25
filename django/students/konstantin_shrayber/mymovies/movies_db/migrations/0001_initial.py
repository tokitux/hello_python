# Generated by Django 2.2.2 on 2019-06-17 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HollywoodCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('release_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
                ('budget', models.FloatField(validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(1000000000)])),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_db.HollywoodCompany')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(verbose_name='date of birth')),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_role', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_db.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_db.Person')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_db.Role')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_db.Person'),
        ),
    ]