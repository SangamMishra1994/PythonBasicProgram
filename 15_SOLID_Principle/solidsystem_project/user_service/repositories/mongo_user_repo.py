from user_service.interfaces.user_repository import UserRepository


class MongoUserRepository(UserRepository):
    def save(self, user):
        print(f"[MongoDB] Saving user {user.name}")

    def find(self, user_id):
        print("[MongoDB] Fetching user")
        return {"id": user_id, "name": "Demo"}
