from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView
    Fields that needs to be accepted
    """

    name = serializers.CharField(max_length=10)
