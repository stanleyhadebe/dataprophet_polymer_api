Polymer Reaction API

A simple FastAPI-based JSON API for ingesting, storing, retrieving, and reacting chemical polymer chains.
Built for the DataProphet backend assignment.

Features

POST /polymers – Store polymer entries with timestamps

GET /polymers – Retrieve raw stored polymers between two timestamps

GET /reactor – React all polymers in a time range and return the final reacted chain

GET /health_check – Check if API + database are healthy

Fully authenticated via Authorization: Bearer <token>

SQLite database using SQLAlchemy ORM

Simple reaction engine following the Aa / aA collapse rules

Setup Instructions
1. Clone the repository
git clone <your-private-repo-url>
cd dataprophet_polymer_api

2. Create a virtual environment
python -m venv venv

3. Activate virtual environment

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Run the server
uvicorn app.main:app --reload
