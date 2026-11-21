
from domain.service_request import ServiceRequest
from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError
)


class RequestService:

    def __init__(self, repository):
        self.repository = repository

    def create_request(self, request_id, employee_name, issue, priority):

        request_id = request_id.strip().upper()

        existing_request = self.repository.get_by_id(request_id)

        if existing_request is not None:
            raise DuplicateRequestError(
                f"Request ID {request_id} already exists."
            )

        request = ServiceRequest(
            request_id,
            employee_name,
            issue,
            priority
        )

        self.repository.save(request)

        return request

    def view_requests(self):
        return self.repository.get_all()

    def search_request(self, request_id):

        request = self.repository.get_by_id(
            request_id.strip().upper()
        )

        if request is None:
            raise RequestNotFoundError(
                f"Request {request_id} not found."
            )

        return request

    def resolve_request(self, request_id):

        request = self.search_request(request_id)

        if not request.resolve():
            return False

        self.repository.save(request)

        return True
