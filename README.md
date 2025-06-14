````markdown
# 📸 Automatic EBS Snapshot & Cleanup Using AWS Lambda & Boto3

## 📝 Overview

This project automates the process of:
- 📦 Creating snapshots for an Amazon EBS volume
- 🧹 Deleting old snapshots older than 30 days

It uses AWS Lambda (Python) and Boto3 to ensure your volumes are backed up and storage is optimized.

---

---

## 📌 Objective

To automate the process of:
- 📦 Creating snapshots of an Amazon EBS volume on a schedule
- 🧹 Deleting old snapshots older than 30 days

This ensures **automated backups** and **storage cost savings** using AWS Lambda + Boto3 (Python).

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| ✅ Snapshot Automation | Automatically creates snapshots of a specified EBS volume |
| ⏱️ CloudWatch Scheduling | Triggers Lambda weekly on Sunday at 12:00 PM IST |
| 🧹 Snapshot Cleanup | Deletes snapshots older than 30 days |
| 🔐 IAM Integration | Uses a dedicated IAM role with EC2 and logging permissions |
| 🧾 Logs | All activity logs available in CloudWatch |

---

## 🛠️ Tech Stack

- **AWS Lambda** – serverless compute
- **Python 3.12**
- **Boto3** – AWS SDK for Python
- **CloudWatch Events** – for scheduling
- **IAM Roles & Policies** – for secure access

---

## 💡 How It Works

1. Lambda is triggered weekly (via CloudWatch Event).
2. It creates a new snapshot of the specified EBS volume.
3. It filters all previous snapshots created by the Lambda function.
4. It deletes any snapshot older than 30 days.

---

## 🧾 Lambda Function Overview

```python
VOLUME_ID = 'vol-0e5b12ae3d1e23bb6'
REGION = 'ap-south-1'
RETENTION_DAYS = 30
````

📁 See full logic in [`lambda_function.py`](lambda_function.py)

---



### ✅ CloudWatch Logs

![image](https://github.com/user-attachments/assets/6677ba22-6387-4d84-9139-14e4bf30fcc1)

![image](https://github.com/user-attachments/assets/cbaed701-c2c5-4f79-a407-7b132407f73c)


### ✅ Snapshot Created

![image](https://github.com/user-attachments/assets/2edbb19a-fb4c-4f49-a8d1-52382fd91e3c)

![image](https://github.com/user-attachments/assets/4e732787-b1bb-40bb-bbd3-458d35725623)


---

## 🔒 IAM Role & Permissions

* `AmazonEC2FullAccess` — to manage snapshots
* `AWSLambdaBasicExecutionRole` — for CloudWatch logging

---

## 🧠 Best Practices Followed

* ✅ Tagging snapshots (`CreatedBy = LambdaBackup`)
* ✅ Time-based cleanup for cost control
* ✅ Reusable code and environment-based variables
* ✅ IAM role separation

---

## 🧑‍💻 Author

**👤 Vignesh Sadanki**


---

## 📃 License

This project is under the [MIT License](LICENSE)

---

```

---

