gmt begin map-out/Henan-in-China-with-bro-JM png,pdf
    gmt set MAP_GRID_PEN_PRIMARY 0.25p,gray,2_2
    @REM 绘制省边界，标红河南边界
    gmt coast -JM105/35/10c -R70/138/13/56 -Ba10f5g10 -G244/243/239 -S167/194/223
    gmt basemap -Lg85/17.5+c17.5+w800k+f+u -TdjLT+w1.5c+l+o0.75c --FONT_ANNOT_PRIMARY=4p
    gmt plot CN-border-La.gmt -W0.1p
    @REM gmt plot CN-Rivers.dat -W0.1p,blue
    gmt plot Henan-border-L1.dat -W0.2p,red

    @REM 绘制南海区域
    gmt inset begin -DjRB+w1.8c/2.2c -F+p0.5p
        gmt coast -JM? -R105/123/3/24 -G244/243/239 -S167/194/223 -Df
        gmt plot CN-border-La.gmt -W0.1p
    gmt inset end
gmt end