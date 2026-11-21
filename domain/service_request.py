
from domain.exceptions import InvalidPriorityError


class ServiceRequest:

    ALLOWED_PRIORITIES = ["LOW", "MEDIUM", "HIGH"]

    def __init__(self, request_id, employee_name, issue, priority):

        priority = priority.strip().upper()

        if priority not in self.ALLOWED_PRIORITIES:
            raise InvalidPriorityError(
                "Priority must be LOW, MEDIUM or HIGH"
            )

        self.request_id = request_id.strip().upper()
        self.employee_name = employee_name.strip()
        self.issue = issue.strip()
        self.priority = priority
        self.status = "OPEN"

    def resolve(self):

        if self.status == "OPEN":
            self.status = "RESOLVED"
            return True

        return False

    def to_dict(self):

        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "issue": self.issue,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):

        request = cls(
            data["request_id"],
            data["employee_name"],
            data["issue"],
            data["priority"]
        )

        request.status = data.get("status", "OPEN")

        return request
