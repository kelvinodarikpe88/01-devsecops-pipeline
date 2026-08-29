# vulnbank — Deliberately Vulnerable App + Full DevSecOps Pipeline

CI pipeline that catches SQL injection, hardcoded credentials, and missing authz
before merge. Zero vulns reach `main`.

## Quick start
```bash
pip3 install -r requirements.txt
python3 app.py
# attack it: curl -X POST -d "user=a' OR '1'='1&pwd=x" localhost:5000/login
```

## Pipeline
- SAST: semgrep (p/ci + p/security-audit) → SARIF → GitHub Security tab
- SCA: pip-audit on requirements
- Secrets: gitleaks on full history
- DAST: OWASP ZAP baseline against the running app (see docs/sop.md)

## Evidence
- `docs/findings.md` — findings table with fix + re-scan proof
- `docs/sop.md` — full SOP

## Learned
- SAST alone misses authz bugs; DAST + manual review catches IDOR.
- Gitleaks on full history finds things staged scans can't.
