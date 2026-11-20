# 👨‍💻 DEVELOPER USAGE GUIDE — SKIPI AI SKILL
> **Comprehensive Guide on How Developers and Non-Technical Creators Use Skipi AI Skill**

---

## ⚡ 1-Click Installation into Google Antigravity

Run this one-line command in your terminal to install Skipi AI skill globally:

```bash
curl -fsSL https://raw.githubusercontent.com/JamilKhanEmon/SKIPI-AI-SKILL/main/install.sh | bash
```

*Or manually clone into Antigravity's global skills directory:*
```bash
git clone https://github.com/JamilKhanEmon/SKIPI-AI-SKILL.git ~/.gemini/antigravity/skills/skipi-ai-skill
```

---

## 🎯 3 Ways to Use Skipi AI Skill

### 🚀 Approach 1: Inside AI IDEs (Antigravity, Cursor, Claude Code) — *Recommended*

This is the primary and most powerful workflow. The developer never writes boilerplate code; the agent handles the entire development lifecycle autonomously.

#### Step 1: Open the Workspace in Your AI IDE
Open this project folder in **Google Antigravity**, **Cursor**, or **VS Code** with Claude Code. The IDE automatically discovers the framework configuration:
* **Antigravity:** `.antigravity-plugin/plugin.json` and `skills/skipi-ai-skill/SKILL.md`
* **Cursor:** `.cursor/rules/skip-engineer.mdc`
* **Claude Code:** `.claude-plugin/plugin.json`
* **MCP Integration:** `.mcp.json` (Chrome DevTools and Playwright automation)

#### Step 2: Provide a Product Brief in Chat
In the agent chat, provide a high-level requirement for the application you want to build. You can be concise or comprehensive:

```text
Build an Enterprise Multi-Tenant SaaS ERP platform where organizations manage inventory, 
invoices, and staff permissions. Everything must be dynamic and manageable from an Admin Panel. 
Follow the Skipi AI skill protocol: ultra-modern human-grade UI, zero dummy data, 
bank-grade security, and run a 50x self-healing test loop with live Chrome browser verification.
```

#### Step 3: Autonomous Multi-Phase Execution
1. **Phase 1 (Skipi Architect):** Generates `docs/PRD.md`, `docs/ARCHITECTURE.md`, and dynamic database schemas (`system_settings`, `tenants`, `feature_flags`, `audit_logs`).
2. **Phase 2 (Skipi Engineer):** Builds production code (e.g., Next.js, Tailwind CSS, PostgreSQL/Prisma) with ultra-modern design aesthetics and a full-featured Admin Control Panel (`/admin`).
3. **Phase 3 (Skipi Senior QA & Browser Tester):** Launches a live Chrome instance (Playwright) — tests mobile viewport (390x844), hamburger drawer, all internal tabs, and verifies dynamic reflection between admin and client views.
4. **Phase 4 (Self-Healing Loop):** If any test fails or console error is caught, the agent parses the stack trace, patches the code, and re-executes up to 50–100 iterations until 100% green.
5. **Phase 5 (Executive Delivery):** Delivers a 95% complete production build ready for final human sanity review and deployment.

---

### 💻 Approach 2: Running Senior QA & Security Tools from the Terminal

If you already have an application running locally (e.g., on `http://localhost:3000`), you can execute Skipi AI skill's automated QA harnesses directly from the command line:

#### 1. Live Chrome Human-Emulating Browser QA
```bash
# Opens Chrome, tests mobile view, visits every tab, tests interactive elements, and audits console errors:
node scripts/skip_browser_verifier.js http://localhost:3000
```
* **Output:** Viewport screenshots saved in `artifacts/screenshots/` and structured audit logs saved in `artifacts/qa_audit_report.json`.

#### 2. Run 50x Self-Healing Test Harness
```bash
# Runs the automated test suite 50 times in a row, triggering self-healing on failure:
python3 scripts/skip_qa_harness.py --iterations 50
```

#### 3. Run 100x Continuous Stress QA Loop
```bash
python3 scripts/skip_qa_harness.py --iterations 100
```

#### 4. Run Bank-Grade Security & Secret Leak Scanner
```bash
# Scans source code for leaked credentials, SQL injection hazards, and robotic AI clichés:
python3 scripts/skip_security_audit.py .
```

---

### 📦 Approach 3: Integrating Skipi AI Skill into Any Existing Project

To bring Skipi AI skill into an existing repository or workflow:
1. Copy the `skills/skipi-ai-skill/` directory into your project root or your global `.gemini/antigravity/skills/` directory.
2. Copy `.mcp.json` into your project root to grant your agent access to Chrome DevTools and Playwright.
3. In your AI chat, instruct the agent:
```text
Activate Skipi AI skill. Audit my existing codebase, eliminate all hardcoded configs 
with dynamic admin models, and run live Chrome browser tests to catch and patch all issues.
```

---

## 📋 Summary of Developer Expectations

| Aspect | Standard Enforced by Skipi AI Skill |
|---|---|
| **Human Coding Required** | **Zero.** The agent authors all architecture, frontend, backend, and migrations. |
| **Data Integrity** | **Zero Dummy Data.** Every view is backed by real relational database queries. |
| **Configurability** | **100% Dynamic.** Zero hardcoded values; all settings controllable via `/admin`. |
| **UI/UX Aesthetics** | **Futuristic.** Tailored typography, harmonic color tokens, zero AI clichés. |
| **Testing Rigor** | **50x–100x Self-Healing QA.** Live Chrome browser navigation across mobile and desktop. |
| **Human Role** | **Final Reviewer (5%–10%).** Approves final delivery and configures production domain. |
