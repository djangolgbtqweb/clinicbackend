from django.core.management.base import BaseCommand
from resource_management.models import Ward

DEFAULT_WARDS = [
    # inpatient
    {'name': 'ICU', 'ward_type': 'ICU', 'capacity': 5},
    {'name': 'HDU', 'ward_type': 'HDU', 'capacity': 6},
    {'name': 'General Ward', 'ward_type': 'GENERAL', 'capacity': 10},
    {'name': 'Surgical Ward', 'ward_type': 'SURGICAL', 'capacity': 10},
    {'name': 'Maternity Ward', 'ward_type': 'MATERNITY', 'capacity': 8},
    {'name': 'NICU', 'ward_type': 'NICU', 'capacity': 6},
    {'name': 'Pediatric Ward', 'ward_type': 'PEDIATRIC', 'capacity': 8},
    {'name': 'Isolation Ward', 'ward_type': 'ISOLATION', 'capacity': 4},
    {'name': 'Psychiatric Ward', 'ward_type': 'PSYCHIATRIC', 'capacity': 6},
    {'name': 'Burn Unit', 'ward_type': 'BURN', 'capacity': 4},
    {'name': 'PACU', 'ward_type': 'PACU', 'capacity': 6},
    # outpatient support (capacity 0 = no beds)
    {'name': 'Consultation Rooms', 'ward_type': 'CONSULT', 'capacity': 0},
    {'name': 'Procedure Rooms', 'ward_type': 'PROCEDURE', 'capacity': 0},
    {'name': 'Triage / Observation', 'ward_type': 'TRIAGE', 'capacity': 6},
    {'name': 'Pharmacy Area', 'ward_type': 'PHARMACY', 'capacity': 0},
    {'name': 'Imaging / Radiology', 'ward_type': 'IMAGING', 'capacity': 0},
    {'name': 'Dialysis Station', 'ward_type': 'DIALYSIS', 'capacity': 4},
    {'name': 'Support / Sterile Processing', 'ward_type': 'SUPPORT', 'capacity': 0},
]

class Command(BaseCommand):
    help = "Create default wards (if they do not exist) and auto-generate beds."

    def handle(self, *args, **options):
        created = 0
        for w in DEFAULT_WARDS:
            ward, was_created = Ward.objects.get_or_create(
                name=w['name'],
                defaults={
                    'ward_type': w['ward_type'],
                    'capacity': w['capacity'],
                    'active': True
                }
            )
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"Created ward {ward.name} capacity={ward.capacity}"))
            else:
                # update capacity if different (optional)
                if ward.capacity != w['capacity']:
                    ward.capacity = w['capacity']
                    ward.save()
                    self.stdout.write(self.style.WARNING(f"Updated capacity for {ward.name} -> {ward.capacity}"))
        self.stdout.write(self.style.SUCCESS(f"Done. Created/updated wards."))