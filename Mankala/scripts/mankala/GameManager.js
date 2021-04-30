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
    this.registerListeners(this.player2);

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
          this.makeMove(hole, player.whichPlayer);
        } else {
          console.log("Not your turn mate");
        }
      });
    }
  }

  makeMove(hole, player) {
    this.game.move(hole, player);
    this.updateUI();
    this.updateTurn();
  }

  updateUI() {
    this.game.show();
    for (let i = 0; i < this.game.boardSize; i++) {
      let holeId = ".h" + i;
      let hole = document.querySelector(holeId);

      hole.textContent = this.game.board[i];
    }
  }

  playComputers() {
    while (!this.game.hasEnded()) {
      this.game.show();
      let hole;

      if (c.PLAYER_ONE === this.game.whichTurn) {
        hole = player1.makeMove();
      } else if (c.PLAYER_TWO === this.game.whichTurn) {
        hole = player2.makeMove();
      }

      if (!this.game.move(hole)) {
        console.log("Wrong move!");
        continue;
      }

      console.log("Move " + (hole + 1));
    }
  }

  playHuman() {}
}
