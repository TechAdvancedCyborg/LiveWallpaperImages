links= ["linkjanuary","linkfebruary","linkmarch","linkapril","linkmay","linkjune","linkjuly","linkaugust","linkseptember","linkoctober","linknovember","linkdecember"]
numbersource = "df(M)"
output="$"
for x in range(len(links)):
	output=output+"if("+numbersource+"="+str(x+1)+","+links[x]+","
output = output[:-1]
output = output+(")"*len(links))+"$"
print(output)