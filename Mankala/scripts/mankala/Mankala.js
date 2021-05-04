import c from "./constants.js";

const Mankala = {
  init(numOfStones, boardSize = 14) {
    this.numOfStones = numOfStones;
    this.boardSize = boardSize;

    this.board = new Array(boardSize);
    this.board.fill(numOfStones);

    this.firstPlayerMankala = boardSize / 2 - 1;
    this.secondPlayerMankala = boardSize - 1;

    this.board[this.firstPlayerMankala] = 0;
    this.board[this.secondPlayerMankala] = 0;

    // this.playerMove = this.chooseRandomPlayer();
    this.playerMove = c.PLAYER_ONE;
    this.show();

    return this;
  },

  move(startingHole, player = this.playerMove) {
    if (!this.isMoveLegit(startingHole)) {
      return false;
    }
    const stones = this.takeStonesFromHole(startingHole);
    this.distributeStones(startingHole, stones, player);

    return true;
  },

  takeStonesFromHole(hole) {
    const stones = this.board[hole];
    this.board[hole] = 0;
    return stones;
  },

  distributeStones(startingHole, numOfStones, player = this.playerMove) {
    let i = startingHole;
    while (numOfStones > 0) {
      i = this.incrementHole(i);

      if (!this.checkIfOppositeMankala(i, player)) {
        this.board[i] += 1;
        numOfStones--;
      }
    }
    this.lastStoneCheck(i, player);
  },
  isMoveLegit(startingHole) {
    if (!this.checkSameSide(startingHole, this.playerMove)) {
      return false;
    }

    if (this.board[startingHole] === 0) {
      return false;
    }

    return true;
  },

  incrementHole(currHole) {
    return (currHole + 1) % this.boardSize;
  },

  lastStoneCheck(lastHole, player) {
    if (this.checkTakes(lastHole, player)) {
      this.takes(lastHole, player);
    }
    if (!this.checkLastInMankala(lastHole, player)) {
      this.playerMove = !this.playerMove;
    }
  },

  checkTakes(lastHole, player) {
    if (this.checkSameSide(lastHole, player)) {
      if (
        this.board[lastHole] === 1 &&
        this.board[this.getOppositeHole(lastHole)] !== 0
      ) {
        return true;
      }
    } else return false;
  },

  takes(lastHole, player) {
    const oppositeHole = this.getOppositeHole(lastHole, player);
    let taken = this.board[oppositeHole];
    taken += this.board[lastHole];

    player === c.PLAYER_ONE
      ? (this.board[this.firstPlayerMankala] += taken)
      : (this.board[this.secondPlayerMankala] += taken);

    this.takeStonesFromHoles(lastHole, oppositeHole);
  },

  takeStonesFromHoles() {
    for (let i = 0; i < arguments.length; i++) {
      this.board[arguments[i]] = 0;
    }
  },

  getOppositeHole(hole) {
    if (hole === this.secondPlayerMankala || hole === this.firstPlayerMankala) {
      return;
    }

    return this.secondPlayerMankala - hole - 1;
  },

  checkSameSide(lastHole, player) {
    if (player === c.PLAYER_ONE) {
      if (this.firstPlayerMankala > lastHole) {
        return true;
      }
    }
    if (player === c.PLAYER_TWO) {
      if (
        this.firstPlayerMankala < lastHole &&
        lastHole != this.secondPlayerMankala
      ) {
        return true;
      }
    }

    return false;
  },

  checkLastInMankala(lastHole, player) {
    if (player === c.PLAYER_ONE && lastHole === this.firstPlayerMankala) {
      return true;
    }
    if (player === c.PLAYER_TWO && lastHole === this.secondPlayerMankala) {
      return true;
    }
    return false;
  },

  checkIfOppositeMankala(hole, player) {
    if (player === c.PLAYER_ONE && hole === this.secondPlayerMankala) {
      return true;
    }
    if (player === c.PLAYER_TWO && hole === this.firstPlayerMankala) {
      return true;
    }

    return false;
  },

  whoWon() {
    if (hasEnded()) {
      if (
        this.board[this.firstPlayerMankala] >
        this.board[this.secondPlayerMankala]
      ) {
        return c.PLAYER_ONE;
      } else if (
        this.board[this.firstPlayerMankala] <
        this.board[this.secondPlayerMankala]
      ) {
        return c.PLAYER_TWO;
      }
      return 0;
    }
  },

  show() {
    console.log({ ...this });
  },
  chooseRandomPlayer() {
    return Math.random() < 0.5;
  },
  gatherFromHolesToMankalas() {
    for (let i = 0; i < this.firstPlayerMankala; i++) {
      let stones = this.takeStonesFromHole(i);
      this.board[this.firstPlayerMankala] += stones;
    }

    for (
      let i = this.firstPlayerMankala + 1;
      i < this.secondPlayerMankala;
      i++
    ) {
      let stones = this.takeStonesFromHole(i);
      this.board[this.secondPlayerMankala] += stones;
    }
  },
  hasEnded() {
    let hasEnded = true;
    for (let i = 0; i < this.firstPlayerMankala; i++) {
      if (this.board[i] !== 0) {
        hasEnded = false;
      }
    }

    if (hasEnded) return hasEnded;

    hasEnded = true;

    for (
      let i = this.firstPlayerMankala + 1;
      i < this.secondPlayerMankala;
      i++
    ) {
      if (this.board[i] !== 0) {
        hasEnded = false;
      }
    }

    return hasEnded;
  },
  evaluate() {
    return this.getScore(true) - this.getScore(false);
  },
  getScore(player) {
    let score = 0;
    if (c.PLAYER_ONE === player) {
      score = this.board[this.firstPlayerMankala];
    } else {
      score = this.board[this.secondPlayerMankala];
    }
    return score;
  },
  isFinished() {
    if (this.hasEnded()) {
      debugger;
      this.gatherFromHolesToMankalas();
      if (this.evaluate() > 0) {
        alert(`Wygrał gracz nr 1! Score ${this.evaluate()}`);
      } else {
        alert(`Wygrał gracz nr 2! Score ${this.evaluate()}`);
      }
    }
  },
  allPlayerMoves(player) {
    const moves = [];
    let start = 0;
    let end = this.firstPlayerMankala;
    if (player === c.PLAYER_TWO) {
      start = this.firstPlayerMankala + 1;
      end = this.secondPlayerMankala;
    }

    for (let i = start; i < end; i++) {
      if (this.board[i] > 0) {
        moves.push(i);
      }
    }
    return moves;
  },
};

export default Mankala;
