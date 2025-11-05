# MeetMatch Graduation Project
### Version: 1.0.0
----
# Objectives:
### MeetMatch is a B2C software application aims to colaborate in recruitment process using Ai dialog power for making a smart interview then making all desired evaluations and preferences.   

MeetMatch is an intelligent, LLM-based interview simulation platform designed for HR professionals and recruiters to streamline the hiring process. It automates candidate interviews using a virtual AI agent that interacts with applicants, evaluates their responses, detects cheating behaviors, and ranks candidates for final in-person interviews.

--------------------------------


 Key Features:
 
- AI Interview Agent**  
  Conducts domain-specific interview questions based on the candidate's CV and field of expertise.
- Smart Evaluation Engine**  
  Uses LLMs to evaluate candidate responses with a neutral, consistent scoring system.
- Anti-Cheating Monitoring**  
  Tracks behavior and session integrity using smart heuristics (e.g., time tracking, session integrity checks).
- Custom Question Banks**  
  Admins can build and manage question sets for each job domain.
- Secure One-Time Interview Links**  
  Unique links generated via JWT and APIs for each candidate — valid for one attempt only.
- HR Admin Dashboard**  
  Review full interviews, scoring breakdowns, and feedback justifications.
- Emotionally Aware Feedback**  
  The AI agent responds with empathetic and interactive commentary during the session.
  
----------------------------

Workflow Pipline: 
1. HR creates a job role and uploads or defines domain-specific questions.
2. Candidate receives a secure one-time link.
3. AI agent starts the interview session.
4. Candidate responds to each question vocally or textually.
5. AI provides real-time feedback and logs responses.
6. After the session ends, evaluation scores are computed.
7. HR accesses detailed insights and final recommendations.
   
-----------------------------

 Tech Stack

- Frontend: React.js / Next.js  
- Backend: Django / Django REST Framework  
- AI Engine: OpenAI GPT / Gemini + LangChain  
- Database: PostgreSQL  
- Authentication: JWT  
- Monitoring: MediaPipe / Custom Observers  
- Deployment: Docker + Cloud Hosting (e.g., Render, Vercel, or AWS)

  ---------------------------------------------------

### Team Members:
- Abdelrahman Eldgwy
- Abdlerhman Ashraf
- Ahmed Ali
- Abdelrahman Helal
- Menna Mohamed
- Fatima Abuelazaim 

