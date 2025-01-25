from rest_framework import serializers

class LeadSerializer(serializers.Serializer):
   
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, required=False,)
    purpose = serializers.CharField(max_length=255, required=False)
    budget = serializers.CharField(max_length=50, required=False)
    message = serializers.CharField(max_length=1000, required=False)
    time_slot = serializers.CharField(max_length=50, required=False)
    experience = serializers.CharField(max_length=50, required=False)
    country = serializers.CharField(max_length=100, required=False)
    state = serializers.CharField(max_length=100, required=False)
    campaign = serializers.CharField(max_length=100, required=False, allow_blank=True)
    adset = serializers.CharField(max_length=100, required=False, allow_blank=True)
    placement = serializers.CharField(max_length=100, required=False, allow_blank=True)
    ad = serializers.CharField(max_length=100, required=False, allow_blank=True)