from . import matcher


class OperationTypes(object):
    GREATER_THAN = '>'
    GREATER_THAN_OR_EQUAL = '>='
    LESS_THAN = '<'
    LESS_THAN_OR_EQUAL = '<='
    IN = 'in'
    NOT_IN = 'ni'
    IS_NULL = 'is_null'
    IS_NOT_NULL = 'is_not_null'

    DEFAULT = 'default'

    @staticmethod
    def match_func(op):
        switcher = {
            OperationTypes.GREATER_THAN: matcher.gt,
            OperationTypes.GREATER_THAN_OR_EQUAL: matcher.ge,
            OperationTypes.LESS_THAN: matcher.lt,
            OperationTypes.LESS_THAN_OR_EQUAL: matcher.le,
            OperationTypes.IN: matcher.in_list,
            OperationTypes.NOT_IN: matcher.ni_list,
            OperationTypes.IS_NULL: matcher.is_null,
            OperationTypes.IS_NOT_NULL: matcher.not_null,
            OperationTypes.DEFAULT: lambda: None,
        }

        return switcher.get(op, 'default')
