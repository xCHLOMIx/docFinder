# Generated by Django 5.0.6 on 2024-05-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='medical_license_number',
            field=models.CharField(choices=[('GP', 'General Practitioner'), ('P', 'Pediatrician'), ('O', 'Ophthalmologist'), ('D', 'Dermatologist'), ('C', 'Cardiologist')], default='GP', max_length=10),
        ),
    ]
