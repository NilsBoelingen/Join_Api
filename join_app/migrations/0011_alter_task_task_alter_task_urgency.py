# Generated by Django 5.1.2 on 2024-11-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0010_alter_task_assignedto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='urgency',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]