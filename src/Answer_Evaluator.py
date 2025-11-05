from .GPT_API import GeminiClient
from .Question_Manager import Question
import re
import json

class AnswerEvaluator:
    def __init__(self):
        self.model = GeminiClient()
        self._eval_template = """you are a technical model answer and evaluate the my answer based on the following parameters:

Question: {question_text}
Answer: {answer_text}
Best Answer for best evaluation score: {best_answer_text}

Key Performance Indicators need to measure (KPIs):
{kpis}

Provide scores (0-10) and very brief feedback for each KPI in KPIs list based on best_answer_text similarity, Output only the following JSON structure without any additional text or explanations:

{{
    "question_id": "{question_id}",
    "evaluations": [
        {{
            "kpi": "KPI_NAME_1",
            "score": 0-10,
            "feedback": "constructive feedback here"
        }},
        {{
            "kpi": "KPI_NAME_2",
            "score": 0-10,
            "feedback": "constructive feedback here"
        }},
        {{
            "kpi": "KPI_NAME_3",
            "score": 0-10,
            "feedback": "constructive feedback here"
        }}
    ],
    "Opinion": "constructive an exclamatory overall sentence here"
    
}}
"""
        
    def _generate_evaluation_prompt(self, answer: str, question: str, satsfied_answer: str, ques_kpis: list[str],question_id:str) -> str:
        eval_prompt = self._eval_template.format(
                                                question_text = question,
                                                answer_text = answer,
                                                best_answer_text = satsfied_answer,
                                                kpis = "\n".join(ques_kpis),
                                                question_id = question_id
                                                )
        return eval_prompt

    def evaluate_answer(self,question:Question, answer)->dict:
        question_id = question.id
        question_text = question.text
        satsfied_answer = question.answer
        kpis = question.related_kpis
        
        try:
            prompt = self._generate_evaluation_prompt(answer, question_text, satsfied_answer,kpis,question_id)
            raw_response = self._call_gemini_api(prompt)

            # return self._parse_evaluation_result(raw_response, question)
            return {"response": raw_response}
            
        except Exception as e:
            return {"error": str(e)}
        
    def _call_gemini_api(self, prompt: str) -> str:
        return self.model.get_response(prompt)   

    def _parse_evaluation_result(self, raw_response: str, question: str) -> dict:
        """Convert Gemini response to structured data"""
        try:
            # Clean and validate response
            cleaned = re.sub(r'[\s\S]*?({.*})', r'\1', raw_response, flags=re.DOTALL)
            result = json.loads(cleaned)
            
            # Validate structure against expected KPIs
            expected_kpis = set(question.get_related_kpis())
            received_kpis = set(e["kpi"] for e in result["evaluation"])
            
            if not expected_kpis.issubset(received_kpis):
                missing = expected_kpis - received_kpis
                raise ValueError(f"Missing KPI evaluations: {', '.join(missing)}")
            
            return result
        except (json.JSONDecodeError, KeyError) as e:
            return {"error": f"Failed to parse evaluation: {str(e)}"}

