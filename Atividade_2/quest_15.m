function [] = quest_15 ()
  im = double( imread( "imagem.tiff" ) ) / 255;
  
  im_1 = quest_10( im, 1 );
  im_5 = quest_10( im, 5 );
  im_10 = quest_10( im, 10 );
  im_50 = quest_10( im, 50 );
  
  subplot( 2, 2, 1 ); imshow( im_1 );  subplot( 2, 2, 2 ); imshow( im_5 );
  subplot( 2, 2, 3 ); imshow( im_10 ); subplot( 2, 2, 4 ); imshow( im_50 );
endfunction