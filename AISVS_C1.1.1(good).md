i gave two example skill sheets please base it on both of those plus the other rules i gave the date should be 10/06/2026 for all controls also keep the auther the same 



# OWASP AISVS Control Skill Sheet

## METADATA

- **Control ID(s):** C1.1.1
- **Standard + version:** OWASP AISVS v1.0 — C1.1.1 Training Data Origin & Traceability
- **Control Level:** P0
- **Scope:** llm_ai, data pipelines, training environments  
- **Author:** Jesse De Koning
- **Date:** 10/06/2026 
- **Lab Evidence Boundary:**  
  *Lab testing can verify dataset inventory, provenance records, and lineage graph integrity. Cannot confirm completeness of all historical or external datasets without organizational audit access.*  
- **Prerequisite Controls:** Dataset governance, audit logging, provenance tracking, supply-chain assurance.

---

## REQUIREMENT SUMMARY

- **Brief Clause Summary:**  
  *Verify that Apex Financial Group maintains an up-to-date inventory of all training datasets, including origin, responsible party, license, collection method, intended-use constraints, and processing history.*  
  *Ensure datasets are attributable, governed, and auditable throughout their lifecycle.*  
- **Source Link:** OWASP AISVS v1.0 — C1.1.1

---

## PENTEST APPLICABILITY

- **In-scope:**  
  - Training pipelines and workflows at Apex, dataset repositories, lineage management tools, data ingestion systems.  
- **Out-of-scope:**  
  - Inference-only systems without access to training data or provenance records.  
- **Lab Over-claim Note:**  
  *Presence of inventory records does not confirm all datasets are documented nor that provenance is complete, especially for external or legacy datasets.*

---

## THREAT / ABUSE SCENARIOS

- **Threats:**  
  - Poisoned datasets inserted into training pipelines, risking model integrity.  
  - Unauthorized or unlicensed data used for training, risking legal or compliance violations.  
  - Tampering with lineage or provenance records to conceal malicious data or modifications.  
  - Supply-chain attack compromising external datasets or ingestion pipelines.  
- **Abuse / Operational Risks:**  
  - Malicious actors tampering with provenance records to hide data poisoning.  
  - Data provenance falsification leading to non-compliance or audit failures.  
  - Insertion of unverified datasets into the training process, risking model bias or regulatory issues.

---

## PRECONDITIONS

- **Accounts & Roles:**  
  - Read access to dataset inventories, lineage systems, and governance logs.  
- **Data & Environment:**  
  - Access to dataset repositories, lineage graphs, ingestion logs, and ownership metadata.  
- **Repeatability Anchors:**  
  - Stable dataset identifiers, audit logs, and version-controlled lineage records.  
- **Stop Conditions:**  
  - Detection of sensitive data exposure, environment contamination, or incomplete provenance records.  

---

## MANUAL TEST PROCEDURE

- *Can be automated:*  
  - Detection of missing metadata, stale lineage records, or duplicate dataset identifiers.  
- *Manual steps:*  
  - Review dataset provenance records for completeness and correctness.  
  - Verify that lineage can be reconstructed from ingestion to deployment.  
  - Confirm licensing, ownership, and processing history aligns with governance policies.  
- **Note:** Focused on verifying the integrity and completeness of dataset provenance, not just presence of records.

---

## TOOLING & ASSISTED TESTING

- **Common tools:**  
  - MLOps governance platforms, lineage tracking tools, audit logs, SIEM systems.  
- **Can be automated:**  
  - Detection of missing or inconsistent provenance metadata, stale records, unlinked datasets.  
- **Human validation needed:**  
  - Legitimacy of data sources, licensing claims, and provenance authenticity.  
- **Notes:**  
  - Confirm anomalies with manual review before marking as fail.

---

## EVIDENCE SPECIFICATION

- **Artefacts:**  
  - Dataset inventories, lineage graphs, ingestion logs, ownership and licensing records.  
- **Redaction & Handling:**  
  - Remove sensitive information; secure provenance artifacts as security evidence.  
- **Storage & Retention:**  
  - Follow organizational audit policies, retain evidence for required periods.  
- **Sensitivity:**  
  - Classify artifacts as confidential, secure per internal policies.

---

## TRIAGE & VERDICT RULES

- **Pass:**  
  - Inventory complete, current, with verifiable provenance, linkage from source to model.  
- **Fail:**  
  - Missing datasets, unverifiable lineage, or untraceable provenance.  
- **Partial:**  
  - Inventory exists but lineage or ownership details are incomplete or inconsistent.  
- **Inconclusive:**  
  - Insufficient evidence or access restrictions prevent assessment.  
- **N/A:**  
  - Control not applicable; no training data lifecycle present.

---

## FALSE POSITIVES & NOISE

- **Common noise:**  
  - Outdated lineage artifacts misclassified as unmanaged datasets.  
  - Temporary caches or preprocessing artifacts mistaken for unmanaged data.  
  - External attestations or metadata that are outdated or incomplete.  
- **Action:**  
  - Confirm via manual review, cross-reference logs, before downgrading or marking false positive.

---

## CROSS-REFERENCES

- **Related Controls & Standards:**  
  - OWASP LLM Top 10: Data Poisoning, Supply Chain Risks.  
  - MITRE ATLAS: Data Poisoning, Artifact Manipulation.  
  - NIST AI RMF: Data Governance and Provenance.  
- **Dependencies:**  
  - Dataset inventory, lineage tracking, supply-chain security, audit logs, governance controls.

---
