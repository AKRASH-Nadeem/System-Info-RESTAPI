from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from monitor import UtilityFunctions


class SystemMonitorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated
    authentication_classes = [TokenAuthentication]

    def list_processes(self, request):
        return Response(UtilityFunctions.list_processes())

    def cpu_usage(self, request):
        cpu_percent = UtilityFunctions.cpu_usage()
        return Response(cpu_percent)

    def memory_usage(self, request):
        memory = UtilityFunctions.memory_usage()
        return Response(memory)

    def network_usage(self, request):
        net_io = UtilityFunctions.network_usage()
        return Response(net_io)

    def temperature(self, request):
        return Response(UtilityFunctions.temperature())

