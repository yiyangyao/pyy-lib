def gt(attribute_value, condition_value):
    return attribute_value > condition_value


def ge(attribute_value, condition_value):
    return attribute_value >= condition_value


def lt(attribute_value, condition_value):
    return attribute_value < condition_value


def le(attribute_value, condition_value):
    return attribute_value <= condition_value


def in_list(attribute_value, condition_value):
    return attribute_value in condition_value


def ni_list(attribute_value, condition_value):
    return attribute_value not in condition_value


def is_null(attribute_value, condition_value):
    if attribute_value is None:
        return True
    return False


def not_null(attribute_value, condition_value):
    if attribute_value is not None:
        return True
    return False
