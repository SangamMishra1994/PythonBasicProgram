from user_service.interfaces.user_repository import UserRepository


class PostgresUserRepository(UserRepository):
    def save(self, user):
        print(f"[Postgres] Saving user {user.name}")

    def find(self, user_id):
        print("[Postgres] Fetching user")
        return {"id": user_id, "name": "Demo"}
