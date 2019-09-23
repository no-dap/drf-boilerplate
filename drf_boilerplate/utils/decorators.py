def paginate(pagination_class=None, **kwargs):
    """
    Decorator that adds a pagination_class to GenericViewSet class.
    """
    assert pagination_class is not None, (
        "@paginate missing required argument: 'pagination_class'"
    )

    class _Pagination(pagination_class):
        def __init__(self):
            self.__dict__.update(kwargs)
            super(_Pagination, self).__init__()

    def decorator(_class):
        _class.pagination_class = _Pagination
        return _class

    return decorator
