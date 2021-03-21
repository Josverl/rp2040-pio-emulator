# Copyright 2021 Nathan Young
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest
from pioemu import emulate, State
from .support import emulate_single_instruction


def test_jump_always_forward():
    new_state = emulate_single_instruction(0x0007)  # jmp 7

    assert new_state.program_counter == 7


@pytest.mark.parametrize(
    "opcode, expected_clock_cycles",
    [pytest.param(0x0000, 1, id="jmp 0"), pytest.param(0x0102, 2, id="jmp 1 [1]"),],
)
def test_jump_consumes_expected_clock_cycles(opcode, expected_clock_cycles):
    new_state = emulate_single_instruction(opcode)

    assert new_state.clock == expected_clock_cycles
