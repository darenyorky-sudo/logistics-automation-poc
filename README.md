# Logistics Automation Engine

A robust automation backend designed to streamline logistics workflows, specifically focusing on delivery validation and automated invoicing.

## Project Workflow
1. **Validation (`processor.py`):** Checks incoming delivery proofs (photos/signatures) for data integrity.
2. **Generation (`generator.py`):** Automatically creates invoice records upon successful validation.
3. **Monitoring:** Professional logging enabled for real-time debugging.

## Getting Started
To run the full flow:
```bash
python run_demo.py