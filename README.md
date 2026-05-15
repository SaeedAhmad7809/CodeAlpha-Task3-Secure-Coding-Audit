Secure Coding Review Report
1. Project Overview
Programming Language: Python
Framework: Flask
Objective: To assess a web-based login system and identify security vulnerabilities such as SQL Injection and XSS.
2. Security Audit Findings
A. SQL Injection (High Severity)
The application constructs SQL queries using unsanitized user input. An attacker can bypass authentication using payloads like ' OR '1'='1.
B. Cross-Site Scripting (XSS) (Medium Severity)
User input is rendered without proper escaping, allowing execution of malicious scripts in the browser.
3. Automated Static Analysis (SAST)
Tool Used: Bandit
Findings:
- B608: Hardcoded SQL string
- B308: Unsafe template rendering
4. Remediation & Best Practices
- Use parameterized queries
- Enable input/output sanitization
- Integrate security tools into CI/CD
- Follow secure coding standards
5. Conclusion
The application contains critical vulnerabilities. Immediate fixes and adoption of secure coding practices are required.