# CampusCribs 🏠

A full-stack Django web application that helps students manage the financial and logistical side of independent living — budgeting, shared expenses, chore tracking, and apartment hunting, all in one place.

---

## Modules

### Budget — Personal Ledger & Spending Runway (`budget`)

Track income (allowances, part-time work, scholarships) against categorised expenses (rent, groceries, textbooks, social).

- **Predictive runway calculator** — measures daily non-essential spending velocity over a trailing 14-day window and projects when your balance will run out relative to the semester end date.
- **"Instant Noodle" alerts** — dashboard warnings that fire when your spending trajectory threatens to undercut fixed costs like rent or utilities before the semester ends.

---

### RoomieRatio — Shared Expenses & Chores (`roomieratio`)

A shared household namespace where roommates log and split bills (Wi-Fi, utilities, groceries).

- **Debt simplifier** — implements a greedy debt-minimisation algorithm in `utils.py`. It nets balances across all members and pairs the largest debtors directly with the largest creditors, reducing the number of transactions needed to settle up.
- **Chore tracker** — displays active chore assignments with due dates and supports image-proof uploads to mark tasks as complete.

---

### Housing — Apartment Search CRM (`housing`)

A Kanban pipeline for tracking potential rentals through your search process.

- **Four-stage pipeline** — move properties through Found → Viewing Scheduled → Applied → Lease Signed.
- **Amenity logging** — record campus distance, transit access, rent price, and Wi-Fi capability per listing.

---

### Accounts — Auth & Profiles (`accounts`)

Secure user authentication with email verification.

- Registration with email confirmation (6-digit code, 15-minute expiry)
- Two-step email change flow with verification code
- Password change with active session preservation
- Profile photo upload and display name management

---

## Project Structure

```
.
├── accounts/       # Authentication, profiles, email verification
├── budget/         # Personal ledger and predictive runway engine
├── roomieratio/    # Shared expenses, debt simplification, chore rotation
├── housing/        # Apartment search Kanban pipeline
├── core/           # Settings and root URL configuration
└── templates/      # Shared HTML templates
```

---

## Tech Stack

- **Backend** — Django (Python 3.12)
- **Database** — SQLite (development)
- **Auth** — Django's built-in auth extended with email verification flows
- **Frontend** — Django templates with inline CSS; no JS framework

---

## Getting Started

```bash
git clone https://github.com/davlatbekzoirov/CampusCribs.git
cd CampusCribs

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Configure `DEFAULT_FROM_EMAIL` and your email backend in `core/settings.py` before using any verification flows.