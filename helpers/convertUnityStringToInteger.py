from config.unityTypes import types_category, unity_category, unity_status


def get_types_through_key(type):
    type.replace(" ", "")
    type.strip()
    return types_category[type]


def get_unity_category_through_key(type):
    type.replace(" ", "")
    type.strip()
    return unity_category[type]


def get_unity_status_through_key(type):
    type.replace(" ", "")
    type.strip()
    return unity_status[type]
