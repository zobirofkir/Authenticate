from sqlalchemy import Column, String, Integer
from authentication_import import Base, SessionLocal, engine, pwd_context

class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    def verify_password(self, password:str):
        return  pwd_context.verify(password, self.password_hash)
    
