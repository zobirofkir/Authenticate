from fastapi import FastAPI, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer

SQLALCHEMY_DATABASE_URI = 'sqlite.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


SECRET_KEY = 'voodoo'
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
security = HTTPBearer()
ALGORITHM = "HS256"
ACCESS_TOKEN_EPIRE_MINUTES = 30


Base.metadata.create_all(bind=engine)