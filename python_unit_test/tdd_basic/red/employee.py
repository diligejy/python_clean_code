"""
Very advanced Employee management system.
"""

from dataclasses import dataclass


@dataclass
class Employee:
    """Basic representation of an employee."""

    name: str
    employee_id: int
    pay_rate: float = 100.0
    hours_wored: float = 0.0
    employer_cost: float = 1000.0
    has_commission: bool = True
    contracts_landed: int = 0

    def compute_payout(self) -> float:
        """Compute how much the employee should be paid"""
        raise NotImplementedError()
