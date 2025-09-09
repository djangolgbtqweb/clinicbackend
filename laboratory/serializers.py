from rest_framework import serializers
from .models import LabTest, SampleTracking, LabResult, Patient

class LabTestSerializer(serializers.ModelSerializer):
    # Pull in the related patient's full_name
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = LabTest
        # Explicitly list fields so we can include ordered_date
        fields = [
            'id',
            'patient',        # the ID
            'patient_name',   # the human name
            'test_name',
            'description',
            'cost',
            'ordered_date',
            'status',
        
        ]
class SampleTrackingSerializer(serializers.ModelSerializer):
    # Pull in the patient’s name from the related lab_test → patient
    patient_name = serializers.CharField(
        source='lab_test.patient.full_name',
        read_only=True
    
    )

    class Meta:
        model = SampleTracking
        fields = [
            'id',
            'lab_test',              # FK ID
            'patient_name',          # pulled from related Patient
            'sample_collected_date',
            'sample_received_date',
            'status',
            'notes',
        ]



class LabResultSerializer(serializers.ModelSerializer):
    # Pull test name and patient name from the related LabTest → Patient
    test_name = serializers.CharField(source='lab_test.test_name', read_only=True)
    patient_name = serializers.CharField(source='lab_test.patient.full_name', read_only=True)

    class Meta:
        model = LabResult
        fields = [
            'id',
            'lab_test',       # the numeric FK, if you still need it
            'test_name',      # human‑readable test
            'patient_name',   # human‑readable patient
            'result_date',
            'notes',
        ]
        read_only_fields = ['id', 'test_name', 'patient_name']

class PatientSerializer(serializers.ModelSerializer):
    # If your Patient model already has a `full_name` field, you can
    # simply list it; otherwise compute it from first_name/last_name:
    full_name = serializers.SerializerMethodField()

