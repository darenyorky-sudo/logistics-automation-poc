import json
import datetime

def generate_invoice_data(order_id):
    """
    Generates a structured invoice data object for the accounting system.
    """
    invoice = {
        "invoice_number": f"INV-{order_id}-{datetime.datetime.now().strftime('%Y%m%d')}",
        "order_id": order_id,
        "status": "READY_FOR_BILLING",
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # Save to a dummy file to simulate system output
    file_path = f"data/invoice_{order_id}.json"
    with open(file_path, "w") as f:
        json.dump(invoice, f, indent=4)
        
    return file_path