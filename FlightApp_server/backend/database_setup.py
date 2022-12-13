from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base()


class Crew(Base):
    __tablename__ = 'crew'
    crew_id = Column(Integer, primary_key=True)
    crew_code = Column(String(50), nullable=False)

class Crew_flight(Base):
    __tablename__ = 'crew_flight'
    crew_flight_id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey("flight.flight_id"))
    crew_id = Column(Integer, ForeignKey("crew.crew_id"))

class Flight(Base):
    __tablename__ = 'flight'
    flight_id = Column(Integer, primary_key=True)
    location_from = Column(String(50), nullable=False)
    location_to = Column(String(50), nullable=False)
    date_from = Column(String(50), nullable=False)
    date_to = Column(String(50), nullable=False)
    time_from = Column(String(50), nullable=False)
    time_to = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)

class Crew_member(Base):
    __tablename__ = 'crew_member'
    crew_user_id = Column(Integer, primary_key=True)
    crew_id = Column(Integer, ForeignKey("crew.crew_id"))
    user_id = Column(Integer, ForeignKey("user.user_id"))

class Crew_member_in_reserve(Base):
    __tablename__ = 'crew_member_in_reserve'
    crew_in_reserve_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    reserve_id = Column(Integer, ForeignKey("reserve.reserve_id"))

class Reserve(Base):
    __tablename__ = 'reserve'
    reserve_id = Column(Integer, primary_key=True)
    reserve_date = Column(String(50), nullable=False)
    airport = Column(String(50), nullable=False)

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    role = Column(String(50), primary_key=True) # admin, pilot, attendant
    first_name = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=False)
    birth_date = Column(String(50), nullable=True)
    user_login = Column(String(50), nullable=False)
    salary = Column(String(50), nullable=True)
    status = Column(String(50), nullable=True)

class Pilot_Certification(Base):
    __tablename__ = 'pilot_certification'
    pilot_cert_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    category = Column(String(50), nullable=False)
    last_date = Column(String(50), nullable=False)
    next_date = Column(String(50), nullable=False)

class Medical_Exam(Base):
    __tablename__ = 'medical_exam'
    med_exam_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    last_date = Column(String(50), nullable=False)
    next_date = Column(String(50), nullable=False)

class Attendant_Certification(Base):
    __tablename__ = 'attendant_certification'
    attendant_cert_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    category = Column(String(50), nullable=False)
    last_date = Column(String(50), nullable=False)
    next_date = Column(String(50), nullable=False)


def load():
    engine = create_engine('sqlite:///flightapp.db')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    session.query(Crew).delete()
    session.query(Flight).delete()
    session.query(Crew_flight).delete()
    session.query(Crew_member_in_reserve).delete()
    session.query(Crew_member).delete()
    session.query(Reserve).delete()
    session.query(User).delete()
    session.query(Attendant_Certification).delete()
    session.query(Pilot_Certification).delete()
    session.query(Medical_Exam).delete()
    session.commit()

    data = pd.read_csv("../crew.csv", sep=';')
    for i in range(len(data)):
        record = Crew(**{'crew_id': int(data.loc[i][0]),
                         'crew_code': data.loc[i][1]})
        session.add(record)
    data = pd.read_csv("../flight.csv", sep=';')
    for i in range(len(data)):
        record = Flight(**{'flight_id': int(data.loc[i][0]),
                         'location_from': data.loc[i][1],
                         'location_to': data.loc[i][2],
                        'date_from': data.loc[i][3],
                        'date_to': data.loc[i][4],
                        'time_from': data.loc[i][5],
                        'time_to': data.loc[i][6],
                        'status': data.loc[i][7]}
        )
        session.add(record)
    data = pd.read_csv("../crew_flight.csv", sep=';')
    for i in range(len(data)):
        record = Crew_flight(**{'crew_flight_id': int(data.loc[i][0]),
                         'flight_id': int(data.loc[i][1]),
                        'crew_id': int(data.loc[i][2])})
        session.add(record)
    data = pd.read_csv("../crew_member.csv", sep=';')
    for i in range(len(data)):
        record = Crew_member(**{'crew_user_id': int(data.loc[i][0]),
                         'crew_id': int(data.loc[i][1]),
                        'user_id': int(data.loc[i][2])})
        session.add(record)
    data = pd.read_csv("../crew_member_in_reserve.csv", sep=';')
    for i in range(len(data)):
        record = Crew_member_in_reserve(**{'crew_in_reserve_id': int(data.loc[i][0]),
                         'user_id': int(data.loc[i][1]),
                        'reserve_id': int(data.loc[i][2])})
        session.add(record)
    data = pd.read_csv("../reserve.csv", sep=';')
    for i in range(len(data)):
        record = Reserve(**{'reserve_id': int(data.loc[i][0]),
                         'reserve_date': data.loc[i][1],
                        'airport': data.loc[i][2]})
        session.add(record)
    data = pd.read_csv("../user.csv", sep=';')
    for i in range(len(data)):
        record = User(**{'user_id': int(data.loc[i][0]),
                         'username': data.loc[i][1],
                         'password': data.loc[i][2],
                         'role': data.loc[i][3],
                         'first_name': data.loc[i][4],
                         'second_name': data.loc[i][5],
                         'birth_date': data.loc[i][6],
                         'user_login': data.loc[i][7],
                         'salary': data.loc[i][8],
                        'status': data.loc[i][9]})
        session.add(record)
    data = pd.read_csv("../pilot_sertification.csv", sep=';')
    for i in range(len(data)):
        record = Pilot_Certification(**{'pilot_cert_id': int(data.loc[i][0]),
                             'user_id': int(data.loc[i][1]),
                             'category': data.loc[i][2],
                             'last_date': data.loc[i][3],
                             'next_date': data.loc[i][4]})
        session.add(record)
    data = pd.read_csv("../attendant_sertification.csv", sep=';')
    for i in range(len(data)):
        record = Attendant_Certification(**{'attendant_cert_id': int(data.loc[i][0]),
                             'user_id': int(data.loc[i][1]),
                             'category': data.loc[i][2],
                             'last_date': data.loc[i][3],
                             'next_date': data.loc[i][4]})
        session.add(record)
    data = pd.read_csv("../medical_exam.csv", sep=';')
    for i in range(len(data)):
        record = Medical_Exam(**{'med_exam_id': int(data.loc[i][0]),
                             'user_id': int(data.loc[i][1]),
                             'last_date': data.loc[i][2],
                             'next_date': data.loc[i][3]})
        session.add(record)


    session.commit()
    session.close()

#load()
