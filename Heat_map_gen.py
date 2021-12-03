from PIL import Image
import numpy

def heatmapgen(Country,TotCases,Populace,barX,barY,barWidth,barHeight):

    map=[]
    for i in range(0,len(TotCases)):
        PopByCap=TotCases[i]/Populace

        im = Image.open(Country+'_MAP.png')
        pix = im.load()
        value = PopByCap
        if (i/len(TotCases))*100 == int((i/len(TotCases))*100):
            print('Loading Heatmap:',(i/len(TotCases))*100,'%')
        for x in range(0, im.size[0]):
            for y in range(0, im.size[1]):
                if(pix[x,y][3] > 0 and pix[x, y][0] != 0):
                    pix[x, y] = (int(200 * value), int(200 * (1-value)), 0)

        borderWidth = 5
        delimiterWidth = 3
#border
        for x in range(barX, barX+barWidth):
            for y in range(barY, barY+barHeight):
                pix[x, y] = (0, 0, 0)
        for x in range(barX+borderWidth, barX+barWidth-borderWidth):
            for y in range(barY + borderWidth, barY+barHeight - borderWidth):
                value = (y - (barY+borderWidth)) / (barHeight - (2*borderWidth))
                pix[x, y] = (int(200 * (1-value)), int(200 * (value)), 0)

# bar AT 75%
        delimY = int(0.25 * (barY + barHeight - (2*borderWidth) - (barY+borderWidth)) + barY+borderWidth) 
        for x in range(barX+borderWidth, barX+barWidth-borderWidth):
            for y in range(delimY, delimY+delimiterWidth):
                pix[x, y] = (0, 0, 0)
        
# bar AT 50%
        delimY = int(0.50 * (barY + barHeight - (2*borderWidth) - (barY+borderWidth)) + barY+borderWidth) 
        for x in range(barX+borderWidth, barX+barWidth-borderWidth):
            for y in range(delimY, delimY+delimiterWidth):
                pix[x, y] = (0, 0, 0)
        
# bar AT 25%
        delimY = int(0.75 * (barY + barHeight - (2*borderWidth) - (barY+borderWidth)) + barY+borderWidth)
        for x in range(barX+borderWidth, barX+barWidth-borderWidth):
            for y in range(delimY, delimY+delimiterWidth):
                pix[x, y] = (0, 0, 0)

        map.append(im)

    map[0].save(Country+'_Heatmap.gif', format="GIF", save_all=True, append_images=map[1:], optimize=False, duration=.2, loop=0)
    print('File saved as: '+Country+'_Heatmap.gif')