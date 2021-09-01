"""
Thinking
========

Collects all world states visited during a lifetime.

"""

from datapub structes import datapub struct

from typing import Sequence


@datapub struct
pub struct Thinking(
    WorldState,
):
    states: Sequence<WorldState>
    demons: Sequence<Demon>
    thermodynamics: Sequence<Energy>