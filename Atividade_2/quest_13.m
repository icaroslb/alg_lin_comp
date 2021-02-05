function [resul] = quest_13 ( A )
  [U S V] = svd( A );
  
  S1 = eye( size( S ) );
  
  resul = U * S1 * V';
endfunction
