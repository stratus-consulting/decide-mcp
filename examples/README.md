# Examples

All data here is synthetic.

| File | What it is |
|---|---|
| `request.json` | An early, partial discovery submission for a CRM consolidation into Salesforce. Three objects are in scope, but only Account has been investigated so far, and a Partner object has turned up outside scope. Some questions are still open |
| `response.json` | What the live service returned for it (17 risks: 3 high, 8 medium, 6 low) |
| `validate.py` | A small client that submits a file over REST and prints the risks |

## Run it

Needs Python 3.9 or later and an API key from Stratus. No packages to install.

```bash
export DECIDE_API_KEY=your-key
python validate.py request.json
```

To try DECIDE without a key, add the MCP server to your agent instead (see the main [README](../README.md#connect)).
