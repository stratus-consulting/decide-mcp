# DECIDE Terms of Service

Last updated: November 10, 2026

These terms govern your use of DECIDE, the hosted migration discovery risk review service provided by Stratus Consulting Group ("Stratus", "we"). By using DECIDE through MCP or the REST API, you agree to them. If you accept these terms on behalf of an organization, you confirm that you have authority to bind it, and "you" includes that organization.

If you have a separate written agreement with Stratus that covers DECIDE, that agreement takes precedence where it differs from these terms.

## 1. The service

DECIDE reviews discovery findings you submit and returns open risks and recommended next steps. It is a risk review, not an approval:

- It doesn't judge whether a business rule or decision is right or safe.
- It doesn't certify migration readiness or return a pass/fail result.
- It reviews only what you send, only when you call it.

Its output is guidance generated with the help of AI. You remain responsible for your migration decisions and for checking anything DECIDE returns before you act on it.

## 2. Access

- **Without a key:** MCP access is open, with daily limits and a cap on the number of risks returned per call.
- **With a key:** API keys are issued by Stratus. Keep your key confidential. You're responsible for use of the service under your key. Tell us at once if you think it has been exposed.

We set and may change rate limits, daily budgets and request size limits to keep the service available.

## 3. What you may submit

Submit discovery findings and metadata only. Don't submit customer records, credentials, personal information, production datasets or confidential source documents. Summarize sensitive findings instead.

You must have the right to submit what you send. You keep ownership of your submissions. You give Stratus permission to process them to provide the service, as described in [Data Handling](docs/data-handling.md).

## 4. Acceptable use

You agree not to:

- try to extract, reconstruct or reverse-engineer DECIDE's question bank, grading rules, weights, prompts or methodology, including by systematically probing the service
- get around rate limits, budgets or access controls, or share keys to do so
- disrupt the service, test it for load, or attack it
- copy or exploit DECIDE's proprietary elements, such as its output structure, risk wording or methodology, to develop or train a competing assessment service. This doesn't restrict you from independently developing your own products.
- use it for anything unlawful

To report a security issue, follow [SECURITY.md](SECURITY.md).

## 5. Intellectual property

The DECIDE service, its assessment engine, methodology and branding belong to Stratus. These terms don't grant you any rights in them except to use the service as described here.

You may use the output DECIDE returns to you in your own migration work, including sharing it with your clients and project teams.

Materials in this repository are licensed as stated in [LICENSE](LICENSE) and [NOTICE](NOTICE).

## 6. Your data

How submissions are processed, what is kept, and how caching works is described in [Data Handling](docs/data-handling.md). Answers are processed by Anthropic, Stratus's AI model provider, to grade answer quality.

## 7. Changes and availability

We may change, suspend or discontinue DECIDE, in whole or in part, at any time.

We may update these terms. When reasonably practicable, we'll announce material changes in this repository or through another appropriate channel before they take effect. The date at the top shows the latest version, and continuing to use DECIDE after a change takes effect means you accept it.

We may suspend or revoke access, including any API key, if these terms are breached or to protect the service.

## 8. No warranty

DECIDE is provided "as is" and "as available". To the extent the law allows, Stratus disclaims all warranties, express or implied, including fitness for a particular purpose, accuracy and non-infringement. We don't promise that the service will be uninterrupted, error-free, or that it will find every risk.

## 9. Limitation of liability

To the extent the law allows, Stratus is not liable for any indirect, incidental, special, consequential or punitive damages, or for lost profits, data or business, arising from your use of DECIDE. Stratus's total liability for any claim relating to DECIDE is limited to the amount you paid Stratus for DECIDE in the 12 months before the claim, or US $100 if you paid nothing.

## 10. Governing law

These Terms are governed by and construed in accordance with the laws of the State of Texas, United States, without regard to its conflict-of-law principles.

## 11. Contact

Questions about these terms: [engage@stratusgroups.com](mailto:engage@stratusgroups.com)
