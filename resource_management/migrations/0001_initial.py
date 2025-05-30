# Generated by Django 4.2.20 on 2025-04-18 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('room_type', models.CharField(choices=[('Consultation', 'Consultation'), ('Lab', 'Lab'), ('Theater', 'Theater'), ('Inpatient', 'Inpatient')], max_length=50)),
                ('is_occupied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RoomAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=255)),
                ('patient_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource_management.room')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_by', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=100)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource_management.equipment')),
            ],
        ),
    ]
