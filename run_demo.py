from src.processor import validate_delivery

# Simulate incoming delivery data from a driver
delivery_payload = {
    "id": "LOG-555",
    "signature_present": True,
    "photo_url": "https://example.com/delivery_photo.jpg"
}

print("--- Logistics Automation Demo ---")

# Validate the delivery
result = validate_delivery(delivery_payload)
print(f"Processing Result: {result}")

# Trigger invoicing if validation succeeded
if result['status'] == 'success':
    print(f"✅ Action: Generating Invoice for Order {delivery_payload['id']}...")