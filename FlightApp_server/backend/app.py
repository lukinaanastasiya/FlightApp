from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Crew, Flight, Crew_member, User, Medical_Exam, Pilot_Certification, Attendant_Certification
from marshmallow_schemas import app, crew_schema, flight_schema, crew_flight_schema, crew_member_schema, crew_member_in_reserve_schema, reserve_schema, user_schema, pilot_cert_schema, med_exam_schema, attendant_cert_schema
import datetime


engine = create_engine('sqlite:///flightapp.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# вывод всех полетов всех пользователей
@app.route('/all_flights/')
def showFlights():
    flights = session.query(Flight).all()
    return flight_schema.dump(flights)

#вывод всех полетов конкретного пользователя
@app.route('/all_flights/<int:user_id>')
def showFlightsbUserId(user_id):
    flights = session.execute(f"SELECT * from flight where flight_id in (SELECT flight_id from crew_flight where crew_id in (SELECT crew_id from crew_member where user_id = {user_id}))")
    return flight_schema.dump(flights)

# вывод следующего полета конкретного пользователя + расчет количества дней до следующего полета
@app.route('/next_flight/<int:user_id>')
def showNextFlightbyUserId(user_id):
    flights = session.execute(f"SELECT * from flight where flight_id in (SELECT flight_id from crew_flight where crew_id in (SELECT crew_id from crew_member where status='on_going' and user_id = {user_id})) limit 1")
    flight_json = flight_schema.dump(flights)[0]
    flight_json.update({'days_to_flight': abs(datetime.datetime.strptime(flight_json['date_from'], "%d.%m.%Y") - datetime.datetime.now()).days})
    return flight_json


# вывод данных о конкретном пользователе
@app.route('/user_info/<int:user_id>')
def showUserInfobyUserId(user_id):
    user = session.query(User).filter_by(user_id=user_id)
    return user_schema.dump(user)


# вывод данных о мед обследовании конкретного пользователя
@app.route('/med_exam_info/<int:user_id>')
def showMedExamInfobyUserId(user_id):
    med_exam = session.query(Medical_Exam).filter_by(user_id=user_id)
    return med_exam_schema.dump(med_exam)

# вывод данных о лицензии пилота конкретного пользователя
@app.route('/pilot_cert_info/<int:user_id>')
def showPilotCertInfobyUserId(user_id):
    pilot_cert = session.query(Pilot_Certification).filter_by(user_id=user_id)
    return pilot_cert_schema.dump(pilot_cert)

# вывод данных о лицензии стюарда конкретного пользователя
@app.route('/attendant_cert_info/<int:user_id>')
def showAttendantCertInfobyUserId(user_id):
    attendant_cert = session.query(Attendant_Certification).filter_by(user_id=user_id)
    return attendant_cert_schema.dump(attendant_cert)

# вывод данных о полете по его id
@app.route('/flight_info/<int:flight_id>')
def showFlightInfobyFlightId(flight_id):
    flight = session.query(Flight).filter_by(flight_id=flight_id)
    return flight_schema.dump(flight)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

