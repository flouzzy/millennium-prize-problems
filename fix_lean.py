with open("test_lean/RiemannSpectralPurity.lean", "r") as f:
    content = f.read()

content = content.replace(
    "exact (Real.rpow_left_inj h_pos (by positivity) h_one_ne).mp h_norm",
    "exact (Real.rpow_right_inj h_pos h_one_ne).mp h_norm"
)

content = content.replace(
    "theorem frobenius_power_purity (p : ℝ) (hp : p > 1) (re_rho : ℝ) (k : ℕ) (hk : k ≥ 1)",
    "theorem frobenius_power_purity (p : ℝ) (hp : p > 1) (re_rho : ℝ) (k : ℕ) (_hk : k ≥ 1)"
)

with open("test_lean/RiemannSpectralPurity.lean", "w") as f:
    f.write(content)
