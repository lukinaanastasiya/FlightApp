from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)


class CrewSchema(ma.Schema):
    class Meta:
        fields = ('crew_id', 'crew_code')


class FlightSchema(ma.Schema):
    class Meta:
        fields = ('flight_id', 'location_from', 'location_to', 'date_from', 'date_to', 'time_from', 'time_to', 'status')


class Crew_flightSchema(ma.Schema):
    class Meta:
        fields = ('crew_flight_id', 'flight_id', 'crew_id')

class Crew_memberSchema(ma.Schema):
    class Meta:
        fields = ('crew_user_id', 'crew_id', 'user_id')

class Crew_member_in_reserveSchema(ma.Schema):
    class Meta:
        fields = ('crew_in_reserve_id', 'user_id', 'reserve_id')

class ReserveSchema(ma.Schema):
    class Meta:
        fields = ('reserve_id', 'reserve_date', 'airport')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'username', 'password', 'role', 'first_name', 'second_name', 'birth_date', 'user_login', 'salary', 'status')

class Pilot_CertificationSchema(ma.Schema):
    class Meta:
        fields = ('pilot_cert_id', 'user_id', 'category', 'last_date', 'next_date')

class Medical_ExamSchema(ma.Schema):
    class Meta:
        fields = ('med_exam_id', 'user_id', 'last_date', 'next_date')

class Attendant_CertificationSchema(ma.Schema):
    class Meta:
        fields = ('attendant_cert_id', 'user_id', 'category', 'last_date', 'next_date')


crew_schema = CrewSchema(many=True)
flight_schema = FlightSchema(many=True)
crew_flight_schema = Crew_flightSchema(many=True)
crew_member_schema = Crew_memberSchema(many=True)
crew_member_in_reserve_schema = Crew_member_in_reserveSchema(many=True)
reserve_schema = ReserveSchema(many=True)
user_schema = UserSchema(many=True)
pilot_cert_schema = Pilot_CertificationSchema(many=True)
med_exam_schema = Medical_ExamSchema(many=True)
attendant_cert_schema = Attendant_CertificationSchema(many=True)
