from pyyoutube import Api
from pytube import YouTube
from os import mkdir
from json import dumps

#fonctions pour les logs
suivi = {
    "title":"",
    "logs":[]
}
def update(data):
    f = open("data.json", "w")
    f.write(dumps(data))
    f.close()

def addLog(inf):
    global suivi
    suivi["logs"].append(inf)
    print(inf)
    update(suivi)

#initialisation
update(suivi)

#fonction pour dl une serie
def download(playlist):
    global suivi
    URL_TEMPLATE = "https://www.youtube.com/watch?v="
    yt = Api(api_key="AIzaSyD_KNDOiC93q1olAU97988wLS0smcXeHu8")

    #innitialisation de la playlist
    videos = yt.get_playlist_items(playlist_id=playlist,count=None)
    title = yt.get_playlist_by_id(playlist_id=playlist).items[0].to_dict()["snippet"]["title"]
    title = "".join(x for x in title if x.isalnum() or x == " ")
    
    suivi["title"] = title
    update(suivi)


    #creation dossiers
    addLog("telechargement de \""+title+"\"")
    try:
        mkdir("./output")
        addLog("output crée")
    except:
        addLog("dossier output existant !")

    try:
        mkdir("./output/"+title)
        addLog("dossier crée")
    except:
        addLog("dossier existant !")

    i = 1
    for cur in [i.snippet.resourceId.videoId for i in videos.items]:
        #initialisation dl chaque videos
        ended = True
        while ended:
            try:
                addLog("video - "+["0"+str(i),str(i)][int(i >= 10)])
                yt = YouTube(URL_TEMPLATE+cur)
                #print(yt.streams.filter(mime_type="audio/mp3"))
                #break
                    
                stream = yt.streams.get_by_itag(18)
                if stream == None:
                    addLog("download en 360p impossible , tentative en 720p")
                    stream = yt.streams.get_by_itag(22)

                stream.download(output_path="./output/"+title,filename_prefix=["0"+str(i)+"-",str(i)+"-"][int(i >= 10)])
                
                addLog("done !")
                ended = False
                
            except:
                addLog("erreur 404 , nouvelle tentative")
                #print(e)
        i+=1
    addLog("finished !")

#download("PLMEX-5pLzLWK0MhLWAhibJD6KWDzVLCkH")
# plays = open("links.txt", "r")
# for cur in plays:
#     temp = cur
#     if temp[-1]=="\n":
#         temp= temp[:-1]
#     download(temp)
