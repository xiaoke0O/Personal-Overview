gmt begin map-out/Xuchang-in-Henan-with-bro-JM png,pdf
    gmt set MAP_GRID_PEN_PRIMARY gray,12_12
    @REM 绘制河南各市边界，黄河，标红许昌市界
    gmt coast -Jm105/35/1:1200000 -R110/117/31/37 -TdjLT+w8c+l+o2c -Bafg -G244/243/239 -S167/194/223 --FONT_ANNOT_PRIMARY=60p --MAP_FRAME_WIDTH=15p
    gmt plot CN-Rivers.dat -W0.9p,blue
    gmt plot Henan-border-La.dat -W1.0p
    gmt plot Xuchang-border-L1.dat -W2.5p,red
    echo 113.65 34.76 | gmt plot -Sc0.8c -Gblack
    echo 113.65 34.76 | gmt plot -Sc1.5c -W2p,black
    echo 113.65 34.76 ML 郑州 | gmt text  -F+f40p,39+j -Dj0.9c/0.9c
gmt end