# FastAPI Supabase Auth API

An asynchronous REST API built with FastAPI and SQLAlchemy (AsyncPG) demonstrating authentication integration with Supabase PostgreSQL.

## Features

- Asynchronous Architecture: High-performance async database sessions using asyncpg.
- Supabase Integration: Connects to Supabase PostgreSQL using connection pooling.
- Secure Configuration: Environment-based settings managed via .env files to prevent secret leakage.

## Setup & Local Development

1. Clone the repository:
   git clone git@github.com:Phvl-0/fastapi-supabase-auth.git
   cd fastapi-supabase-auth

2. Set up environment variables:
   Create a .env file in the root directory:
   DATABASE_URL="postgresql+asyncpg://postgres.<ref>:<password>@<host>:6543/postgres?prepared_statement_cache_size=0"

3. Install dependencies & run:
   pip install -r requirements.txt
   uvicorn main:app --reload
