#!/usr/bin/python3
import sys
import os

#search = sys.argv[1]
#searchlist = sys.argv
#searchlist.remove(searchlist[0])
os.system("clear")
print("Enter search:")
search = input("> ")
searchlist = search.split(" ")
searchstr = "+".join(searchlist)
os.system(f"wget -q 'https://nyaa.si/?f=0&c=0_0&q={searchstr}' -O results -q")

results = open("results","r")
line = results.readline()
while "<tbody>" not in line:
    line = results.readline()

resultlist = []
magnets = []
sizes = []

while "</tbody>" not in line:
    while '<a href="/?c=' not in line:
        if "</tbody>" in line:
            break
        line = results.readline()
    if "</tbody>" in line:
        break
    line = line.replace('<a href="/?c=',"")
    line = line.replace('">',"")
    line = line.replace('" title="',"")
    line = line.replace('					',"")
    line = line[3:]
    result_type = line
    results.readline()
    results.readline()
    results.readline()
    results.readline()
    line = results.readline()
    if 'class="comments"' in line:
        results.readline()
        line = results.readline()
    line = line.replace('					<a href="/view/',"")
    line = line.replace('</a>',"")
    splitline = line.split('" title="')
    line = splitline[0]
    lineA = splitline[1]
    splitline = lineA.split('">')
    lineA = splitline[0]
    result_id = line
    result_title = lineA
    result_type = result_type.replace("\n","")
    resultlist.append(str(f"{result_id};;;{result_type};;;{result_title}"))
    results.readline()
    results.readline()
    results.readline()
    line = results.readline()
    line = line.replace('					<a href="',"")
    line = line.replace('"><i class="fa fa-fw fa-magnet"></i></a>',"")
    magnets.append(line)
    results.readline()
    line = results.readline()
    line = line.replace('				<td class="text-center">',"")
    line = line.replace('</td>',"")
    line = line.replace("\n","")
    sizes.append(line)

counter = 0
for item in resultlist:
    if counter == 20:
        break
    citem = resultlist[counter]
    splititem = citem.split(";;;")
    print(f"{counter+1}. {splititem[2]} | Type: {splititem[1]} | Filesize: {sizes[counter]} | id:{splititem[0]}")
    counter+=1

print("Select result (number):")
selection = int(input("> "))
citem = resultlist[selection-1]
splititem = citem.split(";;;")
print("You selected:")
print(f"{selection}. {splititem[2]} | Type: {splititem[1]} | Filesize: {sizes[selection-1]} | id:{splititem[0]}")
print("Download torrent/magnet link?")
print("    1. Torrent")
print("    2. Magnet")
old_selection = selection
selection = int(input("> "))
if selection == 1:
    os.system(f"wget -q https://nyaa.si/download/{splititem[0]}.torrent")
    print(f"Torrent saved as {splititem[0]}.torrent")
if selection == 2:
    link = (magnets[old_selection-1])
    link = link.replace('&amp;',"&")
    print(link)

#if selection == 2:
#    os.system(f"xdg-open {link}")
#if selection == 1:
#    os.system(f"xdg-open ./{splititem[0]}.torrent")
