# Generated by Django 2.1.2 on 2018-11-10 20:26

from django.db import migrations, models

def create_configs(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Configuration = apps.get_model("booru", "Configuration")
    Configuration.objects.using(db_alias).create(code_name="terms_of_service", value="")
    Configuration.objects.using(db_alias).create(code_name="privacy_policy", value="")

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_configs),
    ]