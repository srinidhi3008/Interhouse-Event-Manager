# Interhouse-Event-Manager
This is a desktop application built with Python's `tkinter` GUI toolkit and a MySQL database. It serves as a simple management system for school inter-house events, providing two distinct user roles: one for regular students and one for admins (House Captains/Vice-Captains).
## Features
### General
* **Login System:** Secure login that directs users to the appropriate dashboard.
* **Signup Portal:** A two-step signup process to register new users and gather their information (name, class, house).
* **Role-Based Access:** The application provides a different set of tools based on whether the user is a regular student or an admin.
---
### Student Dashboard

* **View Events:** See a complete list of all available events, including eligible grades, prelims dates, and finals dates.
* **Search Events:** Search for specific events by name.
* **Register for Events:** Sign up for any event with a single click.
* **View/Withdraw Registrations:** View a list of all events you are currently registered for and withdraw your registration.

---

### Admin (Captain/Vice-Captain) Dashboard

Includes all features from the Student Dashboard, plus:

* **Add Events:** Add new events to the database, including name, eligible grades, and dates.
* **Update Events:** Modify the prelims and finals dates for existing events.
* **View House Registrations:** View a complete list of all students who have registered from your specific house.
* **Personal Registration:** Admins can also register and withdraw from events themselves
