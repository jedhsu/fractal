class Update:
    def update_placement_analysis(
        topos,
        analysis,
        action_id,
        burn: Burn,
    ):
        stats = topos.tree[state].stats
        astats = stats[action_id]
        stats[action_id] = PlacementAnalysis(
            astats.P,
            astats.W + q,
            astats.N + 1,
        )
