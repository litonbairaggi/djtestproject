# Generated by Django 3.1.7 on 2021-05-11 18:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0007_auto_20210511_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medium',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Bangla', 'Bangla'), ('English', 'English'), ('Hindi', 'Hindi'), ('Spanis', 'bangla')], default='Bangla', max_length=100),
        ),
    ]