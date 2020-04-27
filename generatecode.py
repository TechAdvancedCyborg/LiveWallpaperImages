links= ["https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/january.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/february.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/march.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/april.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/may.png","lhttps://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/june.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/july.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/august.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/september.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/october.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/november.png","https://raw.githack.com/TechAdvancedCyborg/LiveWallpaperImages/master/Cropped/december.png"]
# links= ["1","2","3","\"4\"","5","6","7","8","9","10","11","12"]
numbersource = "df(M)"
output="$"
for x in range(len(links)):
	output=output+"if("+numbersource+"="+str(x+1)+","+"\""+links[x]+"\""+","
# output = output[:-1]
output = output+"Error"
output = output+(")"*len(links))+"$"
print(output)
