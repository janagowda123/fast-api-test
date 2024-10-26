from fastapi import FastAPI, HTTPException, Depends
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database connection
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://my_marketing_database_user:YoV1T4eJcHlLsT4943zY40gumECSURE9@dpg-csei6gu8ii6s7394ja50-a.oregon-postgres.render.com/my_marketing_database")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define a simple model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Karnataka 2024 Namma Kannada Namma Hemme"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id, "Hello": "yrutjt"}

@app.post("/send-welcome-email")
async def send_welcome_email(email: str):
    # Gmail account credentials
    sender_email = "janagowda123@gmail.com"
    sender_password = os.environ.get("Tr1p@123")

    if not sender_password:
        raise HTTPException(status_code=500, detail="Gmail app password not set in environment variables")

    # Email content
    subject = "Welcome to Our Microdegree Course!"
    body = """
    Dear Student,

    Welcome to our Microdegree Course! We're excited to have you on board.

    Best regards,
    Your Course Team
    """

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Create a secure SSL context
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
        return {"message": f"Welcome email sent successfully to {email}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

@app.post("/users/")
def create_user(email: str, name: str, db: Session = Depends(get_db)):
    print("name1 ",name, "email : ",email)

    new_user = User(email=email, name=name)
    print("name ",name, "email : ",email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "email": new_user.email, "name": new_user.name}

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "email": user.email, "name": user.name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
