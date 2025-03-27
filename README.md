# MLOps: Definition, Objectives, and Levels

## Definition and Objectives of MLOps
- **MLOps**: DevOps adapted for Machine Learning (ML).
- **Objective**: Engineering tools and practices around ML to bridge the gap between prototype and production (PoC to production gap).
- **Note**: Code ML is a small part of ML Systems.

## Two Main Families of Problems
1. **Technical Problems**
2. **Regulatory and Ethical Problems**

---

# Levels of MLOps

| Level | Description |
|-------|-------------|
| 0     | Manual Process (Training one model, not the main job, handling two or three models) |
| 1     | Automated Processing Chains |
| 2     | CI/CD for ML |

### Transition from Level 0 to Level 1
- Not focused on Level 2.
- Staging: A testing space mimicking production to catch issues before going live.

---

# State of the MLOps Field

- Rapid evolution with many competing libraries.
- Less stable and less homogeneous adoption than the DevOps field.
- Evolving alongside legislation and regulation.
- Given the instability of the field, broad principles are more important than specific techniques.

---

# Lifecycle of an ML Project

1. **Definition of Project Scope**
2. **Data Management**
3. **Modeling**
4. **Deployment**

### Focus Areas
We will study steps **2**, **3**, and **4**.

---

# Data Management

### Key Aspects
- Unbiased method of data collection.
- Clear definition of inputs and outputs.
- Robust data processing pipeline without training/production disparity.
- Reproducibility and experiments.

---

# Modeling

### Key Aspects
- Training considering production needs (model size, speed, etc.).
- Error analysis, often by significance.

---

# Deployment

### Key Aspects
- Scaling.
- Detection of data and concept drifts.
- Monitoring.
- Retraining process.
- Latency.

---

# Introduction to MLOps (Ethics)

### Ethical Considerations
- Transitioning from prototype to production raises ethical questions:
  - Is our system fair?
  - Does it respect privacy?
  - Does it comply with regulations?

### Addressing Ethical Questions
- These questions should be addressed throughout the lifecycle of an ML project.

---

# Fair Systems – Combating Biases

### Examples of Biases Leading to Unfair Treatment
- **Sampling Bias**.
- **Differentiated Treatment**: Based on perceived race, gender, etc.
- **Systemic Bias**: Often leads to differentiated treatment.
- **Tyranny of the Majority**.

---

# Fair Models

### Competing Definitions
1. **Group Calibration**: Same performance level for each group defined by protected or morally important attributes (e.g., perceived race, gender, economic level).
2. **Individual Calibration**: Same performance for individuals.

#### Example: 
- Recidivism prediction (COMPAS system in the United States).

---

# Regulations

### Key Aspects
- **Right to Erasure**.
- **Collection of Consent**.
- **Strong Protection of Personal Data**.
- **Privacy by Design**: Considering privacy aspects from the earliest stages of design.

---

# Levels of Personal Data Protection

| Method          | Description                                         |
|-----------------|-----------------------------------------------------|
| **Pseudonymized** | All personal data is replaced by a pseudonym.       |
| **Anonymized**    | No personal data remains identifiable.              |

---

# Data Management: Research vs Industry

| Aspect              | Research System                     | Industry System                            |
|---------------------|-------------------------------------|-----------------------------------------|
| Definition          | Data + Work (Parameters + Model)    | Work (Data + Parameters) + Model         |
| Focus               | Defining the output                 | Processing pipeline, scalability, deployment, integration. |

---

# Dataset Size

| Size   | Focus                                    |
|--------|-----------------------------------------|
| Small  | Quality of annotations is crucial.      |
| Large  | Quality of data processing process is crucial. |

---

# Processing Pipeline

### Requirements
- Adaptation to batch development and real-time production.
- Faithfulness of development/production processing.
- Scalability.
- Deployment on various targets.
- Ease of development.
- Integration within the ecosystem.

### Popular Tools
- **Kubeflow (GCP)**
- **DVC (Data Version Control)**
- **TFX (TensorFlow Extended)**
- **MLFlow**
- **Pachyderm**

---

# DVC (Data Version Control)

### Overview
- Built on **Git**.
- Only the **md5 hash** of data files is managed by Git.
- The file itself is stored on a dedicated server.
- DVC links the **md5 hash** to the stored file, ensuring reproducibility and caching by the md5 hash of data and intermediate results.

### Key Features
- Model registry using git tags.
- Metric tracking via `dvc live`.
- Supports self-hosted storage servers.

---

# Model Engineering

### Key Considerations
- Performance in production.
- Various deployments with distinct characteristics.
- Interpretability.
- Maintainability.
- Compliance with regulations (non-discrimination).

---

# Model Cards

- [Model Cards (Research Paper)](https://arxiv.org/abs/1810.03993) - Highly recommended for understanding and documenting model performance and limitations.

---

# Model Registry

- Organizes and tracks model versions and performance metrics.
