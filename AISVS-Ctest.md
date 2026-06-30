***Note: Due to the strict length constraint of under 100 lines for five complete skill sheets, the explanations are maximally concise while adhering to all structural and substance requirements.*

# OWASP AISVS Control Skill Sheet: C1.1.1 Training Data Feature Relevance
## METADATA

- **Control ID:** C1.1.1
- **Standard + version:** OWASP AISVS v1.0 — Training Data Features Limitation
- **Control Level:** P1
- **Scope:** llm_ai, data pipelines, feature engineering environments. *Scope covers the entire process of defining, extracting, and sanitizing features from raw training data to ensure only attributes directly required for the model's stated operational purpose are utilized.*
- **Author:** jesse de koning
- **Date:** 10-06-2026
- **Lab Evidence Boundary:** Lab testing can verify schema validation rules and feature filtering mechanisms. Cannot prove that a dataset was never intentionally poisoned or augmented with non-required features outside the pipeline boundaries.
- **Prerequisite Controls:** Data governance, data dictionary management, model specification review.

---

## REQUIREMENT SUMMARY

- **Brief Clause Summary:** Ensure training datasets are restricted to only the features and attributes necessary for the specific model purpose (data minimalization).
- **Source Link:** OWASP AISVS v1.0 — C1.1.1

---

## PENTEST APPLICABILITY

- **In-scope:** Data schema validation tools, feature extraction pipelines, data dictionary definitions used during training setup.
- **Out-of-scope:** The final model output or inference API (unless it implicitly leaks non-required data).
- **Lab Over-claim Note:** Simply having a policy confirming minimum features does not prove that the execution pipeline strictly enforces this restriction at runtime.

---

## THREAT / ABUSE SCENARIOS

- **Threats:** Including irrelevant PII, proprietary fields, or highly sensitive auxiliary features (e.g., facial recognition data when only age is needed).
- **Abuse / Operational Risks:** Model training on excess data leading to function creep, increased attack surface, and non-compliance (GDPR/CCPA overreach).

---

## PRECONDITIONS

- **Accounts & Roles:** Data Scientist, ML Engineer, Data Governance Officer.
- **Data & Environment:** Defined model specification, source data schemas, access to feature store logs.
- **Repeatability Anchors:** Versioned list of necessary features for a given model version.
- **Stop Conditions:** Discovery of non-required sensitive fields being passed into the training pipeline.

---

## MANUAL TEST PROCEDURE

- *Manual steps:* Review dataset schema and preprocessing scripts against the documented minimum feature set (model specification) to identify any extraneous or redundant attributes.

---

## TOOLING & ASSISTED TESTING

- **Common tools:** Schema validators, ML metadata stores, data profiling tools.
- **Can be automated:** Enforcement of schema validation rules during ETL/feature engineering steps.
- **Human validation needed:** Verification that the *concept* of "required" is correct (i.e., no critical missing feature was omitted).

---

## EVIDENCE SPECIFICATION

- **Artefacts:** Model specification document, required features list, data pipeline validation logs.
- **Redaction & Handling:** Redact non-essential sensitive fields from all artifacts.
- **Sensitivity:** High—Must be treated as system blueprint data.

---

## TRIAGE & VERDICT RULES

- **Pass:** Feature selection logic is implemented and validated against the model's stated function.
- **Fail:** Non-minimal or unnecessary features are confirmed being processed into the training set.
- **Partial:** The policy exists, but validation implementation (code) is incomplete or bypassable.
- **Inconclusive:** Model purpose document is unavailable or ambiguous.

---

## FALSE POSITIVES & NOISE

- **Common noise:** Temporary feature engineering outputs that are immediately discarded and not ingested by the model.
- **Action:** Confirm which fields successfully reach the final training dataset artifact.

---

## CROSS-REFERENCES

- **Related Controls & Standards:** General data minimization principles; GDPR/CCPA compliance guidelines.
- **Dependencies:** Data dictionary, Model governance policy enforcement.

***

# OWASP AISVS Control Skill Sheet: C1.1.2 Training Data Inventory & Traceability
## METADATA

- **Control ID:** C1.1.2
- **Standard + version:** OWASP AISVS v1.0 — Dataset Governance and Lineage
- **Control Level:** P0
- **Scope:** llm_ai, data pipelines, training environments. *Detailed coverage across the entire data lifecycle (source -> ingestion -> preprocessing -> model use), ensuring every dataset has clear origin, rights, and usage constraints documented.*
- **Author:** jesse de koning
- **Date:** 10-06-2026
- **Lab Evidence Boundary:** Lab testing can verify the existence of an inventory system/database and audit logs. Cannot confirm completeness for internal legacy datasets or external sources without organizational process review.
- **Prerequisite Controls:** Dataset governance, audit logging, provenance tracking.

---

## REQUIREMENT SUMMARY

- **Brief Clause Summary:** Maintain a comprehensive, up-to-date inventory of all training data sources, documenting origin, license, owner, intended use, and processing history (attributability).
- **Source Link:** OWASP AISVS v1.0 — C1.1.2

---

## PENTEST APPLICABILITY

- **In-scope:** Centralized Data Catalog/Data Mesh implementation, Lineage tracking tools, Dataset ingestion pipelines logs.
- **Out-of-scope:** The original source data owner's internal records (this is an organizational control).
- **Lab Over-claim Note:** A single database view or tool screen showing "Inventory Exists" does not prove that the underlying documentation for *every* included dataset is complete and accurate.

---

## THREAT / ABUSE SCENARIOS

- **Threats:** Using data without proper licensing, introducing undocumented datasets (shadow IT), or failing to retire data when its purpose changes.
- **Abuse / Operational Risks:** Legal non-compliance due to expired licenses; inability to explain the model's behavior (Lack of Explainability/Audit Trail).

---

## PRECONDITIONS

- **Accounts & Roles:** Data Governance Officer, Compliance Analyst, ML Ops Manager.
- **Data & Environment:** Access to the centralized dataset catalog and metadata repository.
- **Repeatability Anchors:** Specific data identifiers (`dataset_ID`) and associated documented license types/expiry dates.
- **Stop Conditions:** Failure of the inventory system to automatically flag expired licenses or unreviewed datasets.

---

## MANUAL TEST PROCEDURE

- *Can be automated:* Checking for metadata presence (e.g., checking if all records have a defined `license` field).
- *Manual steps:* Select random sample sets and manually verify that the documented owner, license terms, and intended use listed in the inventory accurately match their real-world usage context.

---

## TOOLING & ASSISTED TESTING

- **Common tools:** Data Catalogs (e.g., Atlan), MLOps platforms with lineage tracking, Graph databases for provenance.
- **Can be automated:** Checking for metadata consistency and identifying gaps in the inventory's technical fields.
- **Human validation needed:** Confirmation of legal compliance regarding licenses and use restrictions (requires domain expert/legal review).

---

## EVIDENCE SPECIFICATION

- **Artefacts:** Full dataset manifest/inventory reports, lineage graph screenshots showing source linkages.
- **Redaction & Handling:** Keep all provenance records secure; metadata is sensitive but not necessarily private data itself.
- **Sensitivity:** Moderate—Operational control artifact.

---

## TRIAGE & VERDICT RULES

- **Pass:** Inventory is comprehensive, up-to-date, and every entry has defined governance (owner/license/use).
- **Fail:** Known datasets used in training are missing from the inventory or have invalid provenance records.
- **Partial:** The system exists but fails to update the ownership or license details upon change of use.

---

## FALSE POSITIVES & NOISE

- **Common noise:** Draft, experimental, or decommissioned data sources that are included without proper status flagging in the inventory.
- **Action:** Confirm if stale/draft datasets have been formally marked as retired and excluded from active training consideration.

---

## CROSS-REFERENCES

- **Related Controls & Standards:** ISO 27001 (Asset Management), GDPR Data Mapping, Legal Compliance Policies.
- **Dependencies:** Identity management systems for ownership attribution; robust logging services.

***

# OWASP AISVS Control Skill Sheet: C1.1.3 Training Data Integrity/Transfer Assurance
## METADATA

- **Control ID:** C1.1.3
- **Standard + version:** OWASP AISVS v1.0 — Data Confidentiality and Integrity in Transit/Rest
- **Control Level:** P2
- **Scope:** llm_ai, data pipelines, storage endpoints. *Covers cryptographic protection mechanisms (encryption) applied to training datasets when they are stored at rest or transferred between stages of the ML pipeline.*
- **Author:** jesse de koning
- **Date:** 10-06-2026
- **Lab Evidence Boundary:** Lab testing can verify that encryption is enabled and key management procedures (e.g., KMS usage) are followed for data at rest/transit. Cannot confirm the security of external systems not under scope.
- **Prerequisite Controls:** Cryptographic key management, network segmentation, secure data transfer protocols.

---

## REQUIREMENT SUMMARY

- **Brief Clause Summary:** Data must be protected against unauthorized modification or interception while stored and when moved between processing components (encryption/integrity checks).
- **Source Link:** OWASP AISVS v1.0 — C1.1.3

---

## PENTEST APPLICABILITY

- **In-scope:** Data storage buckets (S3, Azure Blob), ETL transfer mechanisms (Kafka, pipes), intermediate feature store caches.
- **Out-of-scope:** The internal network infrastructure components themselves; the encryption algorithm choice (if standard industry practices are followed).
- **Lab Over-claim Note:** Simply confirming HTTPS/TLS usage does not guarantee the integrity or confidentiality of data once it lands in an unsecured memory buffer during processing.

---

## THREAT / ABUSE SCENARIOS

- **Threats:** Man-in-the-Middle (MiTM) attacks intercepting transferred datasets; accessing unencrypted staging storage buckets.
- **Abuse / Operational Risks:** Leakage of raw PII/PHI data if encryption keys are compromised or mismanaged.

---

## PRECONDITIONS

- **Accounts & Roles:** DevOps Engineer, Security Architect, ML Ops Manager.
- **Data & Environment:** Dataset transfer logs, Storage bucket configuration (encryption settings), Key Management System access.
- **Repeatability Anchors:** Standardized encryption protocols (AES-256, TLS 1.2+), documented key rotation schedules.
- **Stop Conditions:** Data is found in an unencrypted state outside of designated ephemeral memory containers or secure pipelines.

---

## MANUAL TEST PROCEDURE

- *Can be automated:* Scanning data storage configuration (e.g., checking S3 buckets for encryption settings).
- *Manual steps:* Trace a dataset from raw source to final model input, confirming that encryption controls are explicitly enforced at the point of transfer and rest in each intermediate step.

---

## TOOLING & ASSISTED TESTING

- **Common tools:** Cloud Security Posture Management (CSPM) tools, Network sniffers, Key Management System interfaces.
- **Can be automated:** Verifying TLS handshake requirements for all internal APIs; auditing storage bucket policies.
- **Human validation needed:** Verification of the secure *usage* of keys (i.e., ensuring cryptographic separation between key materials and data).

---

## EVIDENCE SPECIFICATION

- **Artefacts:** Storage configuration audit reports, network flow logs showing encryption usage, key management policies.
- **Redaction & Handling:** Redact specific keys/IDs; secure the entire set as highly sensitive security evidence.
- **Sensitivity:** Critical—Governing core data protection mechanisms.

---

## TRIAGE & VERDICT RULES

- **Pass:** All transfers and resting points are encrypted using industry-standard, audited methods.
- **Fail:** Any segment of the pipeline uses plain text storage or transmission without appropriate security controls.
- **Partial:** Encryption is used for storage but not enforced during transfer/use (or vice versa).

---

## FALSE