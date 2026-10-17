<picture><source media="(prefers-color-scheme: light)" srcset="assets/sketchbook/header-animated-light.svg"><img src="assets/sketchbook/header-animated-dark.svg" width="100%" alt="Arnav's notebook: Computer Engineering at NMIMS, Mumbai; AI and backend development. An illustrated desk scene with a laptop, dumbbell, badminton racket, drink, and headphones; a small mountain-and-coast study and Formula 1 car, with a notebook side margin, handwritten annotation arrows, and an animated name reveal."></picture>

I'm **Arnav Deshpande**, a Computer Engineering student at **NMIMS, Mumbai**. Most of my work is in Python: AI applications, retrieval systems, and backend APIs.

[Email](mailto:deshpandearnavn@gmail.com) · [LinkedIn](https://www.linkedin.com/in/arnav-deshpande-35251b202/)

## A few projects

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/andy1924/CARRICK"><picture><source media="(prefers-color-scheme: light)" srcset="assets/sketchbook/carrick-light.png"><img src="assets/sketchbook/carrick.png" width="100%" alt="CARRICK: a sketch of a crane beside a project schedule. Open the repository."></picture></a>
<p>Connects infrastructure field reports to schedule activities. AI proposes matches; planners review the changes before export.</p>
<p><sub>Python · SQLite · RAG</sub><br><a href="https://github.com/andy1924/CARRICK/blob/main/docs/architecture/system.md">Architecture</a> · <a href="https://github.com/andy1924/CARRICK/tree/main/tests">Tests</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/andy1924/UdyogSaarthi"><picture><source media="(prefers-color-scheme: light)" srcset="assets/sketchbook/udyog-light.png"><img src="assets/sketchbook/udyog.png" width="100%" alt="UdyogSaarthi: a sketch of a village shop. Open the repository."></picture></a>
<p>A team project for rural entrepreneurs: multilingual business planning, financial calculations, feasibility checks, and project reports.</p>
<p><sub>FastAPI · PostgreSQL / PostGIS · React · Celery</sub><br><a href="https://github.com/andy1924/UdyogSaarthi/blob/main/docs/systemDesign.md">System design</a> · <a href="https://github.com/andy1924/UdyogSaarthi/blob/main/docs/apiDocs.md">API</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/andy1924/Graph-RAG"><picture><source media="(prefers-color-scheme: light)" srcset="assets/sketchbook/graph-light.png"><img src="assets/sketchbook/graph.png" width="100%" alt="Graph-RAG: a sketched network of connected nodes. Open the repository."></picture></a>
<p>Co-authored research comparing multimodal, graph-based retrieval with a chunk-based RAG baseline. Includes an evaluation pipeline and benchmark results.</p>
<p><sub>Python · Neo4j · ChromaDB</sub><br><a href="https://github.com/andy1924/Graph-RAG/blob/main/docs/ARCHITECTURE.md">Architecture</a> · <a href="https://github.com/andy1924/Graph-RAG/blob/main/docs/EVALUATION.md">Evaluation</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/andy1924/The-First-Six-Overs"><picture><source media="(prefers-color-scheme: light)" srcset="assets/sketchbook/cricket-light.png"><img src="assets/sketchbook/cricket.png" width="100%" alt="The First Six Overs: a sketched cricket ball and 1,227 IPL matches. Open the repository."></picture></a>
<p>I used ball-by-ball data from 1,227 IPL matches to look at toss effects, powerplay runs, and wickets.</p>
<p><sub>R · Cricsheet · hypothesis testing · regression</sub><br><a href="https://github.com/andy1924/The-First-Six-Overs/blob/main/analysis.md">Findings</a> · <a href="https://github.com/andy1924/The-First-Six-Overs/blob/main/R/01_analysis.R">Analysis</a></p>
</td>
</tr>
</table>

Also: **[AtlasAI](https://github.com/andy1924/AtlasAI)**. I led AI/ML on this team logistics prototype, working on a LangGraph agent, retrieval memory, and carrier forecasting. The fleet dashboard uses simulated vessel positions.

<details>
<summary>Implementation notes & research results</summary>

### CARRICK

XER exports pass a parser round trip. Independent Oracle P6 import remains an external acceptance check. [Export and verification details](https://github.com/andy1924/CARRICK/tree/main/tests).

### Graph-RAG

The repository reports these aggregate benchmark results:

| Metric | GraphRAG | Chunk-based baseline |
| --- | ---: | ---: |
| Hallucination rate | 0.33% | 2.04% |
| Mean response time | 6.00 s | 4.02 s |
| Semantic similarity | 0.5881 | 0.8308 |

Lower hallucination rate came with higher latency and lower semantic similarity in this experiment. Results depend on the corpus, metric definitions, and evaluation setup. Retrieval F1 uses different definitions across the pipelines and should not be treated as a direct comparison.

[Results and limitations](https://github.com/andy1924/Graph-RAG#current-results-snapshot-repository-json) · [Benchmark data](https://github.com/andy1924/Graph-RAG/blob/main/results/visual_output/tab1_aggregate_metrics.csv)

</details>

I'm open to **AI, backend, and full-stack engineering opportunities**. [Get in touch](mailto:deshpandearnavn@gmail.com).
