#spin function
def spin_wheel():
  ball_land = random.randrange(-1, 37)
  if ball_land == -1:
    ball_land = '00'
  return ball_land


def play_game(bet_type , bet_place , bet):
  spin_wheel()
  print("The ball landed on " + str(ball_land) + "."
  #straight bets
  if bet_type == "Straight Bet":
    multiplier = 35
    straight_bets = [*range(1, 37)]
  ######
  ######
  #split bets
  if bet_type == "Split Bet":
    multiplier = 17
    split_bets = []
    for number in range(1, 34):
      split_bets.append([number, number + 3])
    for number in range(1, 36):
      if number % 3 == 0:
        continue
      split_bets.append([number, number + 1])
  ######
  ######
  #street bets
  if bet_type == "Street Bet":
    multiplier = 11
    street_bets = []
    for number in range(1 , 35 , 3):
      street_bets.append([number , number + 1, number + 2])
    street_bets.append(['00' , 0 , 2])
    street_bets.append([0 , 1 , 2])
    street_bets.append(['00' , 2 , 3])
  ######
  ######
  #corner bets
  if bet_type == "Corner Bet":
    multiplier = 8
    corner_bets = []
    for number in range(1, 37):
      if number % 3 == 0:
        continue
      corner_bets.append([number, number + 1, number + 3, number + 4])
  ######
  ######
  #sucker bet
  if bet_type == "Sucker Bet":
    multiplier = 6
    sucker_bet = ['00' , 0 , 1 , 2 , 3]
  ######
  ######
  #line bet
  if bet_type == "Line Bet":
    multiplier = 5
    line_bet = []
    for number in range(1 , 35, 3):
      line = []
      for i in range(0 , 6):
        line.append(number + i)
      line_bet.append(line)
  ######
  ######
  #column bet
  if bet_type == "Column Bet":
    multiplier = 2
    column_bet = []
    for number in range(1 , 4):
      column = []
      for i in range(0, 36, 3):
        column.append(number + i)
      column_bet.append(column)
  ######
  ######
  #dozens bet
  if bet_type == "Dozens Bet":
    multiplier = 2
    dozens_bet = [[*range(1, 13)] , [*range(13, 25)] , [*range(25 , 37)]]
  ######
  ######
  #color bet
  if bet_type == "Color Bet":
    multiplier = 1
    red_bet = [1 , 3 , 5 , 7 , 9 , 12 , 14 , 16 , 18 , 19 , 21 , 23 , 25 , 27 , 30 , 32 , 34 , 36]
    black_bet = [2 , 4 , 6 , 8 , 10 , 11 , 13 , 15 , 17 , 20 , 22 , 24 , 26 , 28 , 29 , 31 , 33 , 35]
  ######
  ######
  #odd or even bet
  if bet_type == "Odd/Even Bet":
    multiplier = 1
    odd_bet = []
    even_bet = []
    for i in range(1 , 37):
      if i % 2 == 1:
        even_bet.append(i)
      else:
        odd_bet.append(i)
  ######
  ######
  #low high bet
  if bet_type == "Low/High Bet":
    multiplier = 1
    low_bet = [*range(1 , 19)]
    high_bet = [*range(19 , 37)]
  else:
    print("That's not a betting option, please select again.")