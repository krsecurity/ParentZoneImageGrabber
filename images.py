import requests # to get image from the web
import shutil # to save it locally
import sys # args

key = sys.argv[0]
for number in range(193420,215884):
    image_url = "https://api.iconnectdaily.net/api/v1/media/" + str(number) + "?key=" + key + "&size=full&u=2021-07-14T09:32:29"
    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True
    
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
        print('Image sucessfully downloaded: ',filename)
    else:
        print('Image couldn\'t be retreived')
