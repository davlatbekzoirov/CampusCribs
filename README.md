# CampusCribs 🏠💰

A comprehensive, full-stack Django web application designed to help students navigate the financial and logistical complexities of independent living. It combines group expense splitting, co-living chore accountability, sublet/housing search tracking, and student-optimized budgeting into a single, secure hub.

## 🚀 Key Modules & Core Features

### 1. Smart Student Budgeter & "Instant Noodle" Alerts (`budget`)
* **Student-Centric Ledger:** Track income streams (allowances, part-time jobs, scholarships) against customizable expense categories (textbooks, groceries, social, transport).
* **Predictive Runway Calculator:** Evaluates daily non-essential spending velocity against remaining semester target countdown milestones to forecast the exact exhaustion date.
* **"Instant Noodle" Alerts:** Interactive dashboard warning banners that automatically trigger when spending velocity compromises fixed liabilities like utility quarters or rent chunks.

### 2. Frictionless Roommate Expense Splitter (`roomieratio`)
* **Group Ledgers:** Create a unified household environment where roommates log shared apartment responsibilities (Wi-Fi bills, utility splits, collective household supplies).
* **Simplified Balance Matrix:** Implements an aggregate net calculation logic to track custom itemized shares or symmetric flatmatic debts easily.
* **Gamified Chore Rotation:** Automates weekly chore wheels (trash, kitchen deep-clean) that rotate tasks and track accountability via photo verification file asset uploads.
* **Karma Ledger:** Earn Karma Points (KP) for verified on-time completions, tracking overall household stats with friendly automated slacker notifications.

### 3. Housing Search & Sublet CRM Tracker (`housing`)
* **Kanban Pipeline Board:** Visually progress potential apartment properties through stages from initial detection (`Found`) $\rightarrow$ `Viewing Scheduled` $\rightarrow$ `Applied` $\rightarrow$ `Lease Signed`.
* **Amenity Scoring System:** Evaluates potential listings based on specific housing criteria, including distance to campus, transit scores, and Wi-Fi speed cap ratings.

---

## 🛠️ Project Architecture

```text
.
├── accounts       # User Profile Authentication & Registration Logics
├── budget         # Individual Ledger Ledgering & Predictive Engine
├── roomieratio    # Shared Group Ledgers, Matrix Metrics, Chore Rotation
├── housing        # Kanban Prospect CRM Pipeline & Amenity Matrices
├── core           # Base Project Settings & Master Routing Configuration
└── templates      # Unified Global Styling Interface Skins