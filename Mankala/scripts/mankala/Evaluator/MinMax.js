export default class MinMax {
  constructor(depth) {
    this.depth = depth;
  }

  evalBestMove(position, maximizingPlayer) {
    let copy = _.cloneDeep(position);
    let move = this.minmax(copy, this.depth, maximizingPlayer)[0];
    return move;
  }

  minmax(position, depth, maximizingPlayer) {
    if (depth == 0 || position.hasEnded()) {
      let ev = position.evaluate();
      return [0, ev];
    }

    let move;
    let evaluation;

    if (maximizingPlayer) {
      let maxEval = Number.MIN_SAFE_INTEGER;
      let max_move = 0;

      const moves = position.allPlayerMoves(true);

      for (let child of moves) {
        let childPosition = _.cloneDeep(position);
        childPosition.move(child);

        [move, evaluation] = this.minmax(
          childPosition,
          depth - 1,
          childPosition.playerMove
        );

        if (evaluation >= maxEval) {
          maxEval = evaluation;
          max_move = child;
        }
      }

      return [max_move, maxEval];
    } else {
      let minEval = Number.MAX_SAFE_INTEGER;
      let min_move = 8;

      const moves = position.allPlayerMoves(false);

      for (let child of moves) {
        let childPosition = _.cloneDeep(position);
        childPosition.move(child);

        [move, evaluation] = this.minmax(
          childPosition,
          depth - 1,
          childPosition.playerMove
        );

        if (evaluation <= minEval) {
          minEval = evaluation;
          min_move = child;
        }
      }

      return [min_move, minEval];
    }
  }
}
