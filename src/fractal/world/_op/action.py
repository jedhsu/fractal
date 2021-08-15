"""

    *Action*

"""


class Action(
    World,
):
    def action_string(self):
        """
        Return a human-readable string representing provided action.
        """

    def parse_action(self):
        """
        Return the action described by string `str` or `nothing` if `str` does not
        denote a valid action.
        """
