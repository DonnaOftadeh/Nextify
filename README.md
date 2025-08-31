# 🧠 Nextify — Modular, Multi-Agent Product Strategy Assistant

**Nextify** is a lightweight demo showing how AI agents can guide product ideation.
The repo now includes a simple landing page, a chat-style agent walkthrough that
fires all bundled agents in parallel, and a read-only developer dashboard.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
streamlit run app/Nextify_home_page.py
```

On launch you'll see the HTML landing page:
1. Choose a path (idea, industry, explore, improve).
2. Enter a company and product idea, then run the agents.
3. Watch each agent's output stream in and download a PDF summary.
4. Use the *Developer Dashboard* button to inspect evaluation data (demo only).

---

## 📁 Project Structure
```
Nextify/
├── app/
│   ├── Nextify_home_page.py    # HTML landing + agent walkthrough
│   ├── app.py                  # Legacy landing + chat interface
│   ├── agent_runner.py         # Loads prompts and runs agents in parallel
│   ├── static/
│   │   └── home.html           # User-provided landing page HTML
│   └── pages/
│       └── Developer_Dashboard.py  # Simple, view-only dashboard
├── data/
│   └── all_experiment_view.csv  # Evaluation data
├── notebooks/
│   └── nextify_user_walkthrough.ipynb
├── prompts/
└── requirements.txt
```

---

## 🛠️ Notes
- PDF export uses `fpdf` and contains a minimal text summary.
- The developer dashboard is an early preview and not editable.
- Agent steps are illustrative; plug in your own logic or model calls.

---

## 📚 License
MIT — feel free to fork and evolve.
