# Generated by Django 4.2.20 on 2025-04-18 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('last_checked', models.DateField()),
                ('condition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SurgerySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_date', models.DateTimeField()),
                ('surgeon', models.CharField(max_length=255)),
                ('procedure', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='scheduled', max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surgeries', to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PostOpFollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_up_date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('attended', models.BooleanField(default=False)),
                ('surgery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_ups', to='minor_theater.surgeryschedule')),
            ],
        ),
        migrations.CreateModel(
            name='OperationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('outcome', models.CharField(max_length=255)),
                ('performed_by', models.CharField(max_length=255)),
                ('operation_date', models.DateTimeField()),
                ('surgery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operation_records', to='minor_theater.surgeryschedule')),
            ],
        ),
    ]
