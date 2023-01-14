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
    "params": {},
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