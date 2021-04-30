import Evaluator from "./Evaluator.js";

export default class MinMax extends Evaluator {
  constructor(depth) {
    this.depth = depth;
  }

  evaluate(gameState, player) {
    best = this.evalRec(gameState, this.depth, player);
  }

  evalRec(gameState, depth, player) {
    if (depth === 0) return 0, gameState.evaluate();

    if (gameState.hasEnded()) {
      return 0, gameState.evaluate();
    }

    if (player) {
      let min = Number.MAX_SAFE_INTEGER;
      let min_index = -1;

      for (let i = 0; i < gameState.board[gameState.secondPlayerMankala]; i++) {
        let gameCopy = { ...gameState };
      }
    }
  }
}
