import asyncio
import pathlib

import streamlit as st
from fpdf import FPDF

from agent_runner import run_parallel_agents

st.set_page_config(page_title="Nextify", page_icon="🤖", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "landing"
if "mode" not in st.session_state:
    st.session_state.mode = ""

def _create_pdf(text: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    return pdf.output(dest="S").encode("latin-1")

def show_landing() -> None:
    """Render static HTML landing page and mode buttons."""
    home_path = pathlib.Path("app/static/home.html")
    if home_path.exists():
        st.components.v1.html(home_path.read_text(), height=600, scrolling=True)
    else:
        st.title("Nextify")
        st.write("AI-powered innovation lab. Choose your path to begin.")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    if col1.button("🚀 I have an idea"):
        st.session_state.mode = "Idea"
        st.session_state.page = "chat"
    if col2.button("📈 I know the industry"):
        st.session_state.mode = "Industry"
        st.session_state.page = "chat"
    if col3.button("🔍 Explore breakthroughs"):
        st.session_state.mode = "Explore"
        st.session_state.page = "chat"
    if col4.button("🛠 Improve a product"):
        st.session_state.mode = "Improve"
        st.session_state.page = "chat"
    st.sidebar.page_link("pages/Developer_Dashboard.py", label="Developer Dashboard")

def show_chat() -> None:
    st.title("Nextify Agent Lab")
    st.write(f"Mode: **{st.session_state.mode}**")
    company = st.text_input("Company name")
    product = st.text_area("Product idea or industry", height=150)
    run = st.button("Run Analysis")
    if run:
        if company and product:
            with st.spinner("Running parallel agents..."):
                results = asyncio.run(
                    run_parallel_agents(company, product, st.session_state.mode)
                )
            entry = results.pop("entry", "")
            report = [f"Company: {company}", f"Product: {product}", ""]
            if entry:
                with st.chat_message("assistant"):
                    st.markdown(entry)
                report.append(f"entry: {entry}")
            total = len(results)
            progress = st.progress(0)
            for i, (name, output) in enumerate(results.items(), 1):
                with st.chat_message("assistant"):
                    st.markdown(f"### {name.capitalize()}\n{output}")
                report.append(f"{name}: {output}")
                progress.progress(i / total)
            pdf_bytes = _create_pdf("\n".join(report))
            st.success("Analysis complete.")
            st.download_button("Download PDF", data=pdf_bytes, file_name="nextify_report.pdf", mime="application/pdf")
            if st.button("Start over"):
                st.session_state.page = "landing"
        else:
            st.warning("Please fill out both fields before running.")
    st.sidebar.page_link("pages/Developer_Dashboard.py", label="Developer Dashboard")

if st.session_state.page == "landing":
    show_landing()
else:
    show_chat()
