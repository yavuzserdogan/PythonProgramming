# Generated by Django 5.0.6 on 2024-05-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("block", "0007_remove_shopping_post_shopping_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="birthday",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="event",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="movie",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="shopping",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
