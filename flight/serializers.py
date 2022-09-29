from rest_framework import serializers
from .models import Flight, Passenger, Reservation



class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = (
            "flight_number",
            "operating_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )
        
class PassengerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Passenger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    
    passenger = PassengerSerializer(many=True, required=True)
    flight = serializers.StringRelatedField()     # default read_only=True
    flight_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField()     # default read_only=True
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",  # GET
            "flight_id",  # POST
            "user",  # GET
            "user_id",  # POST
            "passenger"
        )