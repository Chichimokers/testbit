from MoodleClient import MoodleClient
import json
jsons ='{"url":"https:\/\/cursos.uo.edu.cu\/draftfile.php\/16602\/user\/draft\/33018802\/HackTheBox_Forge%5BOSCPStyle%5DTWITCHLIVE%5BpXE6rm0VDzM%5D.mp4.3.part","id":33018802,"file":"HackTheBox_Forge[OSCPStyle]TWITCHLIVE[pXE6rm0VDzM].mp4.3.part"}'
cargadp = json.loads(jsons)
print(cargadp["url"])
cargadp["url"]="https://cursos.uo.edu.cu/draftfile.php/16602/user/draft/33018802/"

jsonfinal = {"url":"https://cursos.uo.edu.cu/draftfile.php/16602/user/draft/33018802/","id":"s","file":"aa"}

print(json.encoder.JSONEncoder().encode(jsonfinal))
