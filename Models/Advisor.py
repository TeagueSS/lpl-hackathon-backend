from datetime import datetime

# Here we have our Advisor Class ->
class Advisor:
    def __init__(self, name, dob, years_experience, profesionalSite, desired_equity, description , taking_on_clients):
        self.name = name
        self.dob = self._validate_dob(dob)
        self.years_experience = self._validate_experience(years_experience)
        # Here we can save a link to their personal site (Their portfolio or other
        # Information they might want to tag
        self.profesionalSite = profesionalSite
        # Here they can set the amount of equity they expect
        # And we are going to make sure it's a number as we don't want
        # To store a string of this ->
        self.desired_equity = self._validate_equity(desired_equity)
        # Here we want a short description about our people:
        self.description = description
        # We need to know if our people are taking on Clients
        self.taking_on_clients = taking_on_clients

    def _validate_dob(self, dob):
        try:
            return datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("DOB must be in the format YYYY-MM-DD.")

    def _validate_experience(self, years_experience):
        if not isinstance(years_experience, int) or years_experience < 0:
            raise ValueError("Years of experience must be a non-negative integer.")
        return years_experience

    def _validate_equity(self, equity):
        if not isinstance(equity, (int, float)) or equity < 0:
            raise ValueError("Desired equity must be a non-negative number.")
        return equity

    def to_dict(self):
        return {
            "name": self.name,
            "dob": self.dob.isoformat(),
            "years_experience": self.years_experience,
            "resume": self.profesionalSite,
            "desired_equity": self.desired_equity,
            "description": self.description
        }
