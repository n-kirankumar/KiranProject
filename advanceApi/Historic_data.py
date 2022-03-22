try:
    import json
    import psycopg2
    from flask import Flask, request
    from flask_restful import Api
    from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.pool import NullPool
    from flask import jsonify
    from datetime import date
    from datetime import timedelta
    import os
except Exception as er:
    print("Missing Libraries",er)

app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()


class Student(Base):
    __tablename__ = "student"
    name = Column("name",String)
    mob = Column("mob", Integer, primary_key=True)
    section = Column ("section",String)
    class1 = Column("class", String)
    date = Column("date", Date)


class Login(Base):
    __tablename__= "login"
    userName = Column("section",String, primary_key = True)
    passWord = Column("password",String)



@app.route('/update', methods = ['PATCH'])
def update():
    result = session.query(Student).filter(Student.mob == request.args.get("name"))


@app.route('/sign_in', methods=['GET'])
def home():
    current_date = date.today()
    try:
        result = session.query(Login).filter(Login.userName == request.args.get("username"), Login.passWord == request.args.get("password")).all()
    except Exception as err:
        session.rollback()

    if result:
        yesterday_date = current_date - timedelta(days = 1)
        try:
            result1 = session.query(Student).filter(Student.date == str(yesterday_date),Student.section == request.args.get("section")).all()
            result1 = [i.__dict__ for i in result1]
            return str(result1)
        except Exception as err:
            session.rollback()
    else:
        return "invalid credentials"


app.run(debug=False)
