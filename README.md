# Quantum-Resistant Blockchain for Secure Medical Data Sharing

A secure **Electronic Medical Records (EMR)** system integrating **quantum-resistant cryptography**, **blockchain**, **attribute-based access control (ABE)**, and **IPFS-based decentralized storage** to ensure privacy, integrity, and controlled medical data sharing across healthcare entities.

---

## Overview

This project provides a **future-proof**, **tamper-proof**, and **privacy-preserving** solution for sharing medical records between patients, doctors, and healthcare institutions.

It addresses common EMR challenges:

- Weak access control
- Centralized storage vulnerabilities
- Long-term risks from quantum computing
- Lack of transparent and immutable audit trails

---

## Key Features

### Quantum-Resistant Encryption
- Uses **CRYSTALS-Kyber** for key encapsulation
- Uses **AES-GCM / NaCl** for payload encryption

### Attribute-Based Encryption (ABE)
- Patients define fine-grained access policies
- Doctors can decrypt only if their attributes satisfy the policy
- Example: `(Cardiology AND Orthopedics)`

### IPFS-Based EMR Storage
- EMR files are encrypted before upload to IPFS
- Only authorized users can decrypt the files

### Normal and Emergency Access
- **Normal Access:** Doctor requests → Patient approval → ABE policy applied
- **Emergency Access:** Doctor requests emergency override → Patient notified

### Blockchain-Based Access Control
- Logs all access requests, approvals, and emergency events
- Ensures immutability, transparency, and full audit trail

### PyQt5 and Streamlit Interfaces
- **Patient UI:** policy creation, approvals, encryption, upload
- **Doctor UI:** certificate login, EMR request, decryption

---

## System Architecture Flow

1. Doctor Request  
2. Certificate Authentication  
3. Patient Policy Approval  
4. ABE Policy Generation  
5. EMR Encryption (Kyber + AES-GCM)  
6. Upload to IPFS  
7. Blockchain Logging  
8. Authorized Decryption  

---

## Folder Structure

```

Quantum-Resistant-Blockchain-EMR
├── backend/
│   ├── blockchain/
│   ├── encryption/
│   ├── abe/
│   ├── ipfs/
│   └── server/
├── frontend/
│   ├── pyqt/
│   └── streamlit/
├── certificates/
├── tests/
├── requirements.txt
└── README.md

````

---

## Tech Stack

**Backend:**
- Python 3.x
- Flask
- Pyfhel / Charm-Crypto (ABE)
- Kyber Python library (quantum-resistant KEM)
- PyNaCl
- IPFS API
- Web3.py

**Frontend:**
- PyQt5
- Streamlit

**Storage:**
- IPFS decentralized file storage

**Security:**
- CRYSTALS-Kyber
- AES-GCM
- SHA-256 / SHA-3 hashing

---

## Installation and Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate         # Linux/Mac
venv\Scripts\activate            # Windows
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Backend Server

```bash
python patient.py
```

### 4. Run Frontend Interfaces

**Streamlit:**

```bash
streamlit run app.py
```

**PyQt5:**

```bash
python ui_main.py
```

---

## Core Modules

**Access Policy Handler (ABE):**

* Converts user-defined access rules into ABE structures
* Encrypts EMR using Ciphertext-Policy ABE

**Blockchain Logger:**

* Records doctor requests
* Records patient approvals
* Records emergency access events

**IPFS Manager:**

* Handles encrypted EMR upload and retrieval
* Validates IPFS hash integrity

**EMR Encryption Pipeline:**

* Encrypt EMR with AES-GCM
* Encapsulate AES key with Kyber
* Store encrypted EMR in IPFS
* Log access details on blockchain

---

## Testing

Run all unit tests:

```bash
pytest tests/
```

---

## Future Enhancements

* Integration with FHIR / HL7 standards
* Zero-knowledge proofs for policy verification
* Mobile app for real-time approvals
* Multi-patient and multi-hospital interoperability

---

## License

**MIT License**
Free for academic and research purposes
