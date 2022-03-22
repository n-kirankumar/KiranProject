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
    print("Install Missing Libraries",er)

app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()


class Table22(Base):
    __tablename__ = "table22"
    date = Column("date",Date)
    Name = Column("name", String)
    Mob = Column("mob", String, primary_key=True)
    Email = Column("email", String)
    Full_addr = Column("full_addr", String)

class Dealer(Base):
    __tablename__= "dealer"
    userName = Column("username",String, primary_key = True)
    passWord = Column("password",String)


@app.route('/sign_in', methods=['GET'])
def home():
    current_date = date.today()
    result = session.query(Dealer).filter(Dealer.userName == request.args.get("username"), Dealer.passWord == request.args.get("password")).all()
    if result:
        yesterday_date = current_date - timedelta(days = 1)
        result1 = session.query(Table22).filter(Table22.date == str(yesterday_date),Table22.Name == request.args.get("name")).all()
        result1 = [i.__dict__ for i in result1]
        return str(result1)

    else:
        return "invalid credentials"

app.run(debug=False)
