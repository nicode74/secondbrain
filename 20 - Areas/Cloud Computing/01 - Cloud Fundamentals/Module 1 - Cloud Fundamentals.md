# Study Note: Module 1 - Cloud Fundamentals
Subject: #study/cloud 
Status: #study/learning 

## 📖 Key Concepts & Definitions
- **NIST (National Institute of Standards and Technology)**: Defines the 5-3-4 cloud model.
- **Shared Responsibility Model**: The cloud provider is responsible *of* the cloud (hardware, regions); the customer is responsible *in* the cloud (data, OS, IAM).
- **Scalability**: The ability to grow as workload increases (Vertical vs. Horizontal).
- **Elasticity**: The ability to scale *in* and *out* automatically based on demand.
- **High Availability (HA)**: Ensuring the system is always reachable, typically through multi-region deployment.

## 📝 Detailed Notes

### The 5 Essential Characteristics (NIST)
1. **On-demand self-service**: Provision resources without human intervention.
2. **Broad network access**: Available over the internet from any device.
3. **Resource pooling**: Multi-tenancy (serving multiple customers using the same hardware).
4. **Rapid elasticity**: Scale up or down quickly.
5. **Measured service**: Pay-as-you-go (utility-based pricing).

### The 3 Service Models
- **IaaS (Infrastructure as a Service)**: Host (e.g., AWS EC2, Azure VM). You manage the OS, apps, and data.
- **PaaS (Platform as a Service)**: Build (e.g., AWS Elastic Beanstalk, Heroku). You manage only the application and data.
- **SaaS (Software as a Service)**: Consume (e.g., Gmail, Dropbox, Salesforce). The provider manages everything.

### Deployment Models
- **Public Cloud**: Owned by providers (AWS, Azure).
- **Private Cloud**: Dedicated to one organization (On-premise or hosted).
- **Hybrid Cloud**: Combination of Public and Private.
- **Community Cloud**: Shared by organizations with common interests (e.g., Government, Healthcare).

## 🧠 Questions & Flashcards
- **Q**: What is the difference between Vertical and Horizontal Scaling?
  - **A**: Vertical (Scaling Up) means adding more power (CPU/RAM) to an existing machine; Horizontal (Scaling Out) means adding more machines (instances) to the system.
- **Q**: Under the Shared Responsibility Model, who is responsible for patching the guest OS in an IaaS environment?
  - **A**: The Customer.

## ✍️ Practice / Application
- [ ] Create a free-tier account on **AWS**, **Azure**, or **GCP**.
- [ ] Explore the "Billing Dashboard" to understand how costs are tracked.

## 📅 Review Schedule
- [ ] First Review (Today)
- [ ] Second Review (Tomorrow)
- [ ] Final Review (Next Week)
