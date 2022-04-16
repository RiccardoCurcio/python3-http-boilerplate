create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": ["string", "null"]},
        "vatNumber": {"type": ["string", "null"]},
        "phones": {
            "type": ["array"],
            "items": {"type": "string"}
        },
        "emails": {
            "type": ["array"],
            "items": {"type": "string"}
        }
    },
    "required": [
        "name",
        "vatNumber",
        "phones",
        "emails"
    ]
}

read_schema = {}

update_schema = {
    "type": "object",
    "properties": {
        "name": {"type": ["string", "null"]},
        "vatNumber": {"type": ["string", "null"]},
        "phones": {
            "type": ["array"],
            "items": {"type": "string"}
        },
        "emails": {
            "type": ["array"],
            "items": {"type": "string"}
        }
    },
    "required": [
        "name",
        "vatNumber",
        "phones",
        "emails"
    ]
}

delete_schema = {}
