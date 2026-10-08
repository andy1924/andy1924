# Arnav Deshpande

**Applied AI · Backend systems · Full-stack engineering**<br>
Computer Engineering student at **NMIMS, Mumbai**.

I work on retrieval-augmented generation (RAG), AI agents, and the APIs and interfaces around them. The part I enjoy most comes after the demo looks convincing: finding out where it breaks and what the evidence actually says.

[Email me](mailto:deshpandearnavn@gmail.com) · [LinkedIn](https://www.linkedin.com/in/arnav-deshpande-35251b202/) · [Selected work](#selected-work)

<p align="center">
  <img src="assets/cover.jpg" alt="Vintage Indian print-inspired banner reading Arnav Deshpande, with a tiger in headphones and a vinyl record." width="560">
</p>

## Selected work

For **backend and full-stack work**, start with UdyogSaarthi. For **AI/ML work**, start with Graph-RAG and AtlasAI. These are team projects; the links below point to implementation and evidence.

### [UdyogSaarthi](https://github.com/andy1924/UdyogSaarthi) — Software for rural entrepreneurs

A multilingual platform that guides a business idea through feasibility, finance, compliance, and a Detailed Project Report.

- **Engineering:** server-side financial calculations, JWT-based applicant/reviewer/auditor roles, geospatial feasibility, and asynchronous PDF generation.
- **Stack:** Python, FastAPI, PostgreSQL/PostGIS, Redis, Celery, React, TypeScript.

[System design](https://github.com/andy1924/UdyogSaarthi/blob/main/docs/systemDesign.md) · [API contract](https://github.com/andy1924/UdyogSaarthi/blob/main/docs/apiDocs.md) · [Backend tests](https://github.com/andy1924/UdyogSaarthi/tree/main/backend/tests) · [CI workflow](https://github.com/andy1924/UdyogSaarthi/blob/main/.github/workflows/ci.yml)

### [Graph-RAG](https://github.com/andy1924/Graph-RAG) — Can a retrieval system earn its confidence?

Co-author of a research project comparing multimodal, graph-based retrieval with a chunk-based RAG baseline.

- **Engineering:** PDF/text ingestion, knowledge-graph construction, grounded generation, and an evaluation pipeline covering answer quality, hallucination metrics, latency, and significance tests.
- **Stack:** Python, Neo4j, ChromaDB, LLM APIs.

[Architecture](https://github.com/andy1924/Graph-RAG/blob/main/docs/ARCHITECTURE.md) · [Evaluation methodology](https://github.com/andy1924/Graph-RAG/blob/main/docs/EVALUATION.md) · [Experiments](https://github.com/andy1924/Graph-RAG/tree/main/experiments)

<details>
<summary><strong>A result worth looking at — including the trade-off</strong></summary>

The repository reports these aggregate benchmark results:

| Metric | GraphRAG | Chunk-based baseline |
| --- | ---: | ---: |
| Hallucination rate | 0.33% | 2.04% |
| Mean response time | 6.00 s | 4.02 s |
| Semantic similarity | 0.5881 | 0.8308 |

Lower hallucination rate came with higher latency and lower semantic similarity in this experiment. Results depend on the corpus, metric definitions, and evaluation setup. Retrieval F1 uses different definitions across the pipelines and should not be treated as a direct comparison.

[Results and limitations](https://github.com/andy1924/Graph-RAG#current-results-snapshot-repository-json) · [Benchmark data](https://github.com/andy1924/Graph-RAG/blob/main/results/visual_output/tab1_aggregate_metrics.csv)

</details>

### [AtlasAI](https://github.com/andy1924/AtlasAI) — AI decisions with an approval path

**AI/ML lead** on a team logistics prototype: detect a disruption, retrieve past actions, propose a response, and escalate when human approval is needed.

- **Engineering:** a LangGraph agent, outcome-aware retrieval memory, operator approval flows, and a dual-head LSTM implemented in NumPy for carrier forecasting.
- **Stack:** Python, FastAPI, LangGraph, ChromaDB, NumPy, Next.js, TypeScript. The fleet dashboard uses simulated vessel positions.

[Agent implementation](https://github.com/andy1924/AtlasAI/blob/main/backend/agent.py) · [NumPy LSTM](https://github.com/andy1924/AtlasAI/blob/main/backend/ml/lstm_model.py) · [Project walkthrough](https://github.com/andy1924/AtlasAI)

## Cricket, with evidence

[**The First Six Overs**](https://github.com/andy1924/The-First-Six-Overs) uses **R** and Cricsheet ball-by-ball data to analyse **1,227 completed IPL matches**. Hypothesis tests and logistic regression examine toss effects, powerplay runs, and wickets. Cricket opinions are plentiful; I wanted a reproducible answer.

[Read the findings](https://github.com/andy1924/The-First-Six-Overs/blob/main/analysis.md) · [Run the analysis](https://github.com/andy1924/The-First-Six-Overs/blob/main/R/01_analysis.R)

## Let's talk

If you're hiring for **applied AI, backend, or full-stack software engineering**, I'd like to hear about the problems your team is working on.

[**deshpandearnavn@gmail.com**](mailto:deshpandearnavn@gmail.com) · [LinkedIn](https://www.linkedin.com/in/arnav-deshpande-35251b202/) · [All repositories](https://github.com/andy1924?tab=repositories)

*Outside the code: music, currently Daniel Caesar. Some cricket questions apparently require an entire repository.*
