from typing import Literal, Optional

from tukaan._tcl import Tcl
from tukaan._variables import Float

from ._base import BaseWidget, TkWidget


class ProgressBar(BaseWidget):
    _tcl_class = "ttk::progressbar"
    _keys = {
        "focusable": (bool, "takefocus"),
        "max": float,
        "mode": str,
        "orientation": (str, "orient"),
        "value": float,
        "variable": Float,
    }

    def __init__(
        self,
        parent: Optional[TkWidget] = None,
        max: Optional[int] = 100,
        *,
        focusable: Optional[bool] = None,
        mode: Optional[Literal["determinate", "indeterminate"]] = None,
        orientation: Optional[Literal["horizontal", "vertical"]] = None,
        value: Optional[int] = None,
        variable: Optional[Float] = None,
    ) -> None:
        BaseWidget.__init__(
            self,
            parent,
            maximum=max,
            mode=mode,
            orient=orientation,
            takefocus=focusable,
            value=value,
            variable=variable,
        )

    def _repr_details(self):
        return f"mode={self.mode!r}, max={self.max!r}, value={self.value!r}"

    def get(self) -> float:
        return self.value

    def set(self, value: float = 0) -> None:
        self.value = value

    def start(self, steps_per_second: int = 20) -> None:
        if steps_per_second > 1000:
            raise ValueError("error")
        interval = int(1000 / steps_per_second)
        Tcl.call(None, self, "start", interval)

    def stop(self) -> None:
        Tcl.call(None, self, "stop")

    def step(self, amount: int = 1) -> None:
        Tcl.call(None, self, "step", amount)

    def __add__(self, other: int):
        self.set(self.get() + other)
        return self

    def __sub__(self, other: int):
        self.set(self.get() - other)
        return self
