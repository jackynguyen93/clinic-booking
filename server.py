#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
from sqlalchemy import create_engine, DateTime
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Boolean, BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from flask import Flask, make_response, jsonify, request, render_template, redirect,url_for
app = Flask(__name__)
Base = declarative_base()


####################################################################################################
##### Table Def ############
class Packages(Base):
    __tablename__ = 'packages'
    package_id = Column(Integer, primary_key=True, autoincrement=True)
    package_name = Column(String(100), nullable=False)
    package_duration = Column(INTEGER, nullable=False)

class Doctors(Base):
    __tablename__ = 'doctors'
    doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_name = Column(String(100))
    clinic = Column(String(300))
    working_time = Column(String(300))
    appointments = relationship("appointments")

class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_date = Column(DateTime)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    customer_last_name = Column(String(100))
    customer_first_name = Column(String(100))
    customer_email = Column(String(100))
    customer_phone = Column(String(100))
    doctor_request = Column(Integer, ForeignKey('doctors.doctor_id'))
    package_selected = Column(Integer, ForeignKey('packages.package_id'))

####################################################################################################


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/available-calendar/")
def getAvailableCalendar():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=os.environ.get('PORT', 3000), debug=True)
