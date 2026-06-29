import logging

# Configure logging for production monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_delivery(data):
    """
    Validates delivery data integrity.
    Ensures that signature and photo proof are present.
    """
    required_fields = ['id', 'signature_present', 'photo_url']
    
    logging.info(f"Processing order: {data.get('id', 'Unknown')}")
    
    # Check for missing data fields
    missing = [f for f in required_fields if f not in data]
    if missing:
        logging.error(f"Validation failed for order {data.get('id')}: missing {missing}")
        return {"status": "error", "message": f"Missing: {missing}"}
    
    # Check if delivery is fully confirmed
    if data['signature_present'] and data['photo_url']:
        logging.info(f"Order {data['id']} delivery confirmed.")
        return {"status": "success", "order_id": data['id']}
    
    logging.warning(f"Order {data['id']} data is incomplete.")
    return {"status": "incomplete"}