"""
VDA-Mail Showcase Demo
======================
Demonstrates how to construct transactional emails using VDA-Mail classes.
Run:
    python examples/demo.py
"""

import sys
import os

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vda_mail import (
    VDASecurityEmail,
    VDACustomEmail,
    UDNIDEmail,
    UDNForgotDetailsEmail,
    ProjectIDEmail
)


def main():
    print("=== VDA-Mail Transactional Email Composer ===")

    # 1. Security PIN Email
    sec_email = VDASecurityEmail(
        user_email="client@example.com",
        name="Alex Mercer",
        security_pin_code="948210",
        security_name="UDN Authentication",
        app_email="auth@poweredbyakash.in",
        security_type="pin",
        firm_name="Powered By Akash (PBA)"
    )
    print("\n[1] VDASecurityEmail:")
    print(f"    Subject: {sec_email['Subject']}")
    print(f"    From:    {sec_email['From']}")
    print(f"    To:      {sec_email['To']}")

    # 2. UDN Registration ID Email
    udn_email = UDNIDEmail(
        user_email="engineer@infra.in",
        name="Rajesh Patel",
        udn_id="UDN-GJ-2025-0814",
        app_email="admin@poweredbyakash.in"
    )
    print("\n[2] UDNIDEmail:")
    print(f"    Subject: {udn_email['Subject']}")
    print(f"    To:      {udn_email['To']}")

    # 3. Project Creation Email
    proj_email = ProjectIDEmail(
        user_email="lead@consultancy.com",
        name="Vikram Shah",
        project_name="Surat Ring Road Stormwater Modeling",
        project_id="PRJ-SRT-042",
        app_email="projects@poweredbyakash.in",
        special_key="SK-9941-X7"
    )
    print("\n[3] ProjectIDEmail:")
    print(f"    Subject: {proj_email['Subject']}")
    print(f"    To:      {proj_email['To']}")

    print("\nAll transactional email generators compiled successfully!")


if __name__ == "__main__":
    main()
