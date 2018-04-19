from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shared.permissions import PublicEndpoint


class SpeedSensor(APIView):
    """
    The speed sensor controls the car's speed.
    """
    permission_classes = (PublicEndpoint,)

    def get(self, request):
        json = {
            "sensor_name": "speed_sensor",
            "x": 100,
            "y": 100,
            "demo": True
        }
        return Response(json, status=status.HTTP_200_OK)


class UltrasonicSensor(APIView):
    """
    Ultrasonic sensor view gets data from the ultrasonic sensor.
    """
    permission_classes = (PublicEndpoint,)

    def get(self, request):
        json = {
            "sensor_name": "ultrasonic_sensor",
            "x": 100,
            "y": 100,
            "demo": True
        }
        return Response(json, status=status.HTTP_200_OK)


class DemoSensor(APIView):
    """
    Just a demo sensor, demonstrating that everything is working.
    """
    permission_classes = (PublicEndpoint,)

    def get(self, request):
        json = {
            "sensor_name": "demo_sensor",
            "x": 100,
            "y": 100,
            "demo": True
        }
        return Response(json, status=status.HTTP_200_OK)