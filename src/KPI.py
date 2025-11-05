class KPI:
    def __init__(self, name: str, description: str, weight: float=1.0):
        self.name = name
        self.description = description
        self.weight = weight
        self.evaluation_data = None  # Set by KPIManager during evaluation

    def calculate_score(self) -> float:
        """Calculate score based on evaluation data and KPI-specific logic"""
        if not self.evaluation_data:
            return 0.0
        
        # Example calculation: Sum scores for this KPI from evaluation data
        return sum(
            result["score"] 
            for result in self.evaluation_data.get("metrics", [])
            if result["kpi"] == self.name
        ) 
