from Database.mongo_repository import MongoRepository

class ClientService:
    def __init__(self):
        self.db = MongoRepository('clients')  # Initialize repository for 'clients' collection

    def add_client(self, data):
        client_id = self.db.insert(data)
        return client_id

    def get_client(self, client_id):
        return self.db.find_by_id(client_id)
