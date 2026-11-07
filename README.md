<div align="center">

# ✉️ VDA-Mail (Mail_By_VDA)
### Virtual Development Assistant (VDA) — Automated SMTP Dispatcher & Transactional Email Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Organization](https://img.shields.io/badge/Powered%20By-Akash-00d4ff)](https://github.com/Powered-By-Akash)
[![Founder](https://img.shields.io/badge/Founder-Akash%20Tanna-ff007f)](https://github.com/akashtanna)
[![Engine](https://img.shields.io/badge/Protocol-SMTP__SSL%20%2F%20EmailMessage-10b981)](https://docs.python.org/3/library/smtplib.html)

**The dedicated transactional notification engine powering account security, credential recovery, and project alerts for Powered By Akash (PBA) software platforms and UDN systems.**

---

</div>

## 📌 Overview

**VDA-Mail** (internally designated `Mail_By_VDA` under the **Virtual Development Assistant** system) is an automated, zero-dependency Python messaging framework engineered to handle:
- **Encrypted Transmission**: Direct SSL communication via `smtplib.SMTP_SSL` with automatic routing for **Outlook** (`smtp-mail.outlook.com`) and **Gmail** (`smtp.gmail.com`).
- **Standardized Security Templates**: High-integrity automated formats for Two-Factor Authentication (2FA), OTPs, and verification PINs.
- **Credential Recovery & Account Lifecycle**: Automated dispatch of welcome credentials, UDN IDs, password resets, and user modification alerts.
- **Enterprise Project Receipts**: Confirmation emails generating unique project identifiers and cryptographic keys upon project creation.
- **Backwards Compatibility**: Fully interoperable with legacy imports (`import Mail_By_VDA`) and modern package workflows (`import vda_mail`).

---

## 🧩 Core Component Suite

| Component | Base Class | Primary Purpose |
|---|---|---|
| `SendVDAMail` | `smtplib.SMTP_SSL` | Secure SMTP SSL connection manager. Automatically selects Gmail or Outlook gateway, logs in, dispatches, and terminates the session cleanly. |
| `VDASecurityEmail` | `email.message.EmailMessage` | Generates 2FA, OTP, and security PIN notification messages with structured authentication headers. |
| `VDACustomEmail` | `email.message.EmailMessage` | Generalized transactional email generator with custom subject, body, sender, and recipient configuration. |
| `UDNIDEmail` | `email.message.EmailMessage` | Welcome and account activation message delivering new UDN ID credentials to onboarded users. |
| `UDNForgotDetailsEmail` | `email.message.EmailMessage` | Secure credential recovery email delivering requested UDN ID or account password. |
| `UDNUserSettingEmail` | `email.message.EmailMessage` | Security change alert notifying users of modifications to profile data, credentials, or system settings. |
| `ProjectIDEmail` | `email.message.EmailMessage` | Project generation receipt delivering Project Name, Project ID, and access Special Key. |

---

## 🚀 Installation

### Option 1: Install via Pip from GitHub
```bash
pip install git+https://github.com/Powered-By-Akash/VDA-Mail.git
```

### Option 2: Clone and Install in Editable Mode
```bash
git clone https://github.com/Powered-By-Akash/VDA-Mail.git
cd VDA-Mail
pip install -e .
```

---

## 💻 Minimal Code Example

```python
from vda_mail import SendVDAMail, VDASecurityEmail

# 1. Compose 2FA Security PIN Notification
email = VDASecurityEmail(
    user_email="client@domain.com",
    name="Akash Patel",
    security_pin_code="849201",
    security_name="UDN Portal",
    app_email="auth@poweredbyakash.in",
    security_type="pin",
    firm_name="Powered By Akash (PBA)"
)

# 2. Dispatch securely via SSL (Gmail or Outlook)
SendVDAMail(
    provider="gmail",                          # or "outlook"
    sender_email="auth@poweredbyakash.in",
    sender_email_pass="YOUR_APP_PASSWORD",
    receiver_email="client@domain.com",
    email_message=email.as_string()
)
```

---

## 🎮 Running the Verification Demo

A verification demo script is bundled with the repository:

```bash
python examples/demo.py
```

---

## 📁 Repository Structure

```
VDA-Mail/
├── __init__.py           # Legacy root entry point for Mail_By_VDA
├── vda_mail.py           # Primary module with type hints & full component suite
├── Mail_By_VDA.py        # Backward-compatibility bridge
├── setup.py              # Setuptools distribution config
├── pyproject.toml        # Modern PEP 517/518 build specification
├── LICENSE               # MIT Open Source License
├── .gitignore            # Git exclusions
├── README.md             # Documentation and usage guide
└── examples/
    └── demo.py           # Verification and usage demonstration
```

---

## 🏢 Organization & Founder

- **Organization:** [Powered By Akash (PBA)](https://github.com/Powered-By-Akash)
- **Founder & Lead Architect:** [Akash Tanna](https://github.com/akashtanna)
- **Location:** Gujarat, India
- **Official Website:** [poweredbyakash.in](https://www.poweredbyakash.in/)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
