## Journal Insights Service Backend

This is a simple AI chat feature built with GPT-3.5. It's designed as a small addition like adding a little flower to complement the main project, which primarily focuses on frontend development and learning.

## Tech Stack
Framework: FastAPI

Language: Python

AI Integration: OpenAI API (GPT-3.5)

# Installation
```bash

#Navigate into the directory:

cd backend

#Create a virtual environment and activate it:

python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate

#Install dependencies:

pip install -r requirements.txt

#Environment Setup

#Create an .env file at the project root with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


#Running the Application

#Start the FastAPI server:

uvicorn app.main:app --reload

```
The API will be available at http://localhost:8000.


## API Documentation

FastAPI provides automatic interactive documentation accessible via:

Swagger UI: http://localhost:8000/docs

ReDoc UI: http://localhost:8000/redoc

# Deployment
the recommended platform for deploying this backend service is Render - https://render.com/

