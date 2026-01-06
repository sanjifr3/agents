## Title

Senior AI / Machine Learning Engineer (AI/ML Technical Lead)

## Summary

Senior AI/ML Engineer with 9+ years of experience designing, scaling, and operating production ML platforms and AI systems in regulated, uptime-critical environments.

I specialize in building and operating enterprise ML platforms, with deep experience across MLOps, LLM systems, and applied ML. My work emphasizes reliability, observability, and the safe operation of AI systems—shaped by years of independent model validation and direct ownership of mission-critical ML infrastructure.

At TD, I own and operate the Azure Machine Learning platform, translating funded business and regulatory initiatives into reliable, widely adopted platform capabilities. Under my ownership, AzureML usage scaled 400%, with 531% year-over-year cloud consumption growth, while maintaining stable, secure operations.

Earlier in my career, I built real-time autonomous robotic systems operating in physical environments, integrating perception, state, and decision-making under strict latency and reliability constraints (including on-device computer vision at the edge). This background strongly informs my current work on agentic and LLM-based systems, particularly around autonomy, failure modes, and safe operation in real-world deployments.

## Experience

TD  
Greater Toronto Area, Canada

Senior AI / Machine Learning Engineer (AI/ML Technical Lead), AI/ML Platform Engineering  
Oct 2024 - Present . 1 yr 3 mos  
Toronto, Ontario, Canada · Remote

- Expanded mandate to serve as Technical Lead and Service owner for Azure Machine Learning, accountable for platform architecture, reliability, production readiness, and safe operation across enterprise ML workloads.
- Scaled organization-wide AzureML adoption while maintaining operational stability and controlled production risk, driving 400% usage growth, 224% YoY growth in DEV/PROD workspaces, and 531% YoY increase in cloud consumption.
- Set platform technical direction and made cross-cutting tradeoffs across security, scalability, operability, and regulatory constraints; acted as a primary design-review and escalation point.
- Led delivery of core platform capabilities from concept to GA (e.g., Managed VNets, secure inference patterns, CI/CD automation, automated testing), partnering with security and consuming teams.
- Recognized with TD’s Legendary Award for scaling and stabilizing the AzureML platform and enabling MLOps, laying the foundation for high-value AI/ML initiatives.

Senior AI / Machine Learning Engineer, AI/ML Platform Engineering  
Aug 2023 - Present · 2 yr 5 mos  
Toronto, Ontario, Canada

- Owned end-to-end design, implementation, and production operation of core AzureML platform services as a hands-on individual contributor, including rollout, hardening, and ongoing reliability improvements.
- Architected and implemented a modular AzureML platform, standardizing deployments across teams and reducing environment provisioning from 3+ days to <20 minutes while cutting deployment errors by 95%.
- Built the foundational MLOps pipelines that established CI-based model scanning, and controlled artifact promotion (restricted runners → Nexus → AzureML), preventing bypass paths and unsafe deployments.
- Implemented controlled third-party model onboarding and curation workflows (Hugging Face, AzureML Model Catalog), enforcing Azure Policy–based access controls and dynamic model whitelisting to govern who can deploy which models and at what scope (management group, subscription, resource group).
- Designed and deployed LLM observability and logging services (FastAPI, PostgreSQL, Streamlit) to capture inputs, outputs, and metadata for production RAG workloads, supporting debugging, qualitative evaluation, and hands-on model comparison.
- Delivered secure networking and execution patterns for ML workloads (AzureML Managed VNets, private endpoints), taking core capabilities from POC to GA with HA/DR compliance.

Senior Applied Machine Learning Scientist, Wealth, AI/ML Center of Excellence  
Jan 2023 - Aug 2023 · 8 mos  
Toronto, Ontario, Canada · Hybrid

- Model owner and primary developer for multiple production ML systems within TD Wealth, owning architecture, design, and deployment across business-critical use cases.
- Led the redesign of a legacy, manually operated form processing solution into a real-time, self-serve ML platform, eliminating per-form custom code and human intervention.
- Built a generalized microservices-based ML inference architecture (FastAPI, MongoDB, Redis, MySQL), which replaced a ~$1.1M/year legacy system and decoupled the platform from any single use case.
- Enabled automated, no-code onboarding of new document types by designing workflows that learn from a single example and generalize to previously unseen layouts.
- Developed and deployed applied ML models across Wealth use cases, including intelligent document processing, anomaly detection, personalization, and a semantic-embedding–based video recommendation system for the TD DI Learning Center.

Senior Data Scientist, Wealth Advanced Analytics  
Aug 2021 - Jan 2023 · 1 yr 6 mos  
Toronto, Ontario, Canada

- Owned the end-to-end design and delivery of production ML systems in Wealth, translating ambiguous business problems into measurable, deployed solutions.
- Built an automated batch document processing pipeline (OpenCV, Tesseract OCR) with a two-stage detection and extraction flow to balance throughput, accuracy, and cost, delivering ~$1.1M in annual savings.
- Redesigned a large-scale Spark-based client attrition pipeline, reducing end-to-end processing time from multiple days to ~2 hours.
- Developed an active-learning–based re-ranking system for unsupervised anomaly detection, incorporating iterative human feedback to improve precision and recall in production.

Senior Data Scientist, AI/ML Model Validation  
Nov 2020 - Aug 2021 · 10 mos  
Toronto, Ontario, Canada

- Validation lead for high-risk, customer-impacting ML systems, including independently reviewing and approving the first two high-risk ML models deployed to production at TD.
- Led independent validation of pre-production ML models developed by multiple teams (including Layer6 and line-of-business teams), serving as a final gate prior to production release.
- Independently rebuilt and validated end-to-end ML pipelines (data ingestion, feature engineering, training, evaluation) in Python and PySpark to verify correctness, reproducibility, and behavioral equivalence.
- Validated high-risk models serving 1M+ Visa cardholders, assessing robustness, stability, and failure modes under regulatory and operational constraints.
- Trained challenger and comparison models (Python XGBoost) to validate behavior against production implementations (xgboost4j, xgboost), identifying bugs, inconsistencies, and performance regressions.
- Designed and built systematic evaluation frameworks and automated validation tooling to scale regression testing, reproducibility checks, and production readiness assessments across teams.

Data Scientist, AI/ML Model Validation  
Jul 2019 - Nov 2020 · 1 yr 5 mos  
Greater Toronto Area, Canada

- Early hire on the Model Validation team, helping establish enterprise-wide standards and frameworks for evaluating production AI/ML systems.
- Co-designed a model validation framework defining correctness, reproducibility, robustness, interpretability, and fairness, forming the baseline for high-risk model reviews.
- Independently validated production ML systems by rebuilding data pipelines and training workflows to verify correctness, reproducibility, and alignment with business objectives.
- Redesigned large-scale data ingestion and feature pipelines using PySpark, enabling auditable, scalable evaluation of production models.
- Evaluated Java-based ML models, analyzing behavior, interpretability, and bias to identify bugs, performance bottlenecks, and reliability issues.

---

AI Engineer  
Insight Data Science  
Jan 2019 - May 2019 · 5 mos  
Greater Toronto Area, Canada

- Designed and built an end-to-end multimodal generative AI system, converting images and videos into natural language and audio descriptions to improve accessibility in a real-time application.
- Trained CNN–RNN models in PyTorch, integrating visual feature extraction with sequence-based language generation and iteratively improving performance through evaluation.
- Built and deployed low-latency, production-ready inference APIs on AWS, supporting real-time predictions for web and internal applications.
- Implemented and operated model-serving infrastructure (Flask, Gunicorn, NGINX), optimizing reliability, latency, and throughput in production.

---

University of Toronto  
Greater Toronto Area, Canada

AI / Autonomous Systems Engineer (Research)  
Sep 2016 - May 2019 · 2 yrs 9 mos

- Designed and deployed fully autonomous robotic systems making deterministic, real-time decisions based on perception in real-world physical environments, supporting both single- and multi-agent operation.
- Architected perception → reasoning → action pipelines enabling autonomous decision-making and agent coordination under strict latency, compute, and reliability constraints at the edge.
- Built and deployed concurrent real-time computer vision services on NVIDIA Jetson, including RGB-D direction-invariant person detection (79% mAP), facial recognition, and custom object detection models, operating simultaneously under tight compute budgets.
- Designed distributed, multi-computer robotic systems using low-latency pub/sub and modular service APIs (C++ and Python) over onboard networks, enabling a central control system to query perception and reasoning services in real time.
- Implemented on-device state and persistent embedding-based identity vector store to enable context-aware behavior across missions without cloud dependency.
- Owned systems end-to-end on Linux-based platforms, from model training and evaluation to on-device deployment, live experimentation, and debugging hardware–software integration failures; results published in peer-reviewed journals.

Head Teaching Assistant / Teaching Assistant.  
Sept 2017 - Apr 2019

- Led and supported teaching teams for undergraduate and graduate courses in data science, machine learning, and mechatronic systems.
- Delivered tutorials and office hours covering Python, ML, C++, and ROS; supported grading and course logistics for large cohorts.

---

Computer-Aided Engineering (CAE) Co-op  
ABC Group  
May 2015 - Aug 2015 · 4 mos  
Greater Toronto Area, Canada

- Supported mechanical design, testing, and analysis activities in an engineering validation environment (Solidworks, Ansys)
- Prepared FEA/CFD analysis reports and RFQs for engineering approval.

---

Undergraduate Research Assistant  
University of Waterloo  
Jan 2015 - Apr 2015 · 4 mos  
Waterloo, Ontario, Canada

- Conducted undergraduate research involving experimental design, data analysis, and technical reporting in a materials engineering context.

---

Development Engineering Assistant, PW800 Program  
Pratt & Whitney Canada  
Sep 2014 - Dec 2014 · 4 mos  
Greater Toronto Area, Canada

- Supported aerospace development engineering activities, including compliance tracking and data analysis (Excel VBA).

---

Durability Tester  
General Motors  
Dec 2013 - Mar 2014 · 4 mos  
Kapuskasing, Ontario, Canada

- Supported cold-weather vehicle durability testing, performing root-cause analysis and collaborating with engineering and mechanical teams.

---

Industrial Engineering Co-op  
Polycon Industries Inc  
May 2013 - Aug 2013 · 4 mos  
Guelph, Ontario, Canada

- Supported industrial engineering and process improvement initiatives in a manufacturing environment.
- Executed continuous improvement projects saving $9,765 annually.

---

Electronic Engineering Co-op  
Conspec Controls Inc  
Sep 2012 - Dec 2012 · 4 mos  
Greater Toronto Area, Canada

- Assisted with assembly, testing, and troubleshooting of electronic control equipment

---

Collections Agent  
Global Credit & Collection Inc.  
Feb 2012 - Apr 2012 · 3 mos  
Markham, Ontario, Canada

- Worked in a high-volume customer-facing environment requiring negotiation, professionalism, and conflict resolution.

## Education

University of Toronto  
Master of Applied Science (MASc), AI, Machine Learning, Computer Vision, Robotics

---

University of Waterloo  
Bachelor of Applied Science (BASc), Mechanical Engineering, 85.37%

## Licenses & Certifications

- Microsoft Certified: Azure AI Engineer Associate
- Microsoft Certified: Azure Data Scientist Associate
- Microsoft Cerfified: Azure Administrator Associate
- Microsoft Certified: Azure AI Fundamentals
- Microsoft Certified: Azure Fundamentals
- DeepLearning.ai Deep Learning Specialization

## Honors and Awards

Legendary Award  
Issued by TD · Oct 2025  
Associated with TD

Legendary Award (Q4 FY25) for outstanding transition from IC to technical leader, scaling the AI platform and enabling MLOps, Responsible AI, and custom RAG adoption while strengthening secure, stable operations.

## Skills

Core Technologies & Tools

- Apache Spark
- Ansible
- SQL
- Docker
- Kubernetes
- MLflow
- FastAPI
- MongoDB
- Redis
- Terraform
- Python
- C++
- git
- Java
- PyTorch
- TensorFlow
- Linux
- Bash
- OpenCV

Cloud Platforms

- Microsoft Azure
- Microsoft Azure Machine Learning
- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)
- OpenAI

AI/ML Specializations

- Large Language Models (LLM)
- Deep Learning
- Machine Learning
- Computer Vision
- Natural Language Processing (NLP)
- Natural Language Generation
- Generative AI
- Foundation Models
- Multimodal
- Recurrent Neural Networks (RNN)
- Convolutional Neural Networks (CNN)

MLOps & Data Engineering

- DevOps
- MLOps
- Large Language Model Operations (LLMOps)
- CI / CD
- GitOps
- Data Quality
- Data Versioning
- Data Pipelines
- Extract, Transform, Load (ETL)
- PySpark
- Streaming Systems
- Feature Stores
- Distributed Training
- Distributed Systems

ML Engineering Practices

- Model Monitoring
- Model Evaluation
- Model Validation
- Model Serving
- Model Fine-Tuning
- Model Interpretability
- Model Reproducibility
- Model Robustness & Reliability
- Production Machine Learning Systems
- Scalable ML Systems
- Experiment Tracking
- ML Observability
- Hyperparameter Optimization
- Feature Engineering

Specialized AI Techniques

- Retrieval-Augmented Generation (RAG)
- AI Agents
- Prompt Engineering
- Tool Use / Function Calling
- Agent Frameworks
- Embedding
- Vector Search
- LLM Inference Optimization
- LLM Safety & Alignment
- LLM Evaluation
- Retrieval Evaluation
- Sequence Models

ML Governance & Safety

- Fairness & Bias
- Risk-Aware Machine Learning
- Active Learning
- Anomaly Detection
- Unsupervised Learning

Software Engineering

- Microservices
- API Design
- Software Design
- Software Architecture
- Technical Leadership
- Pub/Sub Architectures
- Jenkins
- Python Packaging

Specialized Domains

- Knowledge Graphs
- Model Distillation
- Hadoop
- Scala
- Cloud Computing

## Languages

- English
- Tamil
