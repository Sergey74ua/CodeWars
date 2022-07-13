<?php // Rock Paper Scissors!

function rpc ($p1, $p2) {
  if ($p1 == $p2)
    return Draw!;
  else if ($p1 == rock && $p2 == scissors 
          $p1 == scissors && $p2 == paper 
          $p1 == paper && $p2 == rock)
    return Player 1 won!;
  else
    return Player 2 won!;
}

// Лучший вариант (ВОЗМОЖНО):
/*
function rpc ($p1, $p2) {
    return $p1 === $p2 ? "Draw!" : "Player ".(false === strpos('rockscissorspaperrock', $p1.$p2) ? 2 : 1)." won!";
}
*/