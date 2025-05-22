from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from patients.models import MedicalRecord

from patients.models import Patient, TestResult, Appointment, MedicalRecord
from patients.serializers import (
    MedicalRecordSerializer,
    TestResultSerializer,
    AppointmentSerializer
)

@api_view(['GET'])
def retrieve_medical_records(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    # filter MedicalRecord by FK
    records = MedicalRecord.objects.filter(patient=patient)
    data    = MedicalRecordSerializer(records, many=True).data

    return Response({
        "patient": f"{patient.first_name} {patient.last_name}",
        "medical_records": data
    })

@api_view(['GET'])
def retrieve_test_results(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"detail": "Patient not found"},
                        status=status.HTTP_404_NOT_FOUND)

    results = TestResult.objects.filter(patient=patient)
    # Build the list with the exact keys your UI needs:
    formatted = [
        {
            "test_name": r.test_name,
            "result":    r.result,
            "date_of_test":    r.date_conducted.isoformat(),
            "technician_name": r.notes or ""
        }
        for r in results
    ]

    return Response({
        "patient":       f"{patient.first_name} {patient.last_name}",
        "test_results":  formatted
    })


@api_view(['GET'])
def retrieve_appointments(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    appts = Appointment.objects.filter(patient=patient)
    data  = AppointmentSerializer(appts, many=True).data

    return Response({
        "patient": f"{patient.first_name} {patient.last_name}",
        "appointments": data
    })

@api_view(['POST'])
def schedule_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_medical_records(request):
    records = MedicalRecord.objects.select_related('patient').all()
    data = [
        {
            'id': r.id,
            'patient_name': f"{r.patient.first_name} {r.patient.last_name}",
            'record_type': r.record_type,
            'description': r.description,
            'created_at': r.created_at,
        }
        for r in records
    ]
    return Response(data)
@api_view(['GET'])
def all_appointments(request):
    """
    Returns every appointment in the system for admin consumption.
    """
    from patients.models import Appointment
    from patients.serializers import AppointmentSerializer

    appts = Appointment.objects.select_related('patient').all()
    serializer = AppointmentSerializer(appts, many=True)
    return Response({
        "appointments": serializer.data
    })
    
@api_view(['GET'])
def patient_test_results(request, patient_id):
    # Load the patient (404 if not found)
    patient = get_object_or_404(Patient, pk=patient_id)
    
    # Fetch all test results for that patient
    results_qs = TestResult.objects.filter(patient=patient)
    
    # Serialize them with your aliased serializer
    serializer = TestResultSerializer(results_qs, many=True)
    
    # Return the full_name plus the array under `test_results`
    return Response({
        'patient': f"{patient.first_name} {patient.last_name}",
        'test_results': serializer.data
    })
