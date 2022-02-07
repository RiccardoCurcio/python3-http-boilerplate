create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "iban": {"type": ["string", "null"]},
        "email": {"type": ["string", "null"]}
    },
    "required": [
        "name",
        "iban",
        "email"
    ]
}

read_schema = {}

update_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "iban": {"type": ["string", "null"]},
        "email": {"type": ["string", "null"]}
    },
    "required": [
        "name"
    ]
}

delete_schema = {}
