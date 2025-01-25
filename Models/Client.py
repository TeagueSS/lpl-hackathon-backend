from datetime import datetime

class Client:
    def __init__(self, name, dob, ethnicity, risk_tolerance, investment_keywords, investment_budget):
        # Here we have Demographic Information allowing us to make better
        # references as our model grows, we can also use this information for
        # Later insight.
        self.name = name
        self.dob = self._validate_dob(dob)
        self.ethnicity = self._validate_ethnicity(ethnicity)
        self.risk_tolerance = self._validate_risk_tolerance(risk_tolerance)
        self.investment_keywords = self._validate_keywords(investment_keywords)
        self.investment_budget = self._validate_budget(investment_budget)
    
    def _validate_dob(self, dob):
        try:
            return datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("DOB must be in the format YYYY-MM-DD.")

    def _validate_ethnicity(self, ethnicity):
        valid_ethnicities = {
            "Asian", "Black", "Hispanic", "White", "Native American", "Other"
        }
        if ethnicity not in valid_ethnicities:
            raise ValueError(f"Ethnicity must be one of {valid_ethnicities}.")
        return ethnicity

    def _validate_risk_tolerance(self, risk_tolerance):
        if not (0 <= risk_tolerance <= 5):
            raise ValueError("Risk tolerance must be between 0 and 5.")
        return risk_tolerance

    def _validate_keywords(self, keywords):
        predefined_keywords = {
            "Retirement", "Education", "Growth", "Income", "Sustainability", "Wealth Preservation"
        }
        if not all(keyword in predefined_keywords for keyword in keywords):
            raise ValueError(f"Keywords must be from the predefined set: {predefined_keywords}.")
        return keywords

    def _validate_budget(self, budget):
        if not isinstance(budget, (int, float)) or budget <= 0:
            raise ValueError("Investment budget must be a positive number.")
        return budget

    def to_dict(self):
        return {
            "name": self.name,
            "dob": self.dob.isoformat(),
            "ethnicity": self.ethnicity,
            "risk_tolerance": self.risk_tolerance,
            "investment_keywords": self.investment_keywords,
            "investment_budget": self.investment_budget
        }
