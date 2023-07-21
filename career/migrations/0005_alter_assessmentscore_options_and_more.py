# Generated by Django 4.2.3 on 2023-07-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0004_alter_assessmentscore_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assessmentscore',
            options={'ordering': ['grade_level', 'session_term']},
        ),
        migrations.AlterUniqueTogether(
            name='assessmentscore',
            unique_together={('subject', 'session_term', 'grade_level')},
        ),
    ]