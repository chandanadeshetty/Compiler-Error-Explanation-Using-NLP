# INTELLIFIX: AI-Assisted Compiler Error Explanation & Auto-Fix Engine

An advanced, offline compiler diagnostic tool that converts dense and cryptic Python tracebacks into highly interactive, automated hot-fixes. Utilizing a powerful hybrid architecture of **Abstract Syntax Tree (AST) Symbolic Extraction** and **Natural Language Processing (Ollama LLM)**, this engine acts as a 5-quadrant local Web IDE capable of resolving runtime logic, scanning for severe security vulnerabilities, and actively measuring hardware computational efficiency via simulated Green IT telemetry.

---

## ⚡ Key Features

* **Hybrid Error-Extraction Engine:** Does not rely solely on probabilistic, hallucination-prone AI. Intecepts Python Tracebacks mathematically using native AST node-trees, only calling Local AI variables when deterministic heuristics are bypassed.
* **5-Quadrant Web IDE:** A beautiful, responsive frontend grid offering completely localized file workspaces, execution terminals, and automated code editors.
* **Sandboxed Runtime Interpreter:** Re-executes buggy scripts locally in an `exec()` envelope safely guarded by `contextlib` routing, ensuring dangerous infinite loops or thread bombs never crack the host Flask server.
* **Pre-Execution Vulnerability Scanning:** A native Static Security Module that physically traverses your raw code attempting to block `os.system` injections, legacy `mktemp()` exploits, and hardcoded `api_key` patterns *before* memory execution occurs.
* **Green IT Profiling Telemetry:** Actively correlates execution compilation times into robust ecological footprints mirroring enterprise *CodeCarbon* output (µg CO2 eq) and *RAPL* computational power usages (mJ).

---

## 🏗️ Project Architecture & File Structure

The project maintains a rigorously decoupled MVC environment spanning API gateways and individual Python processing scripts:

```text
CompilerErrorExplanationNLP/
│
├── gui.py                  # Secondary execution portal suppressing Flask terminal log noise
├── app.py                  # The Flask API Gateway (Handles all File I/O, Error Routing, and Green Metrics generation)
├── security_analyzer.py    # Analyzes the raw AST of test-files specifically for critical code injections
├── error_extractor.py      # Captures tracebacks securely via redirected stdout execution blocks
├── nlp_explainer.py        # The Core Intelligence Engine. Attempts LLM connection, falls back to strict Regex Matrices
├── evaluation.py           # Grades the accuracy of generated fixes using Sequence/Format matching matrices
│
├── templates/
│   └── index.html          # The dynamic, CSS-Grid powered 5-Quadrant local web dashboard
│
└── test*.py                # Various structured execution payloads mimicking large-scale logic crashes
```

---

## ⚙️ Installation & Prerequisites

This system is built entirely on native libraries with a few specific requirements. 

**1. Clone the repository and navigate inside:**
```bash
cd CompilerErrorExplanationNLP
```

**2. Install Core Python Dependencies:**
Ensure Python 3.10+ is installed on your system.
```bash
pip install flask requests
```

**3. (Optional but Recommended) Install Ollama:**
The engine boasts a powerful local Natural Language Generator. If you choose to enable the AI text-generator, you must have [Ollama](https://ollama.com/) running locally.
```bash
# Pull the required fallback model in terminal
ollama run mistral
```
*(Note: If Ollama is not installed or offline, the compiler will gracefully fail-over instantly into the robust Symbolic Regex `nlp_explainer` matrix and still 100% function).*

---

## 🚀 How To Run the Application

1. Open a command terminal and navigate to the project directory.
2. Boot the silent server wrapper:
   ```bash
   python gui.py
   ```
3. Look for the web-studio initialization in the console format: `🌟 http://127.0.0.1:5000 🌟`
4. `CTRL+Click` the URL (or manually paste it into Chrome/Edge) to open the IDE Dashboard.
5. Select a test script (e.g. `test_case_large.py`) on the far-left sidebar and click **"Scan & Diagnose Error"**.

> **Note on Browser Caching:** If making layout modifications to `index.html`, Chrome heavily caches localhost files. Always hit `CTRL + F5` to execute a Hard-Refresh to visibly load updated Javascript/CSS routines!

---

## 🌿 The Green IT & Telemetry Logic

The far-right terminal frame monitors code compilation impact via randomized hardware algorithms mapping execution length latency. Rather than requiring local kernel privileges to pull true physical wall voltages, `app.py` computes an enterprise simulation mapping CodeCarbon Emissions, Pinpoint Latency overheads, and Intel RAPL metric estimations dynamically to actively enforce eco-coding practices among developers.
