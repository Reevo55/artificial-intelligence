import Mankala from "./mankala/Mankala.js";
import GameManager from "./mankala/GameManager.js";
import Human from "./mankala/Players/Human.js";
import Computer from "./mankala/Players/Computer.js";
import c from "./mankala/constants.js";
import MinMax from "./mankala/Evaluator/MinMax.js";

const minmax = new MinMax(4);
const mankala = Mankala.init(4);
const player1 = new Human(c.PLAYER_ONE);
const player2 = new Computer(c.PLAYER_TWO, minmax);
const gameManager = new GameManager(player1, player2, mankala);
