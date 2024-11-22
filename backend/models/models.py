from sqlalchemy import MetaData, Table, Integer, Column, String, TIMESTAMP,ARRAY, Boolean, CheckConstraint, Float, ForeignKey
from datetime import datetime

meta_data = MetaData()

user = Table(
    "user",
    meta_data,
    Column("id", Integer, primary_key=True), 
    Column("email", String, nullable = False),
    Column("hashed_password", String, nullable = False),
    Column("username", String, nullable = False),
    Column("wallet_ids", ARRAY(Integer), default=[]),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),  

    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    CheckConstraint("LENGTH(email) >=6 AND LENGTH(email) <=255", name = "email_length_check")
)

wallet = Table(
    "wallet",
    meta_data,
    Column("id", Integer,primary_key=True),
    Column("name", String, nullable=False),
    Column("transaction_ids", ARRAY(Integer), default=[]),
    Column("balance", Float, nullable= False, default=0),
    
)

transaction = Table(
    "transaction",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("category_id", Integer, ForeignKey("category.id"), nullable=False),
    Column("title", String, nullable=False),
    Column("amount", Float, nullable=False),
    Column("date", TIMESTAMP, nullable=False, default=datetime.utcnow),   
)

category = Table(
    "category",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable = False),
    Column("is_income", Boolean, nullable=False),
)