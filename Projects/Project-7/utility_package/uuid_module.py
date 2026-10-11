import uuid


def generate_uuid():
    unique_id = uuid.uuid4()
    print("Generated UUID:", unique_id)


def uuid_menu():
    print("\n==============================")
    print("Generate Unique Identifiers")
    print("==============================")

    generate_uuid()
