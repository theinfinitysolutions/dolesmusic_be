from rest_framework import serializers

class LeadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.CharField(max_length=15)
    purpose = serializers.CharField(max_length=255, required=False)
    budget = serializers.CharField(max_length=50, required=False)
    message = serializers.CharField(max_length=1000, required=False)
    time_slot = serializers.CharField(max_length=50, required=False, allow_blank=True)
    experience = serializers.CharField(max_length=50, required=False, allow_blank=True)
    country = serializers.CharField(max_length=100, required=False)
    state = serializers.CharField(max_length=100, required=False)
    campaign = serializers.CharField(max_length=100, required=False, allow_blank=True)
    adset = serializers.CharField(max_length=100, required=False, allow_blank=True)
    placement = serializers.CharField(max_length=100, required=False, allow_blank=True)
    ad = serializers.CharField(max_length=100, required=False, allow_blank=True)


class BusinessLeadSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    last_name = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=1000, required=False)
    designation = serializers.CharField(max_length=100, required=False)
    phone_number = serializers.CharField(max_length=15, required=False)


class OldLeadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100, required=False, allow_null=True)
    last_name = serializers.CharField(max_length=100, required=False, allow_null=True)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, required=False)
    purpose = serializers.CharField(max_length=255, required=False)
    budget = serializers.CharField(max_length=50, required=False)
    message = serializers.CharField(max_length=1000, required=False)
    time_slot = serializers.CharField(max_length=50, required=False, allow_blank=True)
    experience = serializers.CharField(max_length=50, required=False, allow_blank=True)
    country = serializers.CharField(max_length=100, required=False)
    state = serializers.CharField(max_length=100, required=False)
    campaign = serializers.CharField(max_length=100, required=False, allow_blank=True)
    adset = serializers.CharField(max_length=100, required=False, allow_blank=True)
    placement = serializers.CharField(max_length=100, required=False, allow_blank=True)
    ad = serializers.CharField(max_length=100, required=False, allow_blank=True)

