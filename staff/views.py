from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import StaffMember, DutyRoster, LeaveRequest, OnCallSchedule
from .serializers import (
    StaffMemberSerializer,
    DutyRosterSerializer,
    LeaveRequestSerializer,
    OnCallScheduleSerializer,
)


class StaffMemberViewSet(viewsets.ModelViewSet):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer


class DutyRosterViewSet(viewsets.ModelViewSet):
    queryset = DutyRoster.objects.all()
    serializer_class = DutyRosterSerializer


class LeaveRequestViewSet(viewsets.ModelViewSet):
    """
    Allows anyone to GET (list) or POST leave‑requests by supplying a valid `pin`.
    If `?all=true` is present, return every leave request (admin view).
    """
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # 1) If ?all=true is passed, return all leave requests (bypass PIN filter)
        show_all = self.request.query_params.get("all", "").lower()
        if show_all == "true":
            return LeaveRequest.objects.all()

        # 2) Otherwise, fallback to “PIN only” behavior
        pin = self.request.query_params.get("pin")
        if not pin:
            return LeaveRequest.objects.none()
        try:
            staff = StaffMember.objects.get(pin=pin)
        except StaffMember.DoesNotExist:
            return LeaveRequest.objects.none()
        return LeaveRequest.objects.filter(staff_member=staff)

    def create(self, request, *args, **kwargs):
        pin = request.data.get("pin")
        if not pin:
            return Response({"detail": "PIN is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            staff = StaffMember.objects.get(pin=pin)
        except StaffMember.DoesNotExist:
            return Response({"detail": "Invalid PIN"}, status=status.HTTP_401_UNAUTHORIZED)

        # Inject staff_member ID into payload
        data = request.data.copy()
        data["staff_member"] = staff.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class OnCallScheduleViewSet(viewsets.ModelViewSet):
    queryset = OnCallSchedule.objects.all()
    serializer_class = OnCallScheduleSerializer


class StaffPinLoginView(APIView):
    def post(self, request):
        pin = request.data.get("pin")
        if not pin:
            return Response({"error": "PIN is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            staff = StaffMember.objects.get(pin=pin)

            if staff.user is None:
                return Response({"error": "No user associated with this staff member"}, status=status.HTTP_400_BAD_REQUEST)

            user = staff.user

            if not user.is_active:
                return Response({"error": "User account is inactive"}, status=status.HTTP_403_FORBIDDEN)

            # Optionally, you can add authentication here, but JWT tokens generation is fine as is
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "staff_id": staff.id,
                "name": staff.name,
                "role": staff.role,  # could be useful
            }, status=status.HTTP_200_OK)

        except StaffMember.DoesNotExist:
            return Response({"error": "Invalid PIN"}, status=status.HTTP_401_UNAUTHORIZED)