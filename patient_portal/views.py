from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from patients.models import Patient, TestResult, Appointment
from patients.serializers import TestResultSerializer, AppointmentSerializer

@api_view(['GET'])
def retrieve_medical_records(request, patient_id):
    """
    Returns all MedicalRecord entries for this patient.
    (You can swap in your MedicalRecord model/serializer if needed.)
    """
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    # Assuming you have a MedicalRecord model/serializer:
    records = patient.medical_records.all()
    from patients.serializers import MedicalRecordSerializer
    data = MedicalRecordSerializer(records, many=True).data
    return Response({"patient": patient.full_name(), "medical_records": data})


@api_view(['GET'])
def retrieve_test_results(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    results = TestResult.objects.filter(patient=patient)
    data = TestResultSerializer(results, many=True).data
    return Response({"patient": patient.full_name(), "test_results": data})


@api_view(['GET'])
def retrieve_appointments(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    appts = Appointment.objects.filter(patient=patient)
    data = AppointmentSerializer(appts, many=True).data
    return Response({"patient": patient.full_name(), "appointments": data})


@api_view(['POST'])
def schedule_appointment(request):
    """
    Expected payload:
    {
      "patient_id": 1,
      "appointment_date": "2025-04-20T10:00:00Z",
      "doctor_name": "Dr. Smith",
      "purpose_of_visit": "Annual checkup"
    }
    """
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
