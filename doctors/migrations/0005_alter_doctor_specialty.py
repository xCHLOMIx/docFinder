# Generated by Django 5.0.6 on 2024-05-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_alter_doctor_medical_license_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(choices=[('General Practitioner', 'General Practitioner'), ('Pediatrician', 'Pediatrician'), ('Ophthalmologist', 'Ophthalmologist'), ('Dermatologist', 'Dermatologist'), ('Cardiologist', 'Cardiologist')], default='General Practitioner', max_length=50),
        ),
    ]
