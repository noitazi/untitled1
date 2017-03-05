import httplib
import urllib

image_url = ''
headers = {
    # Request headers
    #'Content-Type': 'application/json',
    'Content-Type': 'application/octet-stream',

    'Ocp-Apim-Subscription-Key': 'b8f8e3d198df49cab280b1c11e8dcb9d',
}
params = urllib.urlencode({
    # Request parameters
    'visualFeatures': 'Categories,Tags,Description',
    # 'visualFeatures': 'Categories,Tags, Description, Faces, ImageType, Color, Adult',
    'details': 'Celebrities'
})
conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
file_name = 'Login.jpg'
img = open(file_name, 'rb').read()
conn.request("POST", "/vision/v1.0/analyze?%s" % params, img, headers)
response = conn.getresponse()
caption_data = response.read()
print(caption_data)
conn.close()