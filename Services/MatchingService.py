from Database.mongo_repository import MongoRepository

class MatchingService:
    def __init__(self):
        self.client_db = MongoRepository('clients')
        self.advisor_db = MongoRepository('advisors')

    def find_matching_advisor(self, client_id, email):
        client = self.client_db.find_by_id(client_id)
        if not client or client['email'] != email:
            return {"error": "Client not found or email mismatch"}

        # Simple matching logic
        matches = self.advisor_db.find({"risk_tolerance": client['risk_tolerance']})
        return matches
        #TODO We need to add a way to return our top 5 matches ->

