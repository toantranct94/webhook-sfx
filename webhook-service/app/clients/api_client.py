import requests


class APIClient:
    """
    A client for making API requests and forwarding events.
    """

    def forward_event(
        self,
        forward_url: str,
        event_data: dict
    ):
        """
        Forwards an event to the specified URL.

        Args:
            forward_url (str): The URL to forward the event to.
            event_data (dict): The data of the event to be forwarded.

        Returns:
            dict: The JSON response from the API.
        """
        response = requests.post(forward_url, json=event_data)
        response.raise_for_status()
        return response.json()
