from .Interview_Session import InterviewSession
from .KPI_Manager import KPIManager
from .GPT_API import GPTAPIClient
from datetime import datetime
class ReportGenerator:
    def __init__(self, template_path: str = "templates/"):
        self.template_path = template_path
        self.gpt_client = GPTAPIClient()
        
    def generate_summary_report(self, session: InterviewSession, kpi_scores: dict):
        base_data = {
        "session_id": session.session_id,
        "duration": session.get_session_duration(),
        "question_count": len(session.answers),
        "kpi_overview": kpi_scores
            }
        
        # Generate natural language insights using GPT
        prompt = f"Create executive summary report for the interview session: {base_data}"
        narrative = self.gpt_client.get_response(prompt)
        
        # Apply template to generate final report
        return self._apply_template("summary_template.html", {
            "meta": base_data,
            "narrative": narrative
        })
        
    def generate_detailed_report(self, kpi_manager: KPIManager):
        # Generate KPI data
        kpi_data = []
        for kpi in kpi_manager.kpis:
            kpi_data.append({
                "name": kpi.name,
                "weight": kpi.weight,
                "score": kpi.calculate_score(),
                "progress": kpi_manager.track_kpi_progress(kpi.name)
            })
        
        return self._apply_template("kpi_template.html", {
            "kpis": kpi_data,
            "weights": kpi_manager.kpi_weights
        })
    
    def save_report(self, report: str, format: str = "json"):
        filename = f"reports/report_{datetime.now().strftime('%Y%m%d%H%M%S')}.{format}"
        
        if format == "pdf":
            self._generate_pdf(report, filename)
        elif format == "json":
            self._save_json(report, filename)
        else:
            raise ValueError(f"Unsupported report format: {format}")
        
    # Private helper methods
    def _apply_template(self, template_path: str, context: dict) -> str:
        from jinja2 import Environment, FileSystemLoader
        
        self.template_path = template_path
        self.env = Environment(loader=FileSystemLoader(template_path))
        
        # Renders a template with the provided context data.
        """
        Args:
            template_name (str): Name of the template file (e.g., "summary_template.html").
            context (dict): Data to inject into the template.
        Returns:
            str: Rendered template as a string.
        """
        try:
            template = self.env.get_template(template_path)
            return template.render(context)
        except Exception as e:
            raise RuntimeError(f"Template rendering failed: {e}")

    def _generate_pdf(self, content: str, filename: str):
        # Generates a PDF file from HTML content.
        import os
        from weasyprint import HTML
        """
        Args:
            content (str): HTML content to convert to PDF.
            filename (str): Path to save the PDF file.
        """
        try:
            # Ensure the reports directory exists
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            # Generate PDF from HTML
            HTML(string=content).write_pdf(filename)
        except Exception as e:
            raise RuntimeError(f"PDF generation failed: {e}")
    
    def _save_json(self, content: str, filename: str):
        import json
        import os
        
        try:
            # Ensure the reports directory exists
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            
            # Save content as JSON
            with open(filename, "w") as json_file:
                json.dump(json.loads(content), json_file, indent=4)
        except Exception as e:
            raise RuntimeError(f"JSON file save failed: {e}")