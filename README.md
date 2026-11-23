# HealthSync-SRE
**Automated Self-Healing & Compliance Monitoring for Mission-Critical Medical Data**

`AWS Lambda` | `Amazon RDS` | `Python` | `SRE Mindset` | `HIPAA Compliance`

> **Mission Statement:** In healthcare infrastructure, downtime isn't just a business loss—it's a risk to patient care. This project demonstrates a **High-Reliability** architecture designed to detect, log, and auto-remediate database connection failures while maintaining strict **Regulatory Compliance**.

---

## Core Features
* **Automated Self-Healing:** Leverages AWS CloudWatch Alarms to trigger Lambda-based remediation, reducing Mean Time to Recovery (MTTR) from minutes to seconds.
* **Compliance-First Design:** Implements `ForceFailover=False` logic to prioritize **Data Integrity** and prevent record corruption during recovery cycles.
* **Auditability:** Every healing event is logged via Amazon SNS and CloudWatch Logs, providing a transparent trail for **HIPAA** and **SOC2** auditors.
* **Founder’s Logic:** Built with a focus on **Operational Excellence**—minimizing manual "toil" so engineers can focus on feature growth rather than fire-fighting.

---

## The "Healer" Logic (`handler.py`)
This Python-based watchdog monitors the health of the medical database and executes a safe reboot if connection thresholds are breached.

```python
import boto3
import os

rds = boto3.client('rds')

def lambda_handler(event, context):
    db_id = os.environ['DB_INSTANCE_ID']
    print(f"Health Alert: Initiating self-healing for {db_id}")
    
    try:
        # Executing a non-destructive reboot to clear connection bottlenecks
        rds.reboot_db_instance(
            DBInstanceIdentifier=db_id, 
            ForceFailover=False
        )
        return {"statusCode": 200, "status": "Healed"}
    except Exception as e:
        print(f"Healing Failed: {str(e)}")
        return {"statusCode": 500, "status": "Failed"}
```

---

## Verification & Fault Injection Testing
To validate automated recovery and HIPAA-compliant audit logging, a simulated alarm state was injected into the pipeline:

### 1. Automated Remediation Audit Trail (CloudWatch Logs)
![CloudWatch Logs Audit Trail](CloudWatch%20Logs.png)

### 2. Database Recovery Verification (RDS Events)
![RDS Instance Restart Verification](DB%20instance%20reboot.png)

---

## SRE Objectives

### Service Level Indicators (SLIs)
* **Availability:** Successful connection rate to the Medical RDS instance.
* **Latency:** Time taken to complete the automated reboot cycle.

### Service Level Objectives (SLOs)
* Maintain **99.99% Uptime** for core data pipelines.
* Automated recovery must trigger within **30 seconds** of alert breach.

---

*Developed by Kunapuli Jyothsna Sravani | Senior IT Professional | AWS AI & ML Scholar*
