# %%
#pip install pytube
#download with python

# %%
import pytube
link = input("Enter your youtube link : ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloded', link)

# %%
  
  


