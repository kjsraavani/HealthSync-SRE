[healthsync-sre-readme.pdf](https://github.com/user-attachments/files/34823336/healthsync-sre-readme.pdf)
# HealthSync-SRE
Automated Self-Healing &amp; Compliance Monitoring for Medical RDS
HealthSync-SRE
Automated Self-Healing & Compliance Monitoring for Mission-Critical Medical
Data
AWS Lambda Amazon RDS Python SRE Mindset HIPAA Compliance
Mission Statement: In healthcare infrastructure, downtime isn't just a business
loss—it's a risk to patient care. This project demonstrates a High-Reliability
architecture designed to detect, log, and auto-remediate database connection
failures while maintaining strict Regulatory Compliance.
Core Features
Automated Self-Healing: Leverages AWS CloudWatch Alarms to trigger Lambdabased
remediation, reducing Mean Time to Recovery (MTTR) from minutes to
seconds.
Compliance-First Design: Implements ForceFailover=False logic to prioritize
Data Integrity and prevent record corruption during recovery cycles.
Auditability: Every healing event is logged via Amazon SNS and CloudWatch Logs,
providing a transparent trail for HIPAA and SOC2 auditors.
Founder’s Logic: Built with a focus on Operational Excellence—minimizing
manual "toil" so engineers can focus on feature growth rather than fire-fighting.
The "Healer" Logic (handler.py)



SRE Objectives
Service Level Indicators (SLIs)
Availability: Successful connection rate to the Medical RDS instance.
Latency: Time taken to complete the automated reboot cycle.
Service Level Objectives (SLOs)
Maintain 99.99% Uptime for core data pipelines.
Automated recovery must trigger within 30 seconds of alert breach.



Developed by Kunapuli Jyothsna Sravani | Senior IT Professional | AWS AI & ML Scholar
