function [ A_proxima ] = quest_10 ( A, k )
  [ U S V ] = svd( A );
  
  i = k + 1;
  
  while( i <= min( size( S ) ) )
    S( i, i ) = 0;
    i += 1;
  endwhile
  
  A_proxima = U * S * V';
endfunction
