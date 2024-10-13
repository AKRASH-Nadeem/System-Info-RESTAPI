from django.urls import path
from monitor.v1 import views as V1Viewsv1

urlpatterns = [
    # Version 1
    path('v1/processes/', V1Viewsv1.SystemMonitorViewSet.as_view({'get': 'list_processes'}), name='process-list'),
    path('v1/cpu/', V1Viewsv1.SystemMonitorViewSet.as_view({'get': 'cpu_usage'}), name='cpu-usage'),
    path('v1/memory/', V1Viewsv1.SystemMonitorViewSet.as_view({'get': 'memory_usage'}), name='memory-usage'),
    path('v1/network/', V1Viewsv1.SystemMonitorViewSet.as_view({'get': 'network_usage'}), name='network-usage'),
    path('v1/temperature/', V1Viewsv1.SystemMonitorViewSet.as_view({'get': 'temperature'}), name='temperature'),
]