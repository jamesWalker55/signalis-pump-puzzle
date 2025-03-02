import enum
from typing import NamedTuple, Self


class PumpAction(enum.StrEnum):
    AB = enum.auto()
    AC = enum.auto()
    BA = enum.auto()
    BC = enum.auto()
    CA = enum.auto()
    CB = enum.auto()


class PumpActionIsNoop(Exception):
    pass


class PumpState(NamedTuple):
    a: int
    b: int
    c: int

    MAX_A = 12
    MAX_B = 8
    MAX_C = 5

    def is_valid_state(self):
        return (
            0 <= self.a <= 12
            and 0 <= self.b <= 8
            and 0 <= self.c <= 5
            and (self.a + self.b + self.c) == 12
        )

    @classmethod
    def initial_state(cls):
        return cls(12, 0, 0)

    def is_final_state(self):
        return self.a == 6 and self.b == 6 and self.c == 0

    def pump(self, action: PumpAction):
        cls = type(self)

        new_a = self.a
        new_b = self.b
        new_c = self.c

        if action is PumpAction.AB:
            if self.a == 0:
                raise PumpActionIsNoop()
            if self.b == self.MAX_B:
                raise PumpActionIsNoop()

            available_space = self.MAX_B - self.b
            to_move = min(available_space, self.a)
            new_a = self.a - to_move
            new_b = self.b + to_move
        elif action is PumpAction.AC:
            if self.a == 0:
                raise PumpActionIsNoop()
            if self.c == self.MAX_C:
                raise PumpActionIsNoop()

            available_space = self.MAX_C - self.c
            to_move = min(available_space, self.a)
            new_a = self.a - to_move
            new_c = self.c + to_move
        elif action is PumpAction.BA:
            if self.b == 0:
                raise PumpActionIsNoop()
            if self.a == self.MAX_A:
                raise PumpActionIsNoop()

            available_space = self.MAX_A - self.a
            to_move = min(available_space, self.b)
            new_b = self.b - to_move
            new_a = self.a + to_move
        elif action is PumpAction.BC:
            if self.b == 0:
                raise PumpActionIsNoop()
            if self.c == self.MAX_C:
                raise PumpActionIsNoop()

            available_space = self.MAX_C - self.c
            to_move = min(available_space, self.b)
            new_b = self.b - to_move
            new_c = self.c + to_move
        elif action is PumpAction.CA:
            if self.c == 0:
                raise PumpActionIsNoop()
            if self.a == self.MAX_A:
                raise PumpActionIsNoop()

            available_space = self.MAX_A - self.a
            to_move = min(available_space, self.c)
            new_c = self.c - to_move
            new_a = self.a + to_move
        elif action is PumpAction.CB:
            if self.c == 0:
                raise PumpActionIsNoop()
            if self.b == self.MAX_B:
                raise PumpActionIsNoop()

            available_space = self.MAX_B - self.b
            to_move = min(available_space, self.c)
            new_c = self.c - to_move
            new_b = self.b + to_move

        return cls(new_a, new_b, new_c)

    def next_states(self):
        result: list[Self] = []
        for action in PumpAction:
            try:
                new_state = self.pump(action)
            except PumpActionIsNoop:
                continue
            result.append(new_state)
        return result


def get_solution(state: PumpState) -> list[PumpState]:
    to_check: list[list[PumpState]] = [[state]]

    while len(to_check) > 0:
        path = to_check.pop(0)

        # check the next immediate states
        for next_state in path[-1].next_states():
            if next_state.is_final_state():
                # final state found, return it
                return [*path, next_state]

            to_check.append([*path, next_state])

    # should be unreachable, added to satisfy typechecker
    raise RuntimeError("failed to reach final state from intial state")


def main():
    initial_state = PumpState.initial_state()

    solution = get_solution(initial_state)

    print(f"Solution: {len(solution) - 1} steps")
    for state in solution:
        print(f"  {state}")


if __name__ == "__main__":
    main()
