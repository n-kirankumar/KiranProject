# mobile application
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
    import os
except Exception as er:
    print("Missing Libraries",er)

# initilise the app & api
app = Flask(__name__)
api = Api(app)

Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"

# disable sqlalchemy pool using NullPool as by default Postgres has its own pool
engine = create_engine(database_url, echo=True, poolclass=NullPool)

conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


class Table2(Base):
    __tablename__ = "table2"
    Name = Column("name", String)
    Mob = Column("mob", String, primary_key=True)
    Email = Column("email", String)
    Full_addr = Column("full_addr", String)


@app.route('/printtable2', methods=['GET'])
def home():
    try:
        result = session.query(Table2).all()
        result = [item.__dict__ for item in result]
        return str(result)
    except Exception as err:
        session.rollback()


@app.route('/printtable2singlerecord', methods=['GET'])
def getSingleRecord():
    try:
        result = session.query(Table2).filter(Table2.Mob == request.args.get('mobileNO')).all()
        result = [item.__dict__ for item in result]
        return str(result)
    except Exception as er:
        session.rollback()


@app.route('/table2selectedrecord', methods=['GET'])
def getMultipleRecord():
    # http://127.0.0.1:5000/table2selectedrecord?mobileNo=1234,5647
    var2 = [int(numbers) for numbers in request.args.get('mobileNo').split(",")]
    result = session.query(Table2).filter(Table2.Mob.in_(var2)).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)


@app.route('/table2startswithrecord', methods=['GET'])
def getStartsRecord():
    # http://127.0.0.1:5000/table2startswithrecord?name=kir
    var3 = request.args.get('name')
    # 'Joh%' - Matches with Johnson John Hohnavi...
    result = session.query(Table2).filter(Table2.Name.like(var3 + '%')).all()  # 'kiran'+'%' --> "kiran%"
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)


@app.route('/table2multifetchrecord', methods=['GET'])
def getMultiFetchRecord():
    # http://127.0.0.1:5000/table2multifetchrecord?name=kiran&mobile=1234
    var4 = request.args.get('name')
    var5 = request.args.get('mobile')
    result = session.query(Table2).filter(or_(Table2.Name == var4, Table2.Mob == var5)).all()
    print(type(result))
    result = [item.__dict__ for item in result]
    return str(result)


app.run(debug=False)
