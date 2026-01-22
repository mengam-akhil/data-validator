from pydantic import ValidationError
from models.fintech import Transaction
from models.health import BloodPressureObservation

print("\n=== FinTech: Testing Invalid Input ===")
try:
    # This input is WRONG (ID too short, amount negative, currency unsupported)
    tx = Transaction(
        transaction_id="TX1",
        amount=-100,
        currency="INR"
    )
except ValidationError as e:
    print("✅ Clean Error Output:")
    for err in e.errors():
        # Clean field name + message
        print(f"   Field: {err['loc'][0]} -> {err['msg']}")

print("\n=== HealthTech: Testing Invalid Input ===")
try:
    # This input is WRONG (Diastolic higher than Systolic)
    bp = BloodPressureObservation(
        patient_id="P1",
        systolic=110,
        diastolic=120,
        timestamp="2026-01-20T10:00:00"
    )
except ValidationError as e:
    print("✅ Clean Error Output:")
    for err in e.errors():
        print(f"   Field: {err['loc'][0]} -> {err['msg']}")
