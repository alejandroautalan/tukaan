from __future__ import annotations

from typing import Optional

from ._base import BaseWidget, TkWidget
from ._helpers import convert_4side, convert_4side_back


class Frame(BaseWidget):
    _tcl_class = "ttk::frame"
    _keys = {}

    def __init__(
        self, parent: Optional[TkWidget] = None, padding: Optional[int | tuple[int, ...]] = None
    ) -> None:
        BaseWidget.__init__(self, parent, padding=convert_4side(padding))

    def _get(self, type_spec, key):
        if key == "padding":
            return self.padding
        else:
            return super()._get(type_spec, key)

    def _set(self, **kwargs):
        if "padding" in kwargs:
            self.padding = kwargs.pop("padding", (0,) * 4)

        super()._set(**kwargs)

    @property
    def padding(self):
        return convert_4side_back(tuple(map(int, self._tcl_call((str,), self, "cget", "-padding"))))

    @padding.setter
    def padding(self, new_padding):
        self._tcl_call(None, self, "configure", "-padding", convert_4side(new_padding))
