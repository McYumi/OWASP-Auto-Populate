import re

def extract_text_between_numbers(text):
    # Pattern to match the numbered patterns (e.g., 1.1.1, 1.10.10)
    pattern = r'\d+(?:\.\d+)+'
    
    # Find all matches of the numbered patterns
    matches = list(re.finditer(pattern, text))
    
    # Extract the text between the matches
    results = []
    for i in range(len(matches) - 1):
        start = matches[i].end()
        end = matches[i + 1].start()
        # Get the text between the current match and the next
        between_text = text[start:end].strip()
        if between_text:
            results.append(between_text)
    return results

# Example usage
text = """
1.1.1
 Verify that an up-to-date inventory of every training-data source (origin
 responsible party
 license
 collection method
 intended use constraints
 and processing history) is maintained.
 1
 1.1.2
 Verify that training data processes include only features
 attributes
 and fields required for the model's stated purpose
 excluding all others (e.g.
 unused metadata
 sensitive PII
 leaked test data).
 1
 1.1.3
 Verify that all dataset changes are subject to a logged approval workflow.
 1
 1.1.4
 Verify that datasets or subsets are watermarked or fingerprinted to enable downstream attribution and detection of unauthorized use.
 3
 1.2.1
 Verify that when training data is retired or removed
 the impact on models trained on that data is assessed
 and that residual memorization risks are addressed (e.g.
 via targeted fine-tuning
 machine unlearning
 or model retraining).
 1
 1.2.2
 Verify that cryptographic hashes or digital signatures are used to ensure data integrity during training data storage and transfer.
 2
 1.2.3
 Verify that automated integrity monitoring is applied to guard against unauthorized modifications or corruption of training data.
 2
 1.2.4
 Verify that all training dataset versions are uniquely identified
 stored immutably
 and auditable to support rollback and forensic analysis.
 3
 1.3.1
 Verify that labeling interfaces and platforms enforce access controls that restrict who can create
 modify
 or approve annotations.
 1
 1.3.2
 Verify that all labeling activities are recorded in audit logs
 including the annotator identity
 timestamp
 and action performed.
 1
 1.3.3
 Verify that annotator identity metadata is exported and retained alongside the dataset so that every annotation or preference pair can be attributed to a specific
 verified human annotator throughout the training pipeline.
 2
 1.3.4
 Verify that cryptographic hashes or digital signatures are applied to labeling artifacts
 annotation data
 and fine-tuning feedback records (including RLHF preference pairs) to ensure their integrity and authenticity.
 2
 1.3.5
 Verify that sensitive information in labels is redacted
 anonymized
 or encrypted both at rest and in transit before being used in any labeling artifact.
 2
 1.4.1
 Verify that automated tests catch format errors and nulls on every ingest or significant data transformation.
 1
 1.4.2
 Verify that training and fine-tuning pipelines implement data integrity validation and poisoning detection techniques (e.g.
 statistical analysis
 outlier detection
 embedding analysis) to identify potential data poisoning or unintentional corruption in training data.
 2
 1.4.3
 Verify that automatically generated labels (e.g.
 via models or weak supervision) are subject to confidence thresholds and consistency checks to detect misleading or low-confidence labels.
 2
 1.4.4
 Verify that automated tests catch label skews on every ingest or significant data transformation.
 2
 1.4.5
 Verify that models used in security-relevant decisions (e.g.
 abuse detection
 fraud scoring
 automated trust decisions) are evaluated for systematic bias patterns that an adversary could exploit to evade controls (e.g.
 mimicking a trusted language style or demographic pattern to bypass detection).
 2
 1.4.6
 Verify that appropriate training-time defenses against data poisoning
 such as adversarial training
 data augmentation with perturbed inputs
 or robust optimization techniques
 are implemented and tuned for relevant models based on risk assessment.
 2
 1.4.7
 Verify that defenses against clean-label poisoning attacks (e.g.
 input purification
 k-NN filtering
 data partitioning and aggregation) are implemented for models exposed to untrusted or partially trusted training data sources.
 3
 1.5.1
 Verify that the lineage of each dataset and its components
 including all transformations
 augmentations
 and merges
 is recorded and can be reconstructed.
 1
 1.5.2
 Verify that lineage records are immutable
 securely stored
 and accessible for audits.
 2
 1.5.3
 Verify that lineage tracking covers synthetic data generated via augmentation
 synthesis
 or privacy-preserving techniques.
 2
 1.5.4
 Verify that synthetic data is clearly labeled and distinguishable from real data throughout the pipeline.
 2
"""
extracted_texts = extract_text_between_numbers(text)
print(extracted_texts[0])
