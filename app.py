from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
import pyshorteners

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:61548",
    "http://127.0.0.1:61548"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PostgreSQL database connection
engine = create_engine('postgresql://postgres:123@localhost:5432/url_shortener')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class URL(Base):
    __tablename__ = 'urls'
    original_url = Column(String)
    short_url = Column(String, primary_key=True)

Base.metadata.create_all(engine)

class URLItem(BaseModel):
    original_url: str

class CustomURLItem(BaseModel):
    original_url: str
    custom_name: str

@app.post("/shorten-custom/")
def shorten_url_custom(url_item: CustomURLItem):
    # Generate a short URL using secrets module
    # short_url = secrets.token_urlsafe(6)
    short_url = "amal.ly/"+ url_item.custom_name
    # Create a new URL object
    url = URL(original_url=url_item.original_url, short_url=short_url)

    # Add the URL to the database
    db = Session()
    db.add(url)
    db.commit()
    db.close()

    # Return the short URL in the response
    return {"short_url": short_url}

@app.post("/shorten/")
def shorten_url(url_item: URLItem):
    short_url = pyshorteners.Shortener().tinyurl.short(url_item.original_url)
    return {"short_url": short_url}

@app.get("/{short_url}")
def redirect_to_original_url(short_url: str):
    db = Session()
    url = db.query(URL).filter_by(short_url=short_url).first()
    db.close()
    if url:
        return RedirectResponse(url.original_url)
    else:
        raise HTTPException(status_code=404, detail="URL not found")