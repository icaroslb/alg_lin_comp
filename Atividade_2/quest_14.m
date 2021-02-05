function [] = quest_14 ()
    A = rand( 5, 3 );
    A_ = quest_13( A );
    
    [ U S V ] = svd( A );
    
    disp( "Norma da matriz U: " )
    norm( U )
    
    disp( "Norma da matriz Vt: " )
    norm( V' )
    
    disp( "Norma da matriz gerada: " )
    norm( A_ )
endfunction
