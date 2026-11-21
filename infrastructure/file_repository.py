
import json
from pathlib import Path

from domain.service_request import ServiceRequest


class FileRepository:

    def __init__(self, file_path="data/requests.json"):

        self.file_path = Path(file_path)

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def _read_data(self):

        if not self.file_path.exists():
            return []

        content = self.file_path.read_text(
            encoding="utf-8"
        ).strip()

        if not content:
            return []

        try:
            data = json.loads(content)

            if not isinstance(data, list):
                raise ValueError("Invalid JSON data format.")

            return data

        except json.JSONDecodeError as error:
            raise ValueError(
                f"Unable to read JSON file: {error}"
            ) from error

    def get_all(self):

        data = self._read_data()

        return [
            ServiceRequest.from_dict(item)
            for item in data
        ]

    def get_by_id(self, request_id):

        for request in self.get_all():

            if request.request_id == request_id.strip().upper():
                return request

        return None

    def save(self, request):

        data = self._read_data()

        updated = False

        for index, item in enumerate(data):

            if item["request_id"] == request.request_id:

                data[index] = request.to_dict()
                updated = True
                break

        if not updated:
            data.append(request.to_dict())

        self.file_path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )
