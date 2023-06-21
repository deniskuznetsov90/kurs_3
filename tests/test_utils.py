from utils import load_data, executed_operations, \
    last_operations, account_mask, card_mask, date


def test_load_data():
    from_file = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]

    assert load_data('test_operations.json') == from_file


def test_executed_operations():
    assert executed_operations([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]


def test_last_operations():
    assert last_operations([{"date": "2018-09-12T21:27:25.241689"}]) == [{"date": "2018-09-12T21:27:25.241689"}]


def test_account_mask():
    assert account_mask('Счет 90424923579946435907') == "Счет ** 5907"


def test_card_mask():
    assert card_mask("Visa Classic 2842878893689012") == "Visa Classic 2842 87** ****9012"
    assert card_mask("Maestro 7810846596785568") == "Maestro 7810 84** ****5568"


def test_date():
    assert date('2019-12-08T22:46:21.935582') == "08.12.2019"
