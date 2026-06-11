import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_NgyQDO85mBko@ep-dark-block-aqtjpr2x-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

df = pd.read_excel("Book5.xlsx")

df = df.rename(columns={
    "First Name": "first_name",
    "Last Name": "last_name",
    "Title": "title",
    "Company Name": "company_name",
    "Email": "email",
    "Industry": "industry",
    "City": "city",
    "State": "state",
    "Country": "country"
})

df = df[
    [
        "first_name",
        "last_name",
        "title",
        "company_name",
        "email",
        "industry",
        "city",
        "state",
        "country"
    ]
]

df.to_sql(
    "leads",
    engine,
    if_exists="append",
    index=False
)

print("Leads imported successfully!")