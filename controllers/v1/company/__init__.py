create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "vatNumber": {"type": ["string", "null"]},
        "sdi": {"type": ["string", "null"]},
        "iban": {"type": ["string", "null"]},
        "registrationNumber": {"type": ["string", "null"]},
        "email": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "countryCode": {"type": ["string", "null"]},
        "area": {"type": ["string", "null"]},
        "state": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "streetAddress": {"type": ["string", "null"]},
        "postalCode": {"type": ["string", "null"]},
        "website": {"type": ["string", "null"]},
        "logo": {"type": ["string", "null"]}
    },
    "required": [
        "name",
        "vatNumber",
        "sdi",
        "iban",
        "registrationNumber",
        "email"
    ]
}

read_schema = {}

update_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "vatNumber": {"type": ["string", "null"]},
        "sdi": {"type": ["string", "null"]},
        "iban": {"type": ["string", "null"]},
        "registrationNumber": {"type": ["string", "null"]},
        "email": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"]},
        "countryCode": {"type": ["string", "null"]},
        "area": {"type": ["string", "null"]},
        "state": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "streetAddress": {"type": ["string", "null"]},
        "postalCode": {"type": ["string", "null"]},
        "website": {"type": ["string", "null"]},
        "logo": {"type": ["string", "null"]}
    },
    "required": [
        "name"
    ]
}

delete_schema = {}
