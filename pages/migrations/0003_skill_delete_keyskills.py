# Generated by Django 5.1.1 on 2024-11-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_keyskills_alter_cvfile_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='KeySkills',
        ),
    ]
