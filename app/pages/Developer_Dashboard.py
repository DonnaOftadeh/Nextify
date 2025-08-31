import streamlit as st
import pandas as pd

st.set_page_config(page_title="Developer Dashboard", page_icon="🛠", layout="wide")

st.title("Developer Dashboard v0")
st.caption("Demo data – view only, not editable yet.")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/all_experiment_view.csv")
    except Exception:
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.info("No data available.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Run Count", f"{df['Run'].nunique()}")
    col2.metric("Avg LLM Score", f"{df['LLM Score'].mean():.2f}")
    col3.metric("Avg Human Score", f"{df['Human Score'].mean():.2f}")
    st.markdown("### Raw Data")
    st.dataframe(df, use_container_width=True)
