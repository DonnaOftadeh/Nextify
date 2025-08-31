# 🧠 Nextify — Modular, Multi-Agent Product Strategy Assistant

**Nextify** is a lightweight demo showing how AI agents can guide product ideation.
The repo now includes a simple landing page, a chat-style agent walkthrough, and a
read-only developer dashboard.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

On launch you'll see the landing page:
1. Choose a path (idea, industry, explore, improve).
2. Describe your context and run the agents.
3. Watch placeholder steps stream in and download a PDF summary.
4. Visit the *Developer Dashboard* page for raw evaluation data (demo only).

---

## 📁 Project Structure
```
Nextify/
├── app/
│   ├── app.py                  # Landing + agent walkthrough
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
