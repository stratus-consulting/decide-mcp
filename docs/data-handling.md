# Data Handling and Privacy

Stratus DECIDE is designed to review migration discovery findings without requiring access to underlying customer records or source-system datasets.

### What information should be submitted?

DECIDE accepts structured discovery findings, including:

- Migration scope and objectives
- Discovery questions and answers
- Source and target system context
- Data objects, relationships, and dependencies
- Known assumptions, constraints, and unresolved questions
- Stakeholder roles associated with discovery findings

**Do not submit customer records, credentials, personal information, production datasets, or confidential source documents.** Summarize sensitive findings using the minimum information necessary for review.

### How submissions are processed

DECIDE evaluates submitted findings to identify potential migration risks, incomplete discovery, and areas requiring further clarification.

Answer-quality assessments are processed using an external AI model provider, Anthropic.

### Data retention

DECIDE uses engagement identifiers, risk identifiers, and usage metadata to support change tracking and service operation.

The service is designed not to persist submitted answer text as part of its discovery history.

Depending on the API key configuration, derived assessment results may be cached to support reuse of previous evaluations.

### Learning and caching controls

Anonymous MCP access operates with learning disabled.

For authenticated consumers, learning and caching behavior is controlled by the configuration associated with their API key.

When enabled, derived grading results may be retained to avoid repeating evaluations of unchanged answers.

When disabled, derived grading results are not retained for reuse.

### Change tracking

DECIDE associates discovery reviews with an engagement identifier so consumers can compare risks across submissions.

Change history is scoped to the relevant API key or anonymous caller identity.

### Caching is not model training

"Learning" in DECIDE means caching derived grading results so unchanged answers don't have to be graded again. Stratus does not use your submissions to train AI models.

Answers sent for grading are processed by Anthropic as Stratus's AI model provider.

### Hosting and third-party processing

DECIDE is hosted on Render and uses Anthropic for answer-quality assessment.

Hosting region, provider retention policies, and any applicable third-party data-processing terms should be confirmed before publication.

### Questions

Contact [engage@stratusgroups.com](mailto:engage@stratusgroups.com).
