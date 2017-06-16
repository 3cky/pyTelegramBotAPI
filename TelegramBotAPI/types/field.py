

class Field(object):
    def __init__(self, *args, **kwargs):
        self.list = False
        self.types = []

        self.optional = kwargs.get('optional', False)
        self.ignore = kwargs.get('ignore', False)
        if self.ignore:
            self.optional = True
            return

        for arg in args:
            if isinstance(arg, list):
                self.list = True
                self.types = arg
                assert len(args) == 1  # Only allow a single type when using a list
                break
            self.types.append(arg)

    def __repr__(self):
        return '<Field(%s)>' % (', '.join([t.__name__ for t in self.types]))

    def setup_types(self):
        """
        The Message object has a circular reference on itself, thus we have to allow
        Type referencing by name. Here we lookup any Types referenced by name and
        replace with the real class.
        """
        def load(t):
            from TelegramBotAPI.types.type import Type
            if isinstance(t, str):
                return Type._type(t)
            if isinstance(t, list):
                assert all([issubclass(el, Type) for el in t])
            else:
                assert issubclass(t, Type)
            return t
        self.types = [load(t) for t in self.types]

    @property
    def leaf(self):
        for t in self.types:
            if len(t._valid_fields):
                return False
        return True
