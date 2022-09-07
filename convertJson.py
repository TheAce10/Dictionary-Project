import json

dictionary= {

}

with open("data.json") as infile:
    readfile= json.load(infile)


for i in range(1):
    for x in readfile:
        try:
            if x[0].lower()== "z":
                dictionary[x]= {"definition":readfile[x][0],
		"partOfSpeech": "",
		"synonyms": [],
		"antonyms": [],
		"examples": []}
                # dictionary[x]["definition"]=readfile[x][0]
        except:
            pass

for x in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    directory = "./words_data/" + x + ".json"
    with open(directory) as dir:
        dictionary_data = json.load(dir)
        for i in dictionary_data:
            try:
                # if x[0].lower()== "a":
                dictionary_data[i]= dictionary_data[i.lower()]
                    # dictionary[x]["definition"]=readfile[x][0]
            except:
                pass
    with open(directory, "w") as outfile:
        outfile.write(dictionary_data)


"""for x in ["A"]:
# ,"B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    directory = "./words_data/" + x + ".json"
    with open(directory) as dir:
        dictionary_data = json.load(dir)
        for x in dictionary_data:
            dictionary_data= x.lower()
print(dictionary_data)
        


json_object= json.dumps(dictionary, indent= 0)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)"""