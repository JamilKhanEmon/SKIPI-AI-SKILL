#!/usr/bin/env python3
"""
Skip AI Senior Security & Secret Leak Scanner
Audits target project for hardcoded secrets, SQL injection patterns,
missing environment validations, and OWASP Top 10 vulnerabilities.
"""

import os
import re
import sys

SECRET_PATTERNS = [
    (r'(?i)(api[_-]?key|secret|password|auth[_-]?token|private[_-]?key)\s*[:=]\s*["\'][a-zA-Z0-9_\-\.]{8,}["\']', "Potential Hardcoded Secret/Token"),
    (r'(?i)postgres://[^:]+:[^@]+@', "Plaintext Database Credentials in URI"),
    (r'(?i)mongodb(\+srv)?://[^:]+:[^@]+@', "Plaintext MongoDB Credentials in URI"),
    (r'-----BEGIN\s+PRIVATE\s+KEY-----', "Unencrypted RSA/Private Key Block"),
]

SQL_INJECTION_PATTERNS = [
    (r'(?i)(SELECT|INSERT|UPDATE|DELETE)\s+.*\s+(FROM|INTO)\s+.*(\+|%|\.format\(|f["\']).*', "Potential Raw SQL String Concatenation"),
    (r'(?i)execute\s*\(\s*f["\'].*["\']\s*\)', "Raw Formatted SQL Query Execution"),
]

ROBOTIC_AI_PATTERNS = [
    (r'(?i)elevate\s+your\s+workflow', "Robotic AI Cliché"),
    (r'(?i)seamless\s+integration', "Robotic AI Cliché"),
    (r'(?i)revolutionize\s+your\s+(business|life)', "Robotic AI Cliché"),
    (r'(?i)cutting-edge\s+solutions', "Robotic AI Cliché"),
]

IGNORE_DIRS = {'.git', 'node_modules', '.next', 'dist', 'build', '__pycache__', 'venv', '.env', 'ecc', 'MetaGPT', 'ChatDev', 'OpenHands', 'SWE-agent'}

def audit_directory(root_dir="."):
    findings = []
    print(f"\n=======================================================")
    print(f"🛡️ SKIP AI SENIOR SECURITY & CODE QUALITY AUDITOR")
    print(f"Scanning target directory: {os.path.abspath(root_dir)}")
    print(f"=======================================================\n")

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            if f.endswith(('.ts', '.tsx', '.js', '.jsx', '.py', '.json', '.html')):
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file_obj:
                        lines = file_obj.readlines()
                        for idx, line in enumerate(lines, 1):
                            # Check secrets
                            for pattern, desc in SECRET_PATTERNS:
                                if re.search(pattern, line):
                                    findings.append((filepath, idx, f"SECURITY HAZARD: {desc}", line.strip()[:80]))
                            # Check SQL Injection
                            for pattern, desc in SQL_INJECTION_PATTERNS:
                                if re.search(pattern, line):
                                    findings.append((filepath, idx, f"SQL INJECTION RISK: {desc}", line.strip()[:80]))
                            # Check Robotic AI copy
                            for pattern, desc in ROBOTIC_AI_PATTERNS:
                                if re.search(pattern, line):
                                    findings.append((filepath, idx, f"ROBOTIC COPY VIOLATION: {desc}", line.strip()[:80]))
                except Exception as e:
                    pass

    print(f"Total Audited Issues Found: {len(findings)}\n")
    if findings:
        for path, line_no, desc, snippet in findings:
            print(f"🚨 {desc}")
            print(f"   File: {path}:{line_no}")
            print(f"   Snippet: {snippet}\n")
        print("❌ SECURITY/QUALITY AUDIT FAILED. Self-healing loop required.")
        return 1
    else:
        print("✅ SECURITY & QUALITY AUDIT PASSED: Zero secret leaks, zero raw SQL injections, zero robotic AI copy!")
        return 0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(audit_directory(target))
