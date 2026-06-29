import json

def validate_delivery(data):
    """
    Проверяет, содержит ли объект доставки все необходимые данные.
    """
    required_fields = ['id', 'signature_present', 'photo_url']
    
    # Проверка на наличие всех ключей
    if not all(field in data for field in required_fields):
        return {"status": "error", "message": "Missing required fields"}
    
    # Логика подтверждения
    if data['signature_present'] and data['photo_url']:
        return {"status": "success", "order_id": data['id'], "action": "trigger_invoice"}
    
    return {"status": "incomplete", "order_id": data['id']}

# Тестовый вызов (чтобы ты видел, как это работает)
if __name__ == "__main__":
    sample_delivery = {"id": "LOG-101", "signature_present": True, "photo_url": "http://link.to/photo"}
    print(validate_delivery(sample_delivery))