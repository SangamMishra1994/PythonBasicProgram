# main.py
import sys
import os

# Ensure project root path is added
sys.path.append(os.path.dirname(__file__))

# ---------------- USER SERVICE IMPORTS ----------------
from user_service.models.users import User
from user_service.repositories.postgre_user_repo import PostgresUserRepository
from user_service.broker.kafka_broker import KafkaBroker
from user_service.services.user_registeration_service import UserRegistrationService


if __name__ == "__main__":

    print("\n===============================")
    print("✅ USER REGISTRATION MICROSERVICE RUNNING")
    print("===============================\n")

    user = User(1, "Sangam", "sangam@example.com")

    repo = PostgresUserRepository()
    broker = KafkaBroker()

    user_service = UserRegistrationService(repo, broker)
    user_service.register(user)

    print("\n===============================")
    print("✅ E‑COMMERCE ORDER SYSTEM RUNNING")
    print("===============================\n")

    # # order = Order(items=["Shoes", "Bag"], total_amount=2000)

    # # payment = StripePayment()
    # # discount_service = DiscountService()

    # # order_service = OrderService(payment, discount_service)
    # # order_service.place_order(order)

    # print("\n✅ All services executed successfully!\n")
