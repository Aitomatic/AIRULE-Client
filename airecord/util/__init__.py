from uuid import UUID, uuid4


class WithUUIDMixIn:
    @property
    def uuid(self) -> UUID:
        if not hasattr(self, '_uuid'):
            self._uuid = uuid4()

        return self._uuid
