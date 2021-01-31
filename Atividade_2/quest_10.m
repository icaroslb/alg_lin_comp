function [ A_proxima ] = quest_10 ( A, k )
  [ U S V ] = svd( A );
  
  A_proxima = U( 1:k, 1:k ) * S( 1:k, : ) * V( :, : )';
endfunction
