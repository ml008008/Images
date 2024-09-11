#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install rembg')


# In[2]:


pip install --upgrade rembg


# In[3]:


pip install --upgrade pooch


# In[4]:


pip install pooch==1.6.0


# In[5]:


import requests
from PIL import Image
from rembg import remove
from io import BytesIO

# Load the image from a URL
image_url = "https://github.com/ml008008/Images/blob/34b93d40188f75544ed8c6548fb528f1eabc0750/0a3UtNzl5Ll3sq8K.png?raw=true"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Remove the green background
image = remove(image)

# Resize the image
image = image.resize((30, 20))

# Convert the image to grayscale
image = image.convert("L")

# Save the processed image
processed_image_path = "processed_image.png"
image.save(processed_image_path)

# Display the processed image
image.show()


# In[ ]:




