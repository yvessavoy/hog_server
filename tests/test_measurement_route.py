def test_temperature_ok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "temperature",
                "value": 24.15,
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 200


def test_temperature_nok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "temperature",
                "value": "foobar",
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 400


def test_humidity_ok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "humidity",
                "value": 39.55,
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 200


def test_humidity_nok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "humidity",
                "value": "foobar",
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 400


def test_light_ok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "light",
                "value": 576,
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 200


def test_light_nok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "light",
                "value": "foobar",
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 400


def test_co2_ok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "co2",
                "value": 245,
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 200


def test_co2_nok(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "co2",
                "value": "foobar",
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 400


def test_invalid_type(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "foobar",
                "value": 33.96,
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 400


def test_no_type(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "value": 33.96,
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 400


def test_no_value(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "foobar",
                "tech_device_name": "Testing-Client",
            },
        )

        assert response.status_code == 400


def test_no_device_name(app, client):
    with app.app_context():
        response = client.post(
            "/measurements",
            data={
                "type": "foobar",
                "value": 33.96,
            },
        )

        assert response.status_code == 400