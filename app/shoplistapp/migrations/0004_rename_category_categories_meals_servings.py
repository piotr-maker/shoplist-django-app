# Generated by Django 4.0.4 on 2022-05-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplistapp', '0003_alter_meals_category_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
        migrations.AddField(
            model_name='meals',
            name='servings',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]