schema = {
    "headers": {
        "type": "object",
        "properties": {
            "Content-Type": {
                "type": ["string"],
                "enum": ["application/json"]
            }
        },
        "required": [
            "Content-Type"
        ]
    },
    "params": {
        "type": "object",
        "properties": {
            "entity_id": {
                "type": ["string"],
                "minLength": 2
            }
        },
        "required": [
            "entity_id"
        ]},
    "query": {},
    "body": {
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
}