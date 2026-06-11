from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_NgyQDO85mBko@ep-dark-block-aqtjpr2x-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("Database connected successfully!")