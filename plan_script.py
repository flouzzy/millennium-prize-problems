with open("test_lean/RiemannSpectralPurity.lean", "r") as f:
    content = f.read()

content = content.replace("exact (Real.rpow_left_inj h_pos (by positivity) h_one_ne).mp h_norm", "exact (Real.rpow_right_inj h_pos h_one_ne).mp h_norm")
content = content.replace("(hk : k ≥ 1)", "(_hk : k ≥ 1)")

with open("test_lean/RiemannSpectralPurity.lean", "w") as f:
    f.write(content)
