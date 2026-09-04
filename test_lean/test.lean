import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

theorem my_quad (k : ℝ) (hk : k ≥ 4) : (k + 1) ^ 2 < k ^ 2 * 2 := by
  have hk_pos : k ≥ 0 := by linarith
  have h1 : 4 * k ≤ k * k := mul_le_mul_of_nonneg_right hk hk_pos
  have h2 : k * k = k ^ 2 := by ring
  have h3 : 4 * k ≤ k ^ 2 := by linarith
  have h4 : 2 * k + 8 ≤ 4 * k := by linarith
  have h5 : 2 * k + 1 < 2 * k + 8 := by linarith
  have h6 : 2 * k + 1 < k ^ 2 := by linarith
  have h7 : (k + 1) ^ 2 = k ^ 2 + 2 * k + 1 := by ring
  linarith
