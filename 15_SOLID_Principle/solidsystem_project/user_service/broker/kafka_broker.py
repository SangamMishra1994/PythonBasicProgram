from user_service.interfaces.message_broker import MessageBroker


class KafkaBroker(MessageBroker):
    def publish(self, message):
        print(f"[Kafka] Publishing: {message}")
