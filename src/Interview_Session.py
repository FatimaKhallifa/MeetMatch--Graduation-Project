from typing import List
from .Candidate_answer import CandidateAnswer
from datetime import datetime
class InterviewSession:
    def __init__(self, sessino_id: str):
        self.sessino_id = sessino_id
        self.start_time = None
        self.end_time = None
        self.answers : List[CandidateAnswer] = []
        
    def start_session(self):
        """Initialize session timing"""
        
        self.start_time = datetime.now()
        print("Session started at", self.start_time)
    
    
    def end_session(self):
        """Finalize session timing"""

        self.end_time = datetime.now()
        print("Session ended at", self.end_time)
    
    
    def record_answer(self, answer_text:CandidateAnswer):
        # Store candidate answer in a list
        self.answers.append(answer_text)
    
    def get_session_duration(self):
        """Calculate session duration"""
        
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0.0