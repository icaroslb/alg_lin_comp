function [U S V] = quest_11( A )
  tamanhos = size( A );
  H = vertcat( horzcat( zeros( tamanhos ), A' ), horzcat( A, zeros( tamanhos ) ) );
  
  [Vetores, lambda] = eig( H );
  
  S = abs( lambda( 1 : tamanhos( 1 ), 1 : tamanhos( 2 ) ) );
  Vetores = sqrt( 2 ) * Vetores( :, 1 : tamanhos( 2 ) );
  
  V = Vetores( 1 : ( size( Vetores )( 1 ) / 2 ), : );
  U = Vetores( ( size( Vetores )( 1 ) / 2 ) + 1 : size( Vetores )( 1 ), : );
  
  for i = 1 : tamanhos( 1 )
    if ( lambda( i, i ) < 0 )
      U( :, i ) = -U( :, i );
    endif
  endfor
endfunction
