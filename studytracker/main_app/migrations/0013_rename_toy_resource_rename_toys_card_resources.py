# Generated by Django 4.0.6 on 2022-07-13 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_rename_name_card_goal_alter_feeding_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toy',
            new_name='Resource',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='toys',
            new_name='resources',
        ),
    ]
