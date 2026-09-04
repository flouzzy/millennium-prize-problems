with open('test_lean/PvsNPQuiverEntropy.lean', 'r') as f:
    content = f.read()

# Remove Nlinarith import
content = content.replace('import Mathlib.Tactic.Nlinarith\n', '')
content = content.replace("import Mathlib.Analysis.SpecialFunctions.Pow.Real", "import Mathlib.Analysis.SpecialFunctions.Pow.Real\nimport Mathlib.Tactic.Cases")

# Replace induction' and exact_mod_cast if necessary, and fix nlinarith in circuit_lower_bound_strict
new_proof = """    have h_quad : (k + 1 : ℝ) ^ 2 < (k : ℝ) ^ 2 * 2 := by
      have hk_pos : (k : ℝ) ≥ 0 := by linarith
      have h1 : 4 * (k : ℝ) ≤ (k : ℝ) * (k : ℝ) := mul_le_mul_of_nonneg_right hk_ge_4 hk_pos
      have h2 : (k : ℝ) * (k : ℝ) = (k : ℝ) ^ 2 := by ring
      have h3 : 4 * (k : ℝ) ≤ (k : ℝ) ^ 2 := by linarith
      have h4 : 2 * (k : ℝ) + 8 ≤ 4 * (k : ℝ) := by linarith
      have h5 : 2 * (k : ℝ) + 1 < 2 * (k : ℝ) + 8 := by linarith
      have h6 : 2 * (k : ℝ) + 1 < (k : ℝ) ^ 2 := by linarith
      have h7 : (k + 1 : ℝ) ^ 2 = (k : ℝ) ^ 2 + 2 * (k : ℝ) + 1 := by ring
      linarith
    linarith"""

import re
# Find the block we need to replace
pattern = r"    have h_quad : \(k \+ 1 : ℝ\) \^ 2 < \(k : ℝ\) \^ 2 \* 2 := by\n      have : \(k : ℝ\) \^ 2 - 2 \* \(k : ℝ\) - 1 > 0 := by nlinarith\n      nlinarith\n    linarith"
content = re.sub(pattern, new_proof, content)

# Fix positivity type casting in exp_two_gt_linear
content = content.replace("have hk_cast : (k : ℝ) ≥ 1 := by positivity", "have hk_cast : (k : ℝ) ≥ 1 := by exact_mod_cast hk")

# Fix positivity type casting in circuit_lower_bound_strict
content = content.replace("have hk_ge_4 : (k : ℝ) ≥ 4 := by positivity", "have hk_ge_4 : (k : ℝ) ≥ 4 := by exact_mod_cast hk")


with open('test_lean/PvsNPQuiverEntropy.lean', 'w') as f:
    f.write(content)
