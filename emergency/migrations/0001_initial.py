# Generated by Django 4.2.20 on 2025-04-18 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('severity', models.CharField(choices=[('Critical', 'Critical'), ('Moderate', 'Moderate'), ('Mild', 'Mild')], max_length=50)),
                ('arrival_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FirstAidInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TriageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('triage_notes', models.TextField()),
                ('triaged_by', models.CharField(max_length=255)),
                ('triage_time', models.DateTimeField(auto_now_add=True)),
                ('emergency_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergency.emergencycase')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=255)),
                ('reason', models.TextField()),
                ('referred_on', models.DateTimeField(auto_now_add=True)),
                ('emergency_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergency.emergencycase')),
            ],
        ),
    ]
