function [posto] = quest_12( A )
  [U S V] = svd( A );
  
  erro = norm( S, 2 ) * eps;
  posto = min( size( A ) );
  
  for i = 1 : posto
    if ( abs( S( i, i ) ) < erro )
      posto = i;
      break;
    endif
  endfor
endfunction
