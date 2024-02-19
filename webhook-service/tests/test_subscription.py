from flask import url_for

URL = 'http://example.com/webhook-endpoint'
EVENT_TYPE = 'my_event'


def test_upsert_subscription_201(test_client):
    data = {
        "url": URL,
        "event_type": EVENT_TYPE,
        "custom_headers": {
            "Authorization": "Bearer token",
            "Content-Type": "application/json"
        },
        "custom_payload": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    res = test_client.post(url_for('webhook.upsert_subscription'), json=data)

    assert res.status_code == 201


def test_delete_subscription_200(test_client):
    url = URL.replace('/', '~')
    res = test_client.delete(
        url_for('webhook.delete_subscription', url=url, event_type=EVENT_TYPE))

    assert res.status_code == 200
