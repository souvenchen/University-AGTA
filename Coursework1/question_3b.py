from fractions import Fraction
import logging
import random
import time


logging.basicConfig()
_logger = logging.getLogger("question_3b")
_logger.setLevel(logging.INFO)


def run_experiment(player_1_starting, player_2_starting):
  # Only the value for heads is stored. Tails is '1 - player_i'.
  player_1_heads = player_1_starting
  player_2_heads = player_2_starting
  number_rounds = 1

  # Used to track the error. The results are taken to be true once
  # the error has been below 0.001 for both players for 50 rounds.
  # (Those numbers are of course chosen rather arbitrarily, since this
  # is all experimental rather than mathematical.)
  consequtive_errors = 0

  _logger.info("Initial setup:")
  _logger.info("Player 1's (pure) strategy: (%s, %s)", player_1_heads,
      1 - player_1_heads)
  _logger.info("Player 2's (pure) strategy: (%s, %s)", player_2_heads,
      1 - player_2_heads)

  while consequtive_errors < 50:
    expected_player_1 = Fraction(player_1_heads, number_rounds)
    expected_player_2 = Fraction(player_2_heads, number_rounds)

    _logger.debug("Round %s:", number_rounds)
    _logger.debug("Player 1's statistical mixed strategy: (%s, %s)",
        expected_player_1, 1 - expected_player_1)
    _logger.debug("Player 2's statistical mixed strategy: (%s, %s)",
        expected_player_2, 1 - expected_player_2)

    # Find player 1's pure best response.
    if expected_player_2 > Fraction(1, 2):
      # Player 2 is more likely to play heads, so player 1 should play heads
      # as well.
      player_1_move = 1
    elif expected_player_2 < Fraction(1, 2):
      # Player 2 is more likely to play tails, so player 1 should play tails
      # as well.
      player_1_move = 0
    else:
      # The ratio is exactly 50:50, so guess.
      player_1_move = random.randint(0, 1)

    # Find player 2's pure best response.
    if expected_player_1 > Fraction(1, 2):
      # Player 1 is more likely to play heads, so player 2 should play tails.
      player_2_move = 0
    elif expected_player_1 < Fraction(1, 2):
      # Player 1 is more likely to play tails, so player 2 should play heads.
      player_2_move = 1
    else:
      # The ratio is exactly 50:50, so guess.
      player_2_move = random.randint(0, 1)

    # Update the error stats.
    player_1_error = abs(0.5 - float(expected_player_1))
    player_2_error = abs(0.5 - float(expected_player_2))
    _logger.debug("Errors: %s, %s", player_1_error, player_2_error)
    if player_1_error < 0.001 and player_2_error < 0.001:
      consequtive_errors += 1
    else:
      consequtive_errors = 0

    number_rounds += 1
    player_1_heads += player_1_move
    player_2_heads += player_2_move

  _logger.info("Finished after %s rounds, with final mixed strategies:",
      number_rounds)
  _logger.info("Player 1's statistical mixed strategy: (%s, %s)",
      expected_player_1, 1 - expected_player_1)
  _logger.info("Player 2's statistical mixed strategy: (%s, %s)",
      expected_player_2, 1 - expected_player_2)
  print


def convert(num):
  return 'H' if num == 1 else 'T'


def main():
  before = time.time()
  for i in range(2):
    for j in range(2):
      _logger.info("Trying starting pair (%s, %s)", convert(i), convert(j))
      run_experiment(i, j)
  after = time.time()
  _logger.info("Experiment took %.2f seconds", after - before)


if __name__ == '__main__':
  main()