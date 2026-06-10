import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lead Intelligence Dashboard")

st.title("Lead Intelligence Dashboard")

df = pd.read_excel("Book5.xlsx")

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