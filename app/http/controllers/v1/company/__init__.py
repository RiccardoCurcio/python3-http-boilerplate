create_schema = {
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


read_schema = {
    "headers": {},
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
        ]
    },
    "query": {},
    "body": {}
}


read_all_schema = {
    "headers": {},
    "params": {},
    "query": {},
    "body": {}
}

update_schema = {
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

delete_schema = {
    "headers": {},
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
    "body": {}
}
