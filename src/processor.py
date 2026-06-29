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
    import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_delivery(data):
    required_fields = ['id', 'signature_present', 'photo_url']
    
    # Логируем начало процесса
    logging.info(f"Processing order: {data.get('id', 'Unknown')}")
    
    # Проверка на наличие полей с логгированием ошибок
    missing = [f for f in required_fields if f not in data]
    if missing:
        logging.error(f"Validation failed for order {data.get('id')}: missing {missing}")
        return {"status": "error", "message": f"Missing: {missing}"}
    
    # Логика подтверждения
    if data['signature_present'] and data['photo_url']:
        logging.info(f"Order {data['id']} delivery confirmed.")
        return {"status": "success", "order_id": data['id']}
    
    logging.warning(f"Order {data['id']} is incomplete.")
    return {"status": "incomplete"}