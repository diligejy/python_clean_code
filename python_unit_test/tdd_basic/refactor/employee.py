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
    hours_worked: float = 0.0
    # employee_cost: float = 1000.0
    employee_office_cost: float = 200.0
    employee_401k_cost: float = 400.0
    employee_support_cost: float = 400.0
    has_commission: bool = True
    commission: float = 100.0
    contracts_landed: int = 0

    def compute_payout(self) -> float:
        """Compute how much the employee should be paid."""
        employee_cost = (
            self.employee_office_cost
            + self.employee_401k_cost
            + self.employee_support_cost
        )
        payout = self.pay_rate * self.hours_worked + employee_cost
        if self.has_commission:
            payout += self.commission * self.contracts_landed
        return payout
