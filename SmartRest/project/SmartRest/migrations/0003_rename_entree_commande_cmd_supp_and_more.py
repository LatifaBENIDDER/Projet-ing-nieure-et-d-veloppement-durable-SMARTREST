# Generated by Django 4.0.4 on 2022-04-25 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmartRest', '0002_alter_commande_date_commanded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='entree',
            new_name='cmd_supp',
        ),
        migrations.RenameField(
            model_name='commande',
            old_name='date_delivery',
            new_name='delivery_date',
        ),
        migrations.RenameField(
            model_name='commande',
            old_name='commentaire',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='commande',
            old_name='principal',
            new_name='votre_cmd',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='date_commanded',
        ),
    ]