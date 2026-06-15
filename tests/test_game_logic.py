import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, parse_guess, get_range_for_difficulty


# --- Bug 1: check_guess hint direction (int secret) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high_returns_go_lower():
    # Bug: high guess was telling player to go HIGHER instead of LOWER
    # guess=90, secret=8 → guess is too high → must say Go LOWER
    outcome, message = check_guess(90, 8)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low_returns_go_higher():
    # Bug: low guess was telling player to go LOWER instead of HIGHER
    # guess=8, secret=90 → guess is too low → must say Go HIGHER
    outcome, message = check_guess(8, 90)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- Bug 2: string secret — string comparison broke numeric logic ---

def test_string_secret_high_guess_returns_go_lower():
    # Bug: "15" > "9" is False in string comparison (compares "1" vs "9")
    # so guess=15 vs secret="9" would wrongly say Go HIGHER
    outcome, message = check_guess(15, "9")
    assert outcome == "Too High"
    assert "LOWER" in message

def test_string_secret_low_guess_returns_go_higher():
    # Bug: "5" > "10" is True in string comparison (compares "5" vs "1")
    # so guess=5 vs secret="10" would wrongly say Go LOWER
    outcome, message = check_guess(5, "10")
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_string_secret_exact_match_is_win():
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"


# --- Bug 3: parse_guess range validation ---

def test_parse_guess_rejects_above_range():
    # Bug: game accepted numbers above the difficulty's max (e.g. 150 on Easy)
    ok, value, err = parse_guess("150", 1, 100)
    assert ok is False
    assert value is None
    assert "between" in err

def test_parse_guess_rejects_below_range():
    # Bug: game accepted numbers below the difficulty's min
    ok, value, err = parse_guess("0", 1, 20)
    assert ok is False
    assert value is None
    assert "between" in err

def test_parse_guess_accepts_within_range():
    ok, value, err = parse_guess("15", 1, 20)
    assert ok is True
    assert value == 15
    assert err is None

def test_parse_guess_rejects_non_number():
    ok, _, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert "not a number" in err.lower()

def test_parse_guess_rejects_empty():
    ok, _, _ = parse_guess("", 1, 100)
    assert ok is False


# --- Bug 4: difficulty ranges are correct and descending in attempt logic ---

def test_easy_range():
    # Easy should be the smallest range (1–20)
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_easy_range_smaller_than_normal():
    # Easy should be easier (smaller range = fewer numbers to guess from)
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high
