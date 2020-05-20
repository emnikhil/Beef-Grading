I = imread('Beef Grading/Images/63-0193-4.jpg');
[I2,rect] = imcrop(I);
imshow(I2);
imwrite(I2,'Beef Grading/Images/new.jpg');
newmap = im2bw(I2);
imshow(newmap)
pix = size(newmap);
no_of_pix = pix(1)*pix(2);
no_of_white_pix = sum(sum(newmap==1));
percent_of_white_pix = ((no_of_white_pix*100/no_of_pix)+2); % +2 for any false coloring.
disp(percent_of_white_pix);
if (percent_of_white_pix <45.4 )
    disp('Utility Grade Beef')
elseif (percent_of_white_pix > 45.4 ) && (percent_of_white_pix < 47.7 )
    disp('Select Grade Beef')
elseif (percent_of_white_pix  > 47.7 ) && (percent_of_white_pix < 50.0 )
    disp('Choice Grade Beef')
elseif (percent_of_white_pix > 50.0 ) && (percent_of_white_pix < 52.3 )
    disp('Prime Grade Beef')
elseif (percent_of_white_pix > 52.3 ) 
    disp('Wagyu')
end

