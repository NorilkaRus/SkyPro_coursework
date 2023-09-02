from src.utils import *

def test_display_operation():
    #Со счета на счет
    assert display_operation({
        "id": 888407131,
        "state": "EXECUTED",
        "date": "2019-09-29T14:25:28.588059",
        "operationAmount": {
            "amount": "45849.53",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 35421428450077339637",
        "to": "Счет 46723050671868944961"
    }) == '29.09.2019 Перевод со счета на счет\nСчет **9637 -> Счет **4961\n45849.53 USD\n'

    # С карты на карту
    assert display_operation({
    "id": 484201274,
    "state": "EXECUTED",
    "date": "2019-04-11T23:10:21.514616",
    "operationAmount": {
      "amount": "62621.51",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 8193813157568899",
    "to": "МИР 9425591958944146"
  }) == '11.04.2019 Перевод с карты на карту\nМИР 8193 81** **** 8899 -> МИР 9425 59** **** 4146\n62621.51 руб.\n'

    #С карты на счет
    assert display_operation({
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19T09:22:25.899614",
    "operationAmount": {
        "amount": "30153.72",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 7810846596785568",
    "to": "Счет 43241152692663622869"
  }) == '19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n'

    #На счет
    assert display_operation({
    "id": 108066781,
    "state": "EXECUTED",
    "date": "2019-06-21T12:34:06.351022",
    "operationAmount": {
      "amount": "25762.92",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90817634362091276762"
  }) == '21.06.2019 Открытие вклада\n -> Счет **6762\n25762.92 руб.\n'


def test_show_last_operatons():
    assert show_last_operatons(".\operations.json", 1) == [{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }]

    assert show_last_operatons(".\operations.json", 2) == [{
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655"
        }
    ]


def test_find_operation():
    assert find_operation("2019-02-14T17:38:09.910336", ".\operations.json") == {
    "id": 692008409,
    "state": "CANCELED",
    "date": "2019-02-14T17:38:09.910336",
    "operationAmount": {
      "amount": "37044.95",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 4610247282706784",
    "to": "Счет 63229171188548882700"
  }

    assert find_operation("2023-09-02T13:10:00.910336", ".\operations.json") == "None"