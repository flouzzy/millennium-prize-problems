with open("test_lean/PvsNPQuiverEntropy.lean", "r") as f:
    content = f.read()

content = content.replace("have hk_cast : (k : ℝ) ≥ 1 := by exact_mod_cast hk", "have hk_cast : (k : ℝ) ≥ 1 := by exact_mod_cast hk")
with open("test_lean/PvsNPQuiverEntropy.lean", "w") as f:
    f.write(content)
