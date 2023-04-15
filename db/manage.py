from pymongo import MongoClient
from pymongo.database import Database


class MongoManager:
    client: MongoClient = None
    db: Database = None

    def connect_to_database(self, path: str):
        print("Connecting to MongoDB.")
        self.client = MongoClient(path)
        self.db = self.client.main_db
        print("Connected to MongoDB.")

    def close_database_connection(self):
        print("Closing connection with MongoDB.")
        self.client.close()
        print("Closed connection with MongoDB.")

    def ping(self):
        try:
            self.client.admin.command("ping")
            return "Pinged your deployment. You successfully connected to MongoDB!"
        except Exception as e:
            return e

    def connect_to_collection(self):
        return self.db.users
