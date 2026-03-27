from user_service.interfaces.message_broker import MessageBroker


class RabbitMQBroker(MessageBroker):
    def publish(self, message):
        print(f"[RabbitMQ] Publishing: {message}")
