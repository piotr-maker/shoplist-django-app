# Generated by Django 4.0.4 on 2022-05-12 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoplistapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='meals',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shoplistapp.category'),
        ),
    ]
