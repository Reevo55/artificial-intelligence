import c from "../constants.js";

export default class Computer {
  constructor(whichPlayer, evaluator) {
    this.whichPlayer = whichPlayer;
    this.evaluator = evaluator;
  }

  makeMove(gameState) {
    return this.evaluator.evalBestMove(gameState, this.whichPlayer);
  }
}
