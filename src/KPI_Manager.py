from .KPI import KPI
from typing import List, Dict

class KPIManager:
    def __init__(self, kpis: List[KPI], kpi_weights: Dict[str, float]):
        self.kpis = kpis
        self.kpi_weights = kpi_weights
        self.current_scores = {}
        self.historical_data = []

    def calculate_kpi_scores(self, evaluation_result: dict) -> dict:
        """Calculate weighted scores for all KPIs"""
        self.current_scores = {}
        for kpi in self.kpis:
            # Inject evaluation data into KPI instance
            kpi.evaluation_data = evaluation_result  
            
            # Calculate base score and apply weight
            base_score = kpi.calculate_score()
            weighted_score = base_score * self.kpi_weights.get(kpi.name, 1.0)
            
            self.current_scores[kpi.name] = {
                "base_score": base_score,
                "weighted_score": weighted_score,
                "weight": self.kpi_weights[kpi.name]
            }
        
        self.historical_data.append(self.current_scores)
        return self.current_scores

    def get_final_scores(self) -> dict:
        """Get final weighted scores aggregated by category"""
        return {
            kpi.name: data["weighted_score"]
            for kpi, data in zip(self.kpis, self.current_scores.values())
        }

    def track_kpi_progress(self, kpi_name: str) -> float:
        """Calculate progress percentage for a specific KPI"""
        if not self.current_scores:
            return 0.0
            
        target = 100  # Default target score
        current = self.current_scores.get(kpi_name, {}).get("base_score", 0)
        return min(current / target, 1.0)  # Cap at 100% progress