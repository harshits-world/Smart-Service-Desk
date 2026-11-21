
from application.request_service import RequestService
from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError,
    InvalidPriorityError
)
from infrastructure.file_repository import FileRepository


def display_request(request):

    print("\nRequest Details")
    print("-------------------------")
    print("Request ID:", request.request_id)
    print("Employee Name:", request.employee_name)
    print("Issue:", request.issue)
    print("Priority:", request.priority)
    print("Status:", request.status)


def main():

    repository = FileRepository()
    service = RequestService(repository)

    while True:

        print("\n========== SMART SERVICE DESK SYSTEM ==========")
        print("1. Create Service Request")
        print("2. View All Requests")
        print("3. Search Request")
        print("4. Resolve Request")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if not choice:
            print("\nInput cannot be empty.")
            continue

        try:

            if choice == "1":

                request_id = input("Enter Request ID: ")
                employee_name = input("Enter Employee Name: ")
                issue = input("Enter Issue: ")
                priority = input("Enter Priority (LOW/MEDIUM/HIGH): ")

                request = service.create_request(
                    request_id,
                    employee_name,
                    issue,
                    priority
                )

                print("\nService Request created successfully.")

            elif choice == "2":

                requests = service.view_requests()

                if not requests:
                    print("\nNo service requests found.")

                else:
                    print("\nID | Employee | Issue | Priority | Status")
                    print("-" * 70)

                    for request in requests:
                        print(
                            f"{request.request_id} | "
                            f"{request.employee_name} | "
                            f"{request.issue} | "
                            f"{request.priority} | "
                            f"{request.status}"
                        )

            elif choice == "3":

                request_id = input("Enter Request ID: ")

                request = service.search_request(request_id)

                display_request(request)

            elif choice == "4":

                request_id = input("Enter Request ID: ")

                result = service.resolve_request(request_id)

                if result:
                    print("\nRequest resolved successfully.")

                else:
                    print("\nRequest is already RESOLVED.")

            elif choice == "5":

                print("\nThank you for using Smart Service Desk.")
                break

            else:

                print("\nInvalid choice. Please enter 1 to 5.")

        except DuplicateRequestError as error:
            print("\nError:", error)

        except RequestNotFoundError as error:
            print("\nError:", error)

        except InvalidPriorityError as error:
            print("\nError:", error)

        except ValueError as error:
            print("\nError:", error)


if __name__ == "__main__":
    main()
