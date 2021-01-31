function [] = quest_9 ()
  A_1 = rand( 3, 5 );
  A_2 = rand( 5, 5 );
  A_3 = rand( 5, 3 );
  
  disp( "Matrix 3x5: " );
  A_1
  
  disp( "Matrix 5x5: " );
  A_2

  disp( "Matrix 5x3: " );
  A_3
  
  Ai_1 = pseudo_inversa( A_1 );
  Ai_2 = pseudo_inversa( A_2 );
  Ai_3 = pseudo_inversa( A_3 );
  
  a_1 = Ai_1 * A_1;
  b_1 = A_1  * Ai_1;
  c_1 = A_1  * Ai_1 * A_1;
  d_1 = Ai_1 * A_1  * Ai_1;
  
  a_2 = Ai_2 * A_2;
  b_2 = A_2  * Ai_2;
  c_2 = A_2  * Ai_2 * A_2;
  d_2 = Ai_2 * A_2  * Ai_2;
  
  a_3 = Ai_3 * A_3;
  b_3 = A_3  * Ai_3;
  c_3 = A_3  * Ai_3 * A_3;
  d_3 = Ai_3 * A_3  * Ai_3;
  
  disp( "Item a) :" );
  a_1
  a_2
  a_3
  
  disp( "Item b:" );
  b_1
  b_2
  b_3
  
  disp( "Item c:" );
  c_1
  c_2
  c_3
  
  disp( "Item d:" );
  d_1
  d_2
  d_3
endfunction

function [Ai] = pseudo_inversa ( A )
  [U S V] = svd( A );
  S_ = S;
  
  for i = 1: min( size( S_, 1 ), size( S_, 2 ) )
    if ( S_(i, i) != 0 )
      S_(i, i) = 1 / S_(i, i);
    else
      break;
    endif
  endfor
  
  Ai = V * S_' * U';
endfunction