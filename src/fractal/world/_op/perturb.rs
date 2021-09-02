mod perturb {
    fn sample_dirichlet_noise(
        realizing: Realizing,
        noise: Noise,
    ):
        actions = world.possible_actions()
        n = len(actions)
        return rand(Dirichlet(n, noise))
}
