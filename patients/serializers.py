# patients/serializers.py

from rest_framework import serializers
from .models import Patient, Appointment, TestResult, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id","first_name","last_name","date_of_birth","gender",
            "phone_number","email","address","is_active","allergies",
            "blood_type","emergency_contact_name","emergency_contact_phone",
            "is_smoker","is_diabetic","is_pregnant","previous_conditions",
            "created_at","updated_at","full_name",
        ]
        read_only_fields = ["id","created_at","updated_at","full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class AppointmentSerializer(serializers.ModelSerializer):
    # map your frontend field `purpose_of_visit` to the model’s `notes`
    purpose_of_visit = serializers.CharField(source="notes")
    
    # still expose patient name
    patient_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Appointment
        fields = [
            "id",
            "patient",
            "patient_name",
            "appointment_date",
            "purpose_of_visit",   # ← now read/write into the `notes` field
        ]
        read_only_fields = ["patient_name"]

    def get_patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = "__all__"

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ["id","record_type","record_details","date_created"]


