# Generated by Django 4.0.2 on 2023-03-10 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movielist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_screening', to='showtimes.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_screening', to='movielist.movie')),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='movies',
            field=models.ManyToManyField(through='showtimes.Screening', to='movielist.Movie'),
        ),
    ]
