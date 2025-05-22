from rest_framework import serializers
from .models import Patient, Appointment, TestResult, MedicalRecord
from .serializers import PatientMiniSerializer

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id", "first_name", "last_name", "date_of_birth", "gender",
            "phone_number", "email", "address", "is_active", "allergies",
            "blood_type", "emergency_contact_name", "emergency_contact_phone",
            "is_smoker", "is_diabetic", "is_pregnant", "previous_conditions",
            "created_at", "updated_at", "full_name",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class AppointmentSerializer(serializers.ModelSerializer):
    # ✅ Use nested serializer to return id and full_name
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    doctor_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'patient',  # now returns full_name and id
            'appointment_date',
            'doctor_name',
            'purpose_of_visit',
        ]
        read_only_fields = ['doctor_name']

    def get_doctor_name(self, obj):
        return obj.doctor.name if obj.doctor else None

class TestResultSerializer(serializers.ModelSerializer):
    # alias the internal `notes` field back to `technician_name`
    technician_name = serializers.CharField(source='notes', read_only=True)
    # alias the internal `date_conducted` to `date_of_test` for front-end
    date_of_test = serializers.DateField(source='date_conducted', format='%Y-%m-%d')

    class Meta:
        model = TestResult
        fields = [
            'patient',
            'test_name',
            'result',
            'technician_name',
            'date_of_test',
        ]


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'record_type', 'record_details', 'date_created']

