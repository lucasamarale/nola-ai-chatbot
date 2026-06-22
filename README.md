# nola AI — Intelligent Customer Support Chatbot

> AI-powered support chatbot built for [Nola](https://usenola.com.br) — a restaurant management SaaS platform. Developed as part of a 48-hour internship challenge for the Customer Success team.

---

## Overview

Customer Success teams spend a significant amount of time answering repetitive questions — product setup, hardware troubleshooting, delivery integrations. **nola AI** automates these interactions, delivering instant, accurate responses 24/7 and freeing the CS team to focus on cases that truly require human attention.

---

## Demo

![nola AI chatbot interface](https://usenola.com.br/2026/assets/images/nola-logo-preto.svg)

The chatbot handles questions like:
- *"How do I add a new product to the menu?"*
- *"My printer stopped working. What should I do?"*
- *"Does Nola integrate with iFood?"*

---

## Architecture

```
Browser (HTML/JS)
      │
      ▼
Python CORS Proxy (port 3001)
      │
      ▼
N8N Webhook (cloud)
      │
      ├── Knowledge Base (Google Sheets / CSV)
      │
      ▼
Groq API (LLaMA model)
      │
      ▼
Response → User
```

**Key design decisions:**
- **No frontend framework** — plain HTML, CSS and JavaScript for zero dependencies and fast load
- **Python proxy** — resolves CORS restrictions when calling N8N from the browser
- **Session ID per conversation** — each chat session gets a unique ID to maintain context
- **Editable knowledge base** — CSV/Google Sheets format so the CS team can update it without touching code

---

## Tech Stack

| Layer | Tool |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Orchestration | [N8N](https://n8n.io) |
| LLM Inference | [Groq API](https://groq.com) (LLaMA) |
| Knowledge Base | Google Sheets / CSV |
| CORS Proxy | Python (http.server + subprocess) |

---

## Project Structure

```
├── nola_chatbot_frontend.html   # Chat interface (standalone, no build step)
├── proxy.py                     # CORS proxy — forwards requests to N8N
├── workflow_nola_chatbot.json   # N8N workflow (importable)
├── base_conhecimento_nola.csv   # Knowledge base (40+ Q&A entries)
├── abrir_chatbot.command        # macOS launcher script
└── GUIA_CONFIGURACAO_N8N.md    # Step-by-step setup guide (Portuguese)
```

---

## Getting Started

### Prerequisites

- Python 3.x
- N8N account (cloud or self-hosted)
- Groq API key — [get one free at console.groq.com](https://console.groq.com)

### 1. Import the N8N workflow

1. Open your N8N instance
2. Go to **Workflows → Import**
3. Upload `workflow_nola_chatbot.json`
4. Add your Groq API key as a credential
5. Activate the workflow and copy the webhook URL

### 2. Configure the proxy

Open `proxy.py` and update the N8N webhook URL:

```python
N8N_URL = "https://your-instance.app.n8n.cloud/webhook/your-webhook-id/chat"
```

### 3. Run

```bash
python3 proxy.py &
open nola_chatbot_frontend.html
```

Or on macOS, simply double-click `abrir_chatbot.command`.

---

## Knowledge Base

The knowledge base (`base_conhecimento_nola.csv`) contains 40+ entries organized by category:

| Category | Examples |
|---|---|
| Features | Menu management, order flow, kitchen display |
| Technical Support | Printer issues, tablet sync, QR Code |
| Delivery | iFood, Rappi, delivery area config |
| Financial | Plans, billing, payment methods |
| Hardware | Printers, card readers, tablets |
| Security | LGPD compliance, data backup |

To extend the bot's knowledge, simply add rows to the CSV and re-import to Google Sheets.

---

## AI Tools Used

- **[Claude](https://claude.ai) (Anthropic)** — used as a technical reasoning partner throughout development: architecture decisions, debugging CORS issues, prompt engineering, and pixel-perfect logo crop math
- **Groq + LLaMA** — LLM inference engine powering the chatbot responses, chosen for its low latency
- **N8N** — workflow orchestration with native AI capabilities

---

## About

Built in under 48 hours as a practical challenge for a Customer Success internship position at [Nola](https://usenola.com.br) — a Brazilian SaaS platform for restaurant management.

**Author:** Lucas Amaral — [lucasamaralevangelista@gmail.com](mailto:lucasamaralevangelista@gmail.com)
