# Mouspike-early-access-backend
# Live Demo / Connected Front-end
- **Health check endpoint:** https://mouspike-early-access-backend.onrender.com/health
- **Front-end prototype (Repo 1):** https://karis2021.github.io/Mouspike-coming-soon-frontend/
- **Official coming soon page (.uk):** https://mouspike.co.uk/
- **Alternative domain (.us):** https://mouspike.us/

(*This backend is connected to the front-end prototype through JavaScript requests.*)

# Project Overview
This repository contains the backend system I created to support the “Coming Soon” page of my personal brand project, Mouspike. At the time, the landing page already existed, but it was completely static and did not store or process any real data. I decided to build this backend as a way to learn how things actually work behind a web page and to move beyond only working on the front-end. 

This project was created before my official website was publicly launched on Shopify. It works as a technical prototype that allowed me to understand how a front-end connects to a backend, how data can be received and stored, and how a system becomes functional instead of just visual. The main focus was learning and practice, not building a final production system.

# Purpose
The main idea behind this repository was to turn my static “Coming Soon” page into something that actually worked. Before this, the page only existed visually and did not collect or process any real information. I wanted to practice how a front-end can connect to a backend and how data is handled once a user interacts with a page.

I created this backend as a learning step to understand how APIs work in a real situation, how emails can be received and stored, and how a backend becomes public once it is deployed. I separated the project into two repositories because I originally built the front-end first, without knowing how to create a backend. This repository was created later as a way to learn how the full system works together and how different parts of a web project communicate with each other.

# Tech Stack
* Python
* FastAPI
* SQLite
* Resend (testing mode)
* Render
* JavaScript (fetch API)

# System Architecture
When a user enters their email in the “Early Access” section and submits it, the front-end sends that information to the backend. The backend receives the email, checks it, and makes sure it follows basic rules, such as being written in lowercase and not being repeated. If the email is valid and new, it is stored in a database.

At the same time, the system sends a notification email to my personal email so I can see that someone registered. After that, the backend sends a response back to the front-end, which then shows a simple message to the user, such as confirming that they are registered or that the email already exists. This process helped me understand how information moves between the front-end and backend and how both sides depend on each other to work properly.

# Project Structure
- [app.py](app.py) – Main backend application and API routes
- [database.py](database.py) – Database logic and email storage 
- [email_service.py](email_service.py) – Email notification logic
- [signup.db](signup.db) – Database storing registered emails
- [requirements.txt](requirements.txt) – Project dependencies

# Current Status
The backend is currently deployed and working as intended. It can receive emails from the front-end, check for duplicates, and store the information in a database. It also sends notification emails to the admin address whenever someone registers through the form.

At this stage, the system is running in testing mode. Emails are not sent back to users yet, only to the admin, which was enough for learning and testing how the system behaves with real input.

# My Role and Learning
This project was fully built and tested by me. Since this was my first time creating a backend like this, the hardest part was dealing with real errors instead of just writing code. I had to change parts of the structure multiple times, fix database mistakes, solve deployment issues, and adapt when some tools or services did not work as expected. Through this process, I learned that backend development is not only about programming, but also about debugging, testing, and understanding why things fail. It taught me patience and helped me understand how real systems behave outside of tutorials.

# Limitations and Technical Decisions
This project was fully built and tested by me. Since this was my first time creating a backend like this, the hardest part was dealing with real errors instead of just writing code. I had to change parts of the structure multiple times, fix database mistakes, solve deployment issues, and adapt when some tools or services did not work as expected.

Through this process, I learned that backend development is not only about programming, but also about debugging, testing, and understanding why things fail. It taught me patience and helped me understand how real systems behave outside of tutorials.

# Possible Improvements
Originally, I wanted the system to send a confirmation email directly to users when they registered. However, this required a verified domain, which I did not have at the time I built this prototype. To stay true to the moment when the project was created, I decided to keep the system in testing mode.

Instead of sending emails to users, the backend sends notifications only to the admin email. This still shows that the system can process data and trigger automatic actions. This was a conscious decision based on real limitations, not because the feature was forgotten.

# Functional Evidence
To demonstrate that the backend works in a real environment, this repository includes the following evidence collected during testing:

- [EmailNotification:](/assets/images/email-notifications.png)   Screenshots of notification emails received when a user submits the early access form.  
- [DataBase-SQLITE:](/assets/images/database-sqlite.png)   Screenshot of the SQLite database showing stored email entries, confirming data persistence.  
- [LiveBackend:](/assets/images/live-backend.png)   Screenshot of the backend running live and responding correctly through the public URL.  
- [Render:](/assets/images/render.png) Screenshot of the service running and successfully deployed on Render. 
