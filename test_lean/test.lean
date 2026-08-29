import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Cases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

theorem circuit_lower_bound_strict (n : ℕ) (hn : n ≥ 5) :
    (n : ℝ) ^ 2 < (2 : ℝ) ^ (n : ℝ) := by
  induction' hn with k hk ih
  · norm_num
