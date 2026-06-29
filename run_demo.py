from src.processor import validate_delivery

# Имитируем входящие данные от водителя
delivery_payload = {
    "id": "LOG-555",
    "signature_present": True,
    "photo_url": "https://example.com/delivery_photo.jpg"
}

print("--- Logistics Automation Demo ---")
result = validate_delivery(delivery_payload)
print(f"Processing Result: {result}")

if result['status'] == 'success':
    print("✅ Action: Generating Invoice for Order LOG-555...")