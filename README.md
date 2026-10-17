# Hey, I'm Arnav 👋

**Building useful things with AI, Python, and a healthy amount of curiosity.**<br>
Computer Engineering student at **NMIMS, Mumbai**, working across applied AI, backend systems, and full-stack development.

I enjoy turning messy, real-world problems into software people can use — from helping planners make sense of site updates to helping entrepreneurs explore a business idea. Lately, that means retrieval-augmented generation (RAG), AI agents, and the APIs and interfaces that bring them to life.

Around here, you'll also find cricket rabbit holes, research experiments, and a few projects that started with “what if?”

[Say hello](mailto:deshpandearnavn@gmail.com) · [LinkedIn](https://www.linkedin.com/in/arnav-deshpande-35251b202/) · [Explore my projects](#a-few-things-ive-built)

<p align="center">
  <img src="assets/cover.jpg" alt="Vintage Indian print-inspired banner reading Arnav Deshpande, with a tiger in headphones and a vinyl record." width="440">
</p>

## A few things I've built

Infrastructure, entrepreneurship, and AI research: different problems, plenty to learn from each.

### 🏗️ [CARRICK](https://github.com/andy1924/CARRICK)

**Helping site updates find their place in a project schedule.** A runnable Python application where AI connects field reports to schedule activities and planners review the proposed changes before export.

- **Built with:** Python, SQLite, optional RAG, and browser-based capture and review.
- **Under the hood:** project-level access controls, source evidence, conflict checks, and XER/CSV exports. XER output passes a parser round trip; independent Oracle P6 import is still an external acceptance check.

[System architecture](https://github.com/andy1924/CARRICK/blob/main/docs/architecture/system.md) · [AI retrieval design](https://github.com/andy1924/CARRICK/blob/main/docs/architecture/ai-rag.md) · [Verification suites](https://github.com/andy1924/CARRICK/blob/main/tests/README.md) · [API implementation](https://github.com/andy1924/CARRICK/tree/main/services/api)

### 🌱 [UdyogSaarthi](https://github.com/andy1924/UdyogSaarthi)

**Giving a business idea a clearer path forward.** A team-built multilingual platform for rural entrepreneurs, covering feasibility, finance, compliance, and a Detailed Project Report.

- **Built with:** FastAPI, PostgreSQL/PostGIS, Redis, Celery, React, and TypeScript.
- **Under the hood:** financial calculations, applicant/reviewer/auditor roles, geospatial feasibility, and asynchronous PDF generation.

[System design](https://github.com/andy1924/UdyogSaarthi/blob/main/docs/systemDesign.md) · [API contract](https://github.com/andy1924/UdyogSaarthi/blob/main/docs/apiDocs.md) · [Backend tests](https://github.com/andy1924/UdyogSaarthi/tree/main/backend/tests) · [CI workflow](https://github.com/andy1924/UdyogSaarthi/blob/main/.github/workflows/ci.yml)

### 🔎 [Graph-RAG](https://github.com/andy1924/Graph-RAG)

**Exploring how AI can give better-grounded answers.** I co-authored this research project comparing multimodal, graph-based retrieval with a chunk-based RAG baseline.

- **Built with:** Python, Neo4j, ChromaDB, and LLM APIs.
- **Under the hood:** PDF/text ingestion, knowledge graphs, grounded generation, and evaluations of answer quality, hallucinations, latency, and statistical significance.

[Architecture](https://github.com/andy1924/Graph-RAG/blob/main/docs/ARCHITECTURE.md) · [Evaluation methodology](https://github.com/andy1924/Graph-RAG/blob/main/docs/EVALUATION.md) · [Experiments](https://github.com/andy1924/Graph-RAG/tree/main/experiments)

<details>
<summary><strong>Curious about the results? Here's what we found.</strong></summary>

The repository reports these aggregate benchmark results:

| Metric | GraphRAG | Chunk-based baseline |
| --- | ---: | ---: |
| Hallucination rate | 0.33% | 2.04% |
| Mean response time | 6.00 s | 4.02 s |
| Semantic similarity | 0.5881 | 0.8308 |

Lower hallucination rate came with higher latency and lower semantic similarity in this experiment. Results depend on the corpus, metric definitions, and evaluation setup. Retrieval F1 uses different definitions across the pipelines and should not be treated as a direct comparison.

[Results and limitations](https://github.com/andy1924/Graph-RAG#current-results-snapshot-repository-json) · [Benchmark data](https://github.com/andy1924/Graph-RAG/blob/main/results/visual_output/tab1_aggregate_metrics.csv)

</details>

**Also on my workbench: [AtlasAI](https://github.com/andy1924/AtlasAI)** 🚢 — I led AI/ML on this team logistics prototype, bringing together a [LangGraph agent](https://github.com/andy1924/AtlasAI/blob/main/backend/agent.py), outcome-aware ChromaDB memory, human approval, and a [NumPy LSTM](https://github.com/andy1924/AtlasAI/blob/main/backend/ml/lstm_model.py) for carrier forecasting. The fleet dashboard uses simulated vessel positions.

## A cricket question became a whole repository 🏏

How much do the toss and powerplay really matter? [**The First Six Overs**](https://github.com/andy1924/The-First-Six-Overs) explores **1,227 completed IPL matches** using **R** and Cricsheet ball-by-ball data. Hypothesis tests and logistic regression help me put some numbers behind the cricket debates.

[Read the findings](https://github.com/andy1924/The-First-Six-Overs/blob/main/analysis.md) · [Run the analysis](https://github.com/andy1924/The-First-Six-Overs/blob/main/R/01_analysis.R)

## Beyond the code 🎧

Music is usually on — currently Daniel Caesar. Cricket tends to turn into a data project. And I like building things that give me a reason to learn something new.

## Let's build something

I'm open to **applied AI, backend, and full-stack engineering opportunities**. Have an interesting problem, a project to collaborate on, or a cricket theory to test? I'd love to hear from you.

[**deshpandearnavn@gmail.com**](mailto:deshpandearnavn@gmail.com) · [LinkedIn](https://www.linkedin.com/in/arnav-deshpande-35251b202/) · [All repositories](https://github.com/andy1924?tab=repositories)
