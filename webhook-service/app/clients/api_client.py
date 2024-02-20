import requests


class APIClient:

    def forward_event(
        self,
        forward_url: str,
        event_data: dict
    ):
        response = requests.post(forward_url, json=event_data)
        response.raise_for_status()
        return response.json()
