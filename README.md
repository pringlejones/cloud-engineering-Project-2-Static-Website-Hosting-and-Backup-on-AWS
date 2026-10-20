# cloud engineering Project 2 Static Website Hosting and Backup on AWS
# Project 2: Automated Static Website Hosting & Compliant Backup Architecture

## 📌 Project Overview
Deployed an optimized, highly available static web hosting solution utilizing Amazon S3. Configured enterprise-grade data management layers including object version tracking and automated lifecycle rules to seamlessly balance architectural accessibility with cost optimization. Included an automated Python deployment script (`boto3`) to drive programmatic source updates.

## 🏗️ Core Architecture Components

* **Object Storage Isolation:** Engineered a highly scalable, public-read accessible S3 bucket configured explicitly for high-performance static web document streaming.
* **Least-Privilege Bucket Access:** Implemented a secure JSON Bucket Policy allowing global public ingress restricted solely to `s3:GetObject` actions, preventing unauthorized upload attempts or directory modifications.
* **Fault Tolerance & Version Recovery:** Activated global **Bucket Versioning** to maintain a persistent historical record of object states, protecting infrastructure assets from accidental mutations, overwrite errors, or data corruption.
* **Automated Data Lifecycle Optimization:** Designed an automated lifecycle transition rule targeting noncurrent object versions. Old backups are automatically moved to **Glacier Flexible Retrieval** cold storage after **30 days** to dramatically minimize cloud storage expenses.
* **Programmatic DevOps Pipeline (`upload.py`):** Coded a reusable deployment automation engine using the official **AWS SDK for Python (Boto3)**. The script recursively crawls local deployment directories and syncs production updates straight to the target S3 environment.

## 📁 Repository Structure
* `upload.py` - The automated Boto3 directory synchronizer tool.
* `README.md` - Technical project breakdown and architectural insights.
## 📸 Deployment & Compliance Verification

### Live Production URL:
<img width="1440" height="860" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/16b81b8b-b1ad-4f9c-aab0-527c38ed44b0" />

### Lifecycle Management Policy Configuration:
<img width="1440" height="860" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/f2f3b600-8af9-42e2-880c-2cabba46602e" />




