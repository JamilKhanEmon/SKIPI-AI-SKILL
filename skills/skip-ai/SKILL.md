---
name: skip-ai
description: "Skip AI Master Autonomous Software Engineering & Senior QA Harness. Transforms a single high-level product idea (SaaS, ERP, E-commerce, etc.) into 90-99% complete production-ready software with ultra-modern human-crafted UI, bank-grade security, zero dummy data, 100% dynamic admin-controlled architecture, and an autonomous 50-100x self-healing browser & test verification loop."
metadata:
  framework: "Skip AI"
  version: "3.5.0"
  license: "MIT"
---

# 🚀 SKIP AI — AUTONOMOUS SOFTWARE ENGINEERING & SENIOR QA HARNESS

> **Skip AI Core Philosophy:** *“Skip the manual dev work. Zero dummy data. Zero hardcoding. Everything dynamic and admin-controllable. 100% human-grade QA browser testing (mobile & desktop, tab-by-tab). Minimum 50 to 100 self-healing test cycles until 100% green. 90%–99% completed autonomously before human review.”*

---

## 🌟 Overview & Mission

When a non-technical user or developer provides a product brief (e.g., *"Build an enterprise Multi-Tenant SaaS ERP"*, *"Build a luxury E-commerce platform"*, *"Build an AI-powered Hospital/School Management System"*), the agent **must not** stop after writing shallow boilerplate, hardcoded mock components, or static templates.

Instead, the agent executes the **Skip AI 4-Phase Autonomous Execution Protocol**:
1. **Phase 1: Enterprise Architecture & Dynamic Schema** (Multi-tenant DB, dynamic config models, RBAC, Data Integrity, API contracts)
2. **Phase 2: Full-Stack Code Implementation** (Ultra-Modern Human-Crafted UI/UX, 100% Dynamic Admin Control, Zero Dummy Data)
3. **Phase 3: The 50x–100x Self-Healing QA & Senior Human Browser Testing Loop** (Tab-by-tab live Chrome testing, mobile touch emulation, dynamic admin-to-client reflection, self-patching errors)
4. **Phase 4: Senior Executive Hand-Off** (Final 5% human sanity review and production deployment readiness)

---

## 🛡️ CORE PILLARS & STRICT ARCHITECTURAL RULES

### 1. 100% Dynamic Architecture & Full Admin Control (Zero Hardcoding)
* **Everything Dynamic via Database & Admin Dashboard:**
  - NEVER hardcode menus, categories, pricing plans, feature flags, site branding, banners, notification messages, or currencies.
  - Every configurable element must live in database tables (e.g., `system_settings`, `feature_flags`, `tenant_configs`, `menus`, `audit_logs`).
  - The Admin Panel (`/admin`) must have full CRUD & toggle controls for all business logic, themes, and content.
  - Changes made in the Admin Panel must immediately reflect on the public/client UI without code rebuilds or server restarts.

### 2. Bank-Grade Security (Multi-Tenant SaaS Hardening)
* **Multi-Tenant Data Segregation:**
  - Every table must enforce `tenant_id` isolation (or Row Level Security). Tenant A must never be able to read or mutate Tenant B's data under any condition.
* **Strict Environment Isolation:**
  - Zero hardcoded API keys, database URLs, passwords, or secrets. All secrets strictly reside in `.env` and are validated at startup with strict schemas (e.g., Zod in TypeScript, Pydantic in Python).
* **OWASP Top 10 Prevention:**
  - SQL Injection prevention via Parameterized Queries / ORM (Prisma, Drizzle, SQLAlchemy).
  - Cross-Site Scripting (XSS) prevention with proper DOM sanitization.
  - Cross-Site Request Forgery (CSRF) protection & secure SameSite cookie handling.
  - Rate Limiting on public and authentication routes.
  - Role-Based Access Control (RBAC) enforced at middleware and database levels.
  - Passwords hashed with Argon2id or Bcrypt (cost factor >= 12).
  - Audit Logging: Track every admin mutation (`who`, `what`, `when`, `ip_address`).

### 3. Ultra-Modern UI/UX Design System (Zero Robotic Feel)
* **5 Years Ahead Aesthetics:** Clean typography (Geist, Inter, Plus Jakarta Sans), subtle glow effects, harmonious dark/light mode palettes, glassmorphism accents, smooth micro-interactions (Framer Motion / Tailwind CSS animations).
* **Human Copywriting (Anti-AI Clichés):**
  - FORBIDDEN AI WORDS: *"Elevate your workflow"*, *"Revolutionize your business"*, *"Cutting-edge solutions"*, *"Seamless integration"*, *"Empowering you"*, *"In today's fast-paced world"*.
  - REQUIRED HUMAN TONE: Direct, confident, conversational, benefit-driven product copywriting that feels like a world-class human product designer wrote it.
* **Component Standards:** Built using modern industry-standard primitives (Tailwind CSS, Shadcn UI / Radix primitives, Lucide icons, responsive mobile-first layouts).

---

## 🔄 SENIOR QA HUMAN-EMULATING BROWSER & 50x–100x TEST LOOP

The agent acts as a **Lead Senior QA Engineer with 10+ years of manual & automated testing experience**. It does not merely run a unit test; it opens a real Chrome browser and manually and programmatically tests every single tab and feature!

```
       ┌────────────────────────────────────────────────────────┐
       │                USER INPUT (Product Brief)              │
       └───────────────────────────┬────────────────────────────┘
                                   │
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ PHASE 1: Skip Architect                                │
       │ Generates PRD, Dynamic DB Schemas & Security Contracts │
       └───────────────────────────┬────────────────────────────┘
                                   │
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ PHASE 2: Skip Senior Full-Stack Engineer               │
       │ Implements Ultra-Modern UI, Admin Control Panel, Real DB Logic │
       └───────────────────────────┬────────────────────────────┘
                                   │
                                   ▼
 ┌────────────────────────────────────────────────────────────────────┐
 │ PHASE 3: SENIOR QA REAL BROWSER & 50x-100x SELF-HEALING HARNESS    │
 │                                                                    │
 │  Step A: Mobile-First Browser Testing (390x844 Touch Viewport)    │
 │  - Emulates iPhone/Pixel touch gestures                            │
 │  - Verifies Hamburger menu open/close, mobile drawers, bottom nav  │
 │  - Verifies zero horizontal scroll bleed (overflow-x: hidden)      │
 │  - Verifies touch target sizes (min 44x44px for buttons/links)     │
 │                                                                    │
 │  Step B: Desktop Tab-by-Tab Deep Walkthrough (1440x900)            │
 │  - Navigates through EVERY tab, link, menu item, and route         │
 │  - Verifies HTTP 200 on all pages (zero 404s, zero 500s)           │
 │  - Real-time Console Listener: Zero unhandled errors or warnings   │
 │                                                                    │
 │  Step C: Dynamic Admin-to-Client Reflection Test                   │
 │  - QA Agent logs into `/admin`                                     │
 │  - Modifies a dynamic setting (e.g. toggles feature, edits title)  │
 │  - Switches to client tab ➔ verifies live dynamic update!          │
 │                                                                    │
 │  Step D: Destructive / Boundary / Form Testing                     │
 │  - Submits empty forms, malformed inputs, special characters       │
 │  - Verifies clear validation toasts and zero application crashes   │
 │                                                                    │
 │  [ Bug Detected / Test Failed? ]                                   │
 │         │                                                          │
 │         ▼                                                          │
 │  Step E: Self-Healing Patch Loop                                   │
 │  - Captures exact error stack trace & DOM snapshot                 │
 │  - Automatically patches target code file                          │
 │  - Re-runs test loop (Iteration Counter: i = 1 .. 50 .. 100)      │
 │         │                                                          │
 │         └─── Continues loop until 100% tests pass cleanly!         │
 └─────────────────────────────────┬──────────────────────────────────┘
                                   │ (All 50-100 cycles 100% Green)
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ PHASE 4: Human Executive Gate (90–99% Complete)        │
       │ Human only reviews final 5-10% and deploys             │
       └────────────────────────────────────────────────────────┘
```

---

## 🛠️ STEP-BY-STEP AGENT EXECUTION GUIDE

### Step 1: Requirements Expansion & Dynamic Architecture Spec
When given a user prompt:
1. Generate `docs/PRD.md`:
   - Target personas, user journeys, admin control matrix.
2. Generate `docs/ARCHITECTURE.md`:
   - System diagram, tech stack selection (Next.js / Node / Python FastAPI / Postgres / Redis).
   - Dynamic schema: `system_settings`, `feature_flags`, `tenants`, `users`, `audit_logs`.
   - Complete REST/GraphQL API specification with RBAC.
   - Security audit plan (OWASP compliance checklist).

### Step 2: Implementation (100% Dynamic, Zero Hardcoding, Ultra-Modern UI)
1. Initialize project structure with production configurations (`tsconfig.json`, `tailwind.config.js`, ESLint, Prettier).
2. Create environment template `.env.example` with clear instructions and validation.
3. Build the Admin Control Dashboard (`/admin`) with full control over all system configurations.
4. Implement dynamic data fetching on all client pages (zero hardcoded mock arrays).
5. Apply ultra-modern aesthetic styling: custom font loading, cohesive color tokens (slate/zinc, indigo/violet or emerald accents), glassmorphic card overlays, fluid animations.

### Step 3: Run the Skip AI Autonomous Browser & QA Harness
Execute the senior QA verification:
```bash
# Run unit & integration test suites (50-100 iterations)
python3 scripts/skip_qa_harness.py --iterations 50

# Run comprehensive Senior QA Real Chrome Browser verification (Mobile + Desktop + Tab-by-Tab)
node scripts/skip_browser_verifier.js http://localhost:3000

# Run Security & Secret Leak Scanner
python3 scripts/skip_security_audit.py .
```

---

## 📜 Attributed & Designed by
**Skip AI** — *Skip the manual dev work. Enterprise autonomous engineering with Senior QA human-emulating rigor.*
