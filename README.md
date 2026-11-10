<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/icon-dark.png">
    <img src="assets/icon-light.png" alt="Stratus Consulting Group" width="96">
  </picture>
</p>

<h1 align="center">DECIDE</h1>

<p align="center">
  <strong>Migration Discovery Risk Review</strong><br>
  By Stratus Consulting Group
</p>

<p align="center"><em>Reduce uncertainty in migration Discovery, one round at a time.</em></p>

<p align="center">
  MCP Server · Hosted API · Proprietary Service
</p>

<p align="center">
  <a href="docs/api-usage.md">API Usage</a> ·
  <a href="docs/data-handling.md">Data Handling</a> ·
  <a href="SECURITY.md">Security</a> ·
  <a href="https://www.stratusgroups.com">stratusgroups.com</a>
</p>

---

DECIDE is an AI-powered migration discovery risk review service developed by Stratus Consulting Group.

Designed for AI agents and migration professionals, DECIDE reviews migration discovery findings to identify unanswered questions, incomplete or insufficiently supported answers, and potential risks that require further investigation.

Rather than simply identifying gaps, DECIDE provides actionable next steps, including what needs clarification and which stakeholders should be consulted.

**Discovery is iterative. DECIDE is built to work the same way.**

Submit findings after each discovery round to understand:

- Which risks remain open
- Which risks have been resolved
- Which new risks have emerged
- What questions should be addressed next
- Who should provide the missing information

DECIDE does not approve migration decisions, certify readiness, or produce a pass/fail score. It helps teams build a clearer, better-supported understanding of their migration before moving forward.

### Built for real-world migration discovery

Migration discovery rarely happens in a single workshop. Information emerges through stakeholder conversations, source-system analysis, documentation reviews, profiling, and technical investigation.

DECIDE supports that process by reviewing the evidence available at each stage and highlighting what still requires attention.

The service is accessible through MCP for AI agents and through a REST API for programmatic integrations.

## Connect

**MCP (no key needed)**

```json
{
  "mcpServers": {
    "decide": {
      "type": "http",
      "url": "https://stratus-decide.onrender.com/mcp"
    }
  }
}
```

Tool: `validate_migration_discovery`. Listed in the official MCP registry as `io.github.stratus-consulting/stratus-decide`.

Without a key, each call returns up to 10 of the highest-severity risks (the summary still counts all of them), each network address gets a daily grading budget, and learning is off.

**REST (API key issued by Stratus)**

```bash
curl -X POST https://stratus-decide.onrender.com/v1/discovery/validate \
  -H "X-API-Key: $DECIDE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @examples/request.json
```

With a key, calls return up to 25 risks by default (set `max_risks` to change it). The full schema (OpenAPI) is at https://stratus-decide.onrender.com/docs.

## In this repository

| Path | What it is |
|---|---|
| [docs/api-usage.md](docs/api-usage.md) | What to send, how to read the result, limits and errors |
| [docs/data-handling.md](docs/data-handling.md) | What happens to submitted discovery data |
| [examples/](examples/) | A synthetic request, its response, and a small client |
| [SECURITY.md](SECURITY.md) | How to report a security issue |
| [TERMS.md](TERMS.md) | Terms of Service for the hosted DECIDE service |

All examples are synthetic. None contain client data.

---

**Stratus DECIDE** is a proprietary migration discovery risk review service developed by **Stratus Consulting Group**.

[Website](https://www.stratusgroups.com) · [Terms](TERMS.md) · [Data Handling](docs/data-handling.md) · [Security](SECURITY.md)

© 2026 Stratus Consulting Group. All rights reserved in the proprietary DECIDE service and methodology.

Public integration materials are subject to the [LICENSE](LICENSE) and [NOTICE](NOTICE) in this repository.
