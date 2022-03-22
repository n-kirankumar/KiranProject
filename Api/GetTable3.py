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
import os

app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()


class Table3(Base):
    __tablename__ = "table3"
    Name = Column("name", String)
    Mob = Column("mob", String, primary_key=True)
    Email = Column("email", String)
    Full_addr = Column("full_addr", String)


@app.route('/printtable3', methods=['GET'])
def home():
    result = session.query(Table3).all()
    result = [item.__dict__ for item in result]
    return str(result)


@app.route('/printtable2singlerecord', methods=['GET'])
def getSingleRecord():
    # http://127.0.0.1:5000/printtable2singlerecord?mobile=1234
    var1 = request.args.get('mobileNO')
    result = session.query(Table3).filter(Table3.Mob == var1).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)


app.run(debug=False)