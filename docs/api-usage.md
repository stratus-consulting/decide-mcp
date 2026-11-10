# API usage

## Endpoints

| Interface | Address | Auth |
|---|---|---|
| MCP | `https://stratus-decide.onrender.com/mcp`, tool `validate_migration_discovery` | Optional `X-API-Key` |
| REST | `POST https://stratus-decide.onrender.com/v1/discovery/validate` | `X-API-Key` required |

Full schema: https://stratus-decide.onrender.com/docs

## How to use it

Discovery is iterative. Submit your full, current findings after each iteration, using the same `engagement_id` every time. An iteration can be a workshop, a stakeholder clarification, a profiling report or a confirmed decision.

Each submission must contain everything found so far, not just what's new. Anything left out is treated as gone.

## What to send

1. **`sow` (optional):** use case, objects in scope, assumptions, out-of-scope items, definition of success.
2. **`project_items`:** each project-level question, its answer (`null` if still open) and who gave it.
3. **`objects`:** for each object or table: name, criticality, whether it has a hierarchy, its questions and answers, and any flags.
4. **`discovered_outside_scope` (optional):** objects found that aren't in scope, who asked for them, and whether they're needed on Day 1.

Tag every question with a topic:

| Project topics | Object topics |
|---|---|
| `purpose`, `scope`, `use_case`, `success`, `people`, `data_landscape`, `procurement`, `process` | `object_context`, `object_source`, `dependencies`, `hierarchy`, `migration_logic` |

Rules that affect your result:

- Send open questions with `answer: null`. Hiding them doesn't help.
- Identify sources by role, not by name. Answers with no source are reported as a risk.
- Record what you learned, not what you think should be done.

## Reading the result

| Field | Meaning |
|---|---|
| `summary` | Count of high, medium and low risks |
| `risks` | Highest severity first. Each has a stable `id`, a `message`, a `next_step` and `must_confirm` |
| `changes` | Which risks are `new`, `closed` or `not_resubmitted` since your last submission |
| `coverage_project`, `coverage_objects` | Per topic: `covered`, `partial`, `missing` or `not_applicable` |
| `risks_omitted` | How many risks were left out of the list |

How many risks are listed: up to 25 by default with an API key (`max_risks` changes it, up to 500). Anonymous MCP calls are capped at 10. The `summary` always counts every risk.

`not_resubmitted` means the question or flag was left out, not that the risk was resolved.

## Errors

| Status | Meaning | What to do |
|---|---|---|
| `401` | Missing, invalid or revoked key | Check `X-API-Key` |
| `413` | Request too large | Split the submission, e.g. by object |
| `422` | Doesn't match the schema | Fix the field named in the response |
| `429` | Rate limit or daily budget reached | Wait for `Retry-After` |
| `503` | Grading temporarily unavailable | Retry after `Retry-After`. No partial result is returned |

Resubmitting unchanged answers doesn't use up your daily budget when caching is on.
