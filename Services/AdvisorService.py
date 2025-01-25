from Database.mongo_repository import MongoRepository

class AdvisorService:
    # Initialize repository for 'advisors' collection
    def __init__(self):
        self.db = MongoRepository('advisors')
    # Here we can add an instance of an advisor
    def add_advisor(self, data):
        advisor_id = self.db.insert(data)
        # We need to return our Advisor ID as this is how
        # We can search for them later on ->
        return advisor_id

    def get_advisor(self, advisor_id):
        # Here we can return our Advisor by their ID from the Database
        return self.db.find_by_id(advisor_id)
