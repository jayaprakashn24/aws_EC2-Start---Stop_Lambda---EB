```md
# AWS EC2 Start/Stop Automation using Lambda + EventBridge

## 🔧 Overview

This solution automates the **starting and stopping of EC2 instances** based on a schedule using:

- Amazon EC2 (compute instances)
- AWS Lambda (serverless execution)
- Amazon EventBridge (scheduler)

---

## ⚙️ Architecture

```

EventBridge (Schedule)
↓
Lambda Function
↓
EC2 API (Start/Stop Instances)

````

---

## 🧠 How It Works

1. EventBridge triggers at a defined time (cron schedule)
2. It invokes a Lambda function
3. Lambda calls EC2 APIs to start or stop instances

---

## 🪜 Implementation Steps

### 1. Create EC2 Instance(s)

- Example:
  - Development server
  - QA server
  - Batch processing instance

---

### 2. Create IAM Role for Lambda

Attach permissions:

```json
{
  "Effect": "Allow",
  "Action": [
    "ec2:StartInstances",
    "ec2:StopInstances"
  ],
  "Resource": "*"
}
````

---

### 3. Create Lambda Function

#### Python Example:

```python
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_ids = ['i-1234567890abcdef0']

    if event['action'] == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        print("Instances started")

    elif event['action'] == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)
        print("Instances stopped")
```

---

### 4. Create EventBridge Rules

#### 🟢 Start Rule (9:00 AM)

```json
{
  "action": "start"
}
```

#### 🔴 Stop Rule (7:00 PM)

```json
{
  "action": "stop"
}
```

#### Cron Expressions

```
cron(0 9 * * ? *)   → 9 AM daily
cron(0 19 * * ? *)  → 7 PM daily
```

---

## 🧪 Real-Time Use Case

### 🏢 Scenario: IT Company (Development Environment)

* 20 EC2 instances
* Used only during office hours (9 AM – 7 PM)

### ❌ Problem:

Instances run 24/7 → high cost

### ✅ Solution:

* Auto start at 9 AM
* Auto stop at 7 PM

---

## 💰 Cost Savings Example

| Metric        | Before    | After   |
| ------------- | --------- | ------- |
| Daily Runtime | 24 hrs    | 10 hrs  |
| Monthly Cost  | ₹1,00,000 | ₹42,000 |
| Savings       | ❌         | ₹58,000 |

👉 Approx. **58% cost reduction**

---

## 🌍 Additional Use Cases

### 1. Development & Testing

* Stop servers after work hours

### 2. Batch Processing

* Start before job execution
* Stop after completion

### 3. Training Labs

* Auto start/stop based on schedule

### 4. E-commerce Scaling

* Reduce infra during non-peak hours

---

## 📈 Business Impact

### 💰 Cost Optimization

* Pay only for active usage

### ⚡ Efficiency

* No manual intervention

### 🔒 Governance

* Enforces infrastructure policies

### 📊 Predictable Billing

* Controlled usage patterns

---

## ⚠️ Important Considerations

### 1. Stateful Applications

* Instance stop clears RAM
* Use EBS for persistence

### 2. Production Systems

* Avoid stopping critical workloads

### 3. Time Zone Awareness

* EventBridge uses UTC
* IST = UTC +5:30

---

## 🚀 Advanced Enhancements

### 🔹 Tag-Based Automation

```python
Filters=[
    {'Name': 'tag:AutoSchedule', 'Values': ['true']}
]
```

---

### 🔹 Multi-Environment Scheduling

| Environment | Behavior      |
| ----------- | ------------- |
| Dev         | Stop at night |
| QA          | Stop weekends |
| Prod        | Always ON     |

---

### 🔹 Notifications

* Use SNS for alerts (email/SMS)

---

## 🧩 Analogy

Like office lights:

* ON at 9 AM
* OFF at 7 PM

Automatically — no human effort needed

---

## 🏁 Summary

This solution:

* Automates EC2 lifecycle
* Reduces cloud cost significantly
* Improves operational efficiency

**Key Services Used:**

* EC2
* Lambda
* EventBridge

---

## 📌 Next Steps

* Add Terraform / CloudFormation
* Implement tagging strategy
* Add monitoring & alerts

```
```
