import Mankala from "./mankala/Mankala.js";
import GameManager from "./mankala/GameManager.js";
import Human from "./mankala/Players/Human.js";
import c from "./mankala/constants.js";

const mankala = new Mankala(4);
const player1 = new Human(c.PLAYER_ONE);
const player2 = new Human(c.PLAYER_TWO);
const gameManager = new GameManager(player1, player2, mankala);
