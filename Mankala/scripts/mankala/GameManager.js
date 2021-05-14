import c from "./constants.js";

export default class GameManager {
  gameInfo = document.querySelector(".info");

  constructor(player1, player2, game) {
    if (player1.whichPlayer) {
      this.player1 = player1;
      this.player2 = player2;
    } else {
      this.player1 = player2;
      this.player2 = player1;
    }
    this.game = game;

    this.registerListeners(this.player1);

    this.updateTurn();

    this.gameInfo.textContent = "Start playing!";
  }

  whichPayer() {
    if (this.game.playerMove === c.PLAYER_ONE) {
      return "Player 1 turn";
    } else return "Player 2 turn";
  }

  updateTurn() {
    this.whichTurn = this.game.playerMove;
    this.gameInfo.textContent = this.whichPayer();
  }
  registerListeners(player) {
    let curr = 0;
    let end = this.game.firstPlayerMankala;

    if (player.whichPlayer === c.PLAYER_TWO) {
      curr = this.game.firstPlayerMankala + 1;
      end = this.game.secondPlayerMankala;
    }

    for (; curr < end; curr++) {
      let holeId = ".h" + curr;
      let hole = document.querySelector(holeId);

      hole.addEventListener("click", (e) => {
        let hole = e.target.classList[1].substr();
        hole = parseInt(hole.replace(/\D/g, ""));
        if (this.game.checkSameSide(hole, this.whichTurn)) {
          if (this.makeMove(hole, true)) {
            debugger;
            this.updateUI();

            if (this.game.playerMove === c.PLAYER_TWO) this.computerMove();
            this.updateTurn();
          } else {
            alert("Wrong move");
          }
        } else {
          console.log("Not your turn mate");
        }
      });
    }
  }

  makeMove(hole, player) {
    if (!this.game.move(hole, player)) {
      return false;
    }
    this.game.isFinished();
    this.updateUI();
    this.updateTurn();
    return true;
  }

  updateUI() {
    this.game.show();
    for (let i = 0; i < this.game.boardSize; i++) {
      let holeId = ".h" + i;
      let hole = document.querySelector(holeId);

      hole.textContent = this.game.board[i];
    }
  }

  playWithComputer() {
    alert("Starting the game...");

    while (!this.game.hasEnded()) {
      this.game.show();
      let hole;

      if (c.PLAYER_TWO === this.game.whichTurn) {
        hole = player2.makeMove({ ...this.game });
      }

      if (!this.game.move(hole)) {
        console.log("Wrong move!");
        continue;
      }

      console.log("Move " + (hole + 1));
    }
  }

  computerMove() {
    let hole = parseInt(this.player2.makeMove(this.game));
    setTimeout(() => {
      alert(`Computer moved on ${hole}`);
      this.updateUI();
    }, 100);
    this.game.move(hole);
    this.game.isFinished();
    if (this.game.playerMove === false) {
      this.computerMove();
    }
  }
  computerVScomputer(randomMove = true) {
    if (randomMove) {
      let randMove = getRandomInt(0, this.game.firstPlayerMankala);
      this.game.move(randMove);
      console.log("Random move");
      console.log(randMove);
    }

    while (!this.game.hasEnded()) {
      this.game.show();
      let hole = 0;

      if (c.PLAYER_ONE === this.game.playerMove) {
        hole = parseInt(this.player1.makeMove(this.game));
        console.log(`Player 1, move ${hole}`);
      } else {
        hole = parseInt(this.player2.makeMove(this.game));
        console.log(`Player 2, move ${hole}`);
      }

      this.game.move(hole);
      this.updateUI();
    }
  }

  playHuman() {}
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}
