import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Database connection
DATABASE_URL = "postgresql://neondb_owner:npg_NgyQDO85mBko@ep-dark-block-aqtjpr2x-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

# Page config
st.set_page_config(page_title="Lead Intelligence Dashboard")

st.title("Lead Intelligence Dashboard")

# Add Lead Form
st.subheader("Add New Lead")

with st.form("add_lead_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    title = st.text_input("Title")
    company_name = st.text_input("Company Name")
    email = st.text_input("Email")
    industry = st.text_input("Industry")
    city = st.text_input("City")
    state = st.text_input("State")
    country = st.text_input("Country")

    submitted = st.form_submit_button("Save Lead")

    if submitted:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    INSERT INTO leads
                    (first_name, last_name, title, company_name, email, industry, city, state, country)
                    VALUES
                    (:first_name, :last_name, :title, :company_name, :email, :industry, :city, :state, :country)
                """),
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "title": title,
                    "company_name": company_name,
                    "email": email,
                    "industry": industry,
                    "city": city,
                    "state": state,
                    "country": country
                }
            )
            conn.commit()

        st.success("Lead added successfully!")

# Load data from PostgreSQL
df = pd.read_sql(
    "SELECT * FROM leads",
    engine
)

# Search
search = st.text_input(
    "Search by Name, Company, Title, Industry"
)

if search:
    results = df[
        df.astype(str)
        .apply(
            lambda row: row.str.contains(
                search,
                case=False,
                na=False
            ).any(),
            axis=1
        )
    ]
else:
    results = df

st.write(f"Found {len(results)} leads")

st.dataframe(results) 