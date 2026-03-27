class UserRegistrationService:
    def __init__(self, repository, broker):
        self.repository = repository  # DIP
        self.broker = broker  # DIP

    def register(self, user):
        self.repository.save(user)
        self.broker.publish(f"User {user.name} registered successfully")
