function [Ai] = quest_8 ( A )
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
