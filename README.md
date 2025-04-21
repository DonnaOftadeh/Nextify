# 🧠 Nextify — Modular, Multi-Agent Product Strategy Assistant

**Nextify** is your product management brain — upgraded. It’s a modular, multi-agent system built to assist (and often outperform) traditional PM workflows. Designed during the Google GenAI Capstone, Nextify started with prompt evaluation but now powers a full AI-driven feature and roadmap engine.

It intelligently generates product features, ICE scores, OKRs, strategic roadmaps, competitive insights, and even multi-format storytelling — while grounding recommendations in prompts, agents, and (soon) embeddings.

---

## 🔍 What Does It Do?

- ✅ Evaluate prompt strategies across LLM runs and human feedback
- 🔁 Compare Zero-Shot, Few-Shot, Chain-of-Thought, ReAct, and more
- 🧠 Generate structured product strategy outputs:
  - Mission & Vision
  - Feature Prioritization (ICE)
  - Strategic Roadmaps (short/mid/long-term)
  - SMART OKRs
  - Next-level innovation
- 🧩 Modular agent design — agents for feature ideation, roadmap planning, OKR writing, feedback parsing, and competitive analysis
- 📦 Multi-format output generation (JSON, text, blog post, video outline)

---

## 📊 Live Interactive Dashboard

Deployed on [Render.com](https://render.com), the dashboard lets you:

- Filter by `Company`, `Strategy`, `Prompt Tag`, or `Run`
- View evaluation tables with LLM & Human scores
- See full LLM outputs (in Markdown or JSON mode)
- Track score trends across runs
- Expand feedback and lessons per prompt
- Explore placeholder tabs for:
  - 🧬 Embedding-based similarity (coming)
  - 🤖 Agent evaluations (multi-agent chain visibility)

### ➡️ [View the Live Dashboard](https://nextify-dashboard.onrender.com)

---

## 📁 Project Structure

```
productify-next/
├── app/
│   └── app.py                  # Streamlit dashboard logic
├── data/
│   └── all_experiment_view.csv  # Evaluation data across runs
├── prompts/
│   └── prompt_outputs.json     # Raw prompt + response archives
├── requirements.txt
└── README.md
```

---

## 🧪 Prompting Framework

Supports side-by-side comparison of:
- Zero-shot
- Few-shot
- Chain-of-Thought (CoT)
- Tree-of-Thought
- ReAct
- Combined approaches

Each strategy logs:
- Prompt content
- LLM-generated output
- Self-evaluation (LLM score)
- Human evaluation
- Feedback + lessons

---

## 🧠 Future Modules

| Component           | Status     | Description |
|---------------------|------------|-------------|
| Embedding Explorer  | 🛠️ in progress | Document-level product understanding |
| Multi-Agent Orchestration | 🛠️ prototyping | Role-based agent chains for PM tasks |
| Fine-tuning Stub    | ✅ planned  | Dataset formatter for continued LLM training |
| Real-Time Interface | 🧪 demo     | Goal: Reactive prompt + feedback loop |

---

## 🛠️ Local Run

```bash
pip install -r requirements.txt
streamlit run app/app.py
```
Here you can find the dashboard link to streamlit dashboard:
https://nextify-dashboard-100.streamlit.app/
---

## 📚 License

MIT — feel free to fork, remix, and evolve the PM workflow of the future.
