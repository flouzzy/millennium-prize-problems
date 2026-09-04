with open('test_lean/PvsNPQuiverEntropy.lean', 'r') as f:
    content = f.read()

# Let's replace the whole exp_two_gt_linear proof
new_proof = """theorem exp_two_gt_linear (n : ℕ) (hn : n ≥ 1) :
    (2 : ℝ) ^ (n : ℝ) > (n : ℝ) := by
  induction' n, hn using Nat.le_induction with k hk ih
  · norm_num
  · push_cast
    have h_step : (2 : ℝ) ^ (k + 1 : ℝ) = (2 : ℝ) ^ (k : ℝ) * 2 := by
      rw [← Real.rpow_add_one (by norm_num)]
    rw [h_step]
    have hk_cast : (k : ℝ) ≥ 1 := by exact_mod_cast hk
    linarith"""

content = content.replace(new_proof, """theorem exp_two_gt_linear (n : ℕ) (hn : n ≥ 1) :
    (2 : ℝ) ^ (n : ℝ) > (n : ℝ) := by
  induction' n, hn using Nat.le_induction with k hk ih
  · norm_num
  · push_cast
    have h_step : (2 : ℝ) ^ (k + 1 : ℝ) = (2 : ℝ) ^ (k : ℝ) * 2 := by
      have : (2 : ℝ) > 0 := by norm_num
      rw [Real.rpow_add this]
      have : (2 : ℝ) ^ (1 : ℝ) = 2 := by norm_num
      rw [this]
    rw [h_step]
    have hk_cast : (k : ℝ) ≥ 1 := by exact_mod_cast hk
    linarith""")

new_proof_2 = """theorem circuit_lower_bound_strict (n : ℕ) (hn : n ≥ 4) :
    (n : ℝ) ^ 2 < (2 : ℝ) ^ (n : ℝ) := by
  induction' n, hn using Nat.le_induction with k hk ih
  · norm_num
  · push_cast
    have hk_ge_4 : (k : ℝ) ≥ 4 := by exact_mod_cast hk
    have h_pow_step : (2 : ℝ) ^ (k + 1 : ℝ) = (2 : ℝ) ^ (k : ℝ) * 2 := by
      have : (2 : ℝ) > 0 := by norm_num
      rw [Real.rpow_add this]
      have : (2 : ℝ) ^ (1 : ℝ) = 2 := by norm_num
      rw [this]
    rw [h_pow_step]
    have h_quad : (k + 1 : ℝ) ^ 2 < (k : ℝ) ^ 2 * 2 := by
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
pattern2 = r"theorem circuit_lower_bound_strict \(n : ℕ\) \(hn : n ≥ 4\) :\n    \(n : ℝ\) \^ 2 < \(2 : ℝ\) \^ \(n : ℝ\) := by[\s\S]*?linarith"
content = re.sub(pattern2, new_proof_2, content)


with open('test_lean/PvsNPQuiverEntropy.lean', 'w') as f:
    f.write(content)
