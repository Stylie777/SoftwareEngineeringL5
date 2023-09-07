# Generated by Django 4.2.4 on 2023-08-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tickets",
            name="ticket_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="usergroups",
            name="group_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="userpermissions",
            name="permissions_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="users",
            name="user_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
