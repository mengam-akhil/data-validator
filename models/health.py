from datetime import datetime
from pydantic import BaseModel, field_validator


class BloodPressureObservation(BaseModel):
    patient_id: str
    systolic: int
    diastolic: int
    timestamp: datetime

    @field_validator("systolic", "diastolic")
    @classmethod
    def must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("blood pressure values must be positive numbers")
        return v

    @field_validator("diastolic")
    @classmethod
    def diastolic_lower_than_systolic(cls, v: int, info) -> int:
        systolic = info.data.get("systolic")
        if systolic is not None and v >= systolic:
            raise ValueError("diastolic pressure must be lower than systolic pressure")
        return v
