# Generated by Django 3.2.5 on 2022-01-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0195_group_type_name"),
    ]

    operations = [
        migrations.RemoveConstraint(model_name="propertydefinition", name="property_type_and_format_are_valid",),
        migrations.AlterField(
            model_name="propertydefinition",
            name="property_type_format",
            field=models.CharField(
                blank=True,
                choices=[
                    ("unix_timestamp", "Unix Timestamp in seconds"),
                    ("unix_timestamp_milliseconds", "Unix Timestamp in milliseconds"),
                    ("YYYY-MM-DDThh:mm:ssZ", "YYYY-MM-DDThh:mm:ssZ"),
                    ("YYYY-MM-DD hh:mm:ss", "YYYY-MM-DD hh:mm:ss"),
                    ("DD-MM-YYYY hh:mm:ss", "DD-MM-YYYY hh:mm:ss"),
                    ("YYYY-MM-DD", "YYYY-MM-DD"),
                    ("rfc_822", "day, DD MMM YYYY hh:mm:ss TZ"),
                    ("YYYY/MM/DD hh:mm:ss", "YYYY/MM/DD hh:mm:ss"),
                    ("DD/MM/YYYY hh:mm:ss", "DD/MM/YYYY hh:mm:ss"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddConstraint(
            model_name="propertydefinition",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("property_type__in", ["DateTime", "String", "Numeric", "Boolean"]),
                        (
                            "property_type_format__in",
                            [
                                "unix_timestamp",
                                "unix_timestamp_milliseconds",
                                "YYYY-MM-DDThh:mm:ssZ",
                                "YYYY-MM-DD hh:mm:ss",
                                "DD-MM-YYYY hh:mm:ss",
                                "YYYY-MM-DD",
                                "rfc_822",
                                "YYYY/MM/DD hh:mm:ss",
                                "DD/MM/YYYY hh:mm:ss",
                            ],
                        ),
                    )
                ),
                name="property_type_and_format_are_valid",
            ),
        ),
    ]