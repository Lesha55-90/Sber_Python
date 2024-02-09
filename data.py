data = [
    {
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
        "to": "Счет ****************5907"
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
        "from": "Visa Classic 284287******9012",
        "to": "Счет ****************3655"
    },
  
    {
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
        "from": "Maestro 781084******5568",
        "to": "Счет ****************2869"
    },

    {
        "id": 482520625,
        "state": "EXECUTED",
        "date": "2019-11-13T17:38:04.800051",
        "operationAmount": {
            "amount": "62814.53",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет ****************9794",
        "to": "Счет ****************8125"
    },
    
    {
        "id": 801684332,
        "state": "EXECUTED",
        "date": "2019-11-05T12:04:13.781725",
        "operationAmount": {
            "amount": "21344.35",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет ****************8381"
    }
]

for item in data:
    print(f"{item['date']} {item['description']}\n")
    if 'from' in item:
        print(f"{item['from']} -> {item['to']}\n")
    else:
        print(f"-> {item['to']}\n")
    print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['code']}\n")
