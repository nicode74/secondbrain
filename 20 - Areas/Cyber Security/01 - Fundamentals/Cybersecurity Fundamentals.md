# Study Note: Cybersecurity Fundamentals
Subject: #study/cybersecurity 
Status: #study/learning 

## 📖 Key Concepts & Definitions
- **CIA Triad**: Confidentiality, Integrity, and Availability – the cornerstone of security.
- **DAD Triad**: Disclosure, Alteration, and Destruction (the opposite of CIA).
- **Vulnerability**: A weakness in a system or network that can be exploited.
- **Threat**: A potential event or person that could harm a system by exploiting a vulnerability.
- **Risk**: The likelihood that a threat will exploit a vulnerability and the resulting impact. (Risk = Threat × Vulnerability × Impact).

## 📝 Detailed Notes

### The CIA Triad Breakdown
1. **Confidentiality**: Ensuring that sensitive information is only accessed by authorized individuals.
   - *Tools*: Encryption, Access Control Lists (ACLs), MFA.
2. **Integrity**: Ensuring that data remains accurate and has not been tampered with.
   - *Tools*: Hashing (MD5, SHA), Digital Signatures, Version Control.
3. **Availability**: Ensuring that systems and data are accessible when needed.
   - *Tools*: Redundancy (RAID), Backups, DDoS Protection, Load Balancing.

### The AAA Framework
- **Authentication**: Proving who you are (something you know, have, are, or do).
- **Authorization**: Determining what you are allowed to do.
- **Accounting**: Tracking what you did (logging and auditing).

### Types of Security Controls
- **Administrative (Managerial)**: Policies, procedures, training, background checks.
- **Technical (Logical)**: Firewalls, encryption, IDSs, passwords.
- **Physical**: Locks, guards, cameras, biometric scanners.

## 🧠 Questions & Flashcards
- **Q**: What is the "Defense in Depth" strategy?
  - **A**: Layering multiple security controls (administrative, technical, and physical) so that if one fails, others remain to protect the system.
- **Q**: Explain the difference between Hashing and Encryption.
  - **A**: Hashing is a one-way process used for integrity (detecting changes); Encryption is a two-way process used for confidentiality (hiding data).

## ✍️ Practice / Application
- [ ] Research a recent major data breach and identify which part of the CIA triad was compromised.
- [ ] Practice hashing a file using `sha256sum` in Linux.

## 📅 Review Schedule
- [ ] First Review (Today)
- [ ] Second Review (Tomorrow)
- [ ] Final Review (Next Week)
