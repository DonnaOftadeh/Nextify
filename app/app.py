import asyncio
import streamlit as st
from fpdf import FPDF
from agent_runner import run_parallel_agents

st.set_page_config(
    page_title="Nextify",
    page_icon="🤖",
    layout="wide",
)

if "stage" not in st.session_state:
    st.session_state.stage = "landing"


def create_pdf(text: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    return pdf.output(dest="S").encode("latin-1")


def show_landing():
    st.title("Nextify")
    st.write("AI-powered innovation lab. Choose your path to begin.")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    if col1.button("🚀 I have an idea"):
        st.session_state.user_mode = "Idea";
        st.session_state.stage = "chat"
    if col2.button("📈 I know the industry"):
        st.session_state.user_mode = "Industry";
        st.session_state.stage = "chat"
    if col3.button("🔍 Explore breakthroughs"):
        st.session_state.user_mode = "Explore";
        st.session_state.stage = "chat"
    if col4.button("🛠 Improve a product"):
        st.session_state.user_mode = "Improve";
        st.session_state.stage = "chat"
    st.sidebar.page_link("pages/Developer_Dashboard.py", label="Developer Dashboard")
    st.page_link("pages/Developer_Dashboard.py", label="👩‍💻 Developer Dashboard")


def show_chat():
    st.title("Nextify Agent Lab")
    st.write(f"Mode: **{st.session_state.get('user_mode','')}**")
    company = st.text_input("Company name")
    product = st.text_area("Product idea or industry", height=150)
    run = st.button("Run Agents")
    if run and company and product:
        with st.spinner("Running parallel agents..."):
            results = asyncio.run(
                run_parallel_agents(company, product, st.session_state.get("user_mode", "Idea"))
            )
        entry = results.pop("entry", "")
        report = [f"Company: {company}", f"Product: {product}", ""]
        if entry:
            with st.chat_message("assistant"):
                st.markdown(entry)
            report.append(f"entry: {entry}")
        for name, output in results.items():
            with st.chat_message("assistant"):
                st.markdown(f"### {name.capitalize()}\n{output}")
            report.append(f"{name}: {output}")
        pdf_bytes = create_pdf("\n".join(report))
        st.success("Analysis complete.")
        st.download_button("Download PDF", data=pdf_bytes, file_name="nextify_report.pdf", mime="application/pdf")
        if st.button("Start over"):
            st.session_state.stage = "landing"
    else:
        st.info("Enter company and product, then click **Run Agents**.")
        st.sidebar.page_link("pages/Developer_Dashboard.py", label="Developer Dashboard")


if st.session_state.stage == "landing":
    show_landing()
else:
    show_chat()
