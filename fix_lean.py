import re

with open('test_lean/RiemannSpectralPurity.lean', 'r') as f:
    content = f.read()

# Fix Real.rpow_left_inj to Real.rpow_right_inj and add exact_mod_cast
content = content.replace('exact (Real.rpow_left_inj h_pos (by positivity) h_one_ne).mp h_norm', 'exact (Real.rpow_right_inj h_pos h_one_ne).mp h_norm')
content = content.replace('(k : ℕ) (hk : k ≥ 1)', '(k : ℕ) (_hk : k ≥ 1)')

with open('test_lean/RiemannSpectralPurity.lean', 'w') as f:
    f.write(content)
