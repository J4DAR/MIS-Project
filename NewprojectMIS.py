#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import os  # Importing the os module for file handling
from PIL import Image  # Importing the Image module from PIL for image manipulation
from IPython.display import display  # Importing display function from IPython.display to display images in Jupyter Notebook

# Path to the directory containing style folders
styles_path = "MIS_Project/Styles"

# List of style folders
style_folders = ["vintage", "streetwear", "minimalist", "workwear", "preppy"]

# Dictionary to store user selections count for each style
selection_count = {style: 0 for style in style_folders}

# Iterate through each style folder
for style in style_folders:
    print(f"Select your preferred {style} style:")
    
    # Iterate through each image in the style folder
    for i in range(1, 5):  # Assuming there are 4 images for each style
        # Constructing the path to the image file
        image_path = os.path.join(styles_path, style, f"{style}_{i}.jpg")  # Assuming image names are style_1.jpg, style_2.jpg, etc.
        
        # Check if the image file exists
        if os.path.exists(image_path):
            # Open the image using PIL's Image module
            img = Image.open(image_path)
            # Display the image in the Jupyter Notebook
            display(img)
            # Prompt the user to select the style
            user_choice = input("Do you like this style? (yes/no): ").lower()
            
            # Update the selection count if the user likes the style
            if user_choice == "yes":
                selection_count[style] += 1

# Find the most selected style
most_selected_style = max(selection_count, key=selection_count.get)

# Print the most selected style
print(f"You selected {most_selected_style} the most!")

# Construct the URL for the Pinterest board related to the most selected style
pinterest_url = f"https://www.pinterest.com/search/pins/?q={most_selected_style}+style+inspiration"
# Print a message indicating redirection
print(f"Redirecting you to {pinterest_url}")
# Add code to open the URL in a web browser


# In[ ]:





# In[ ]:


plt.plot([1, 2, 3])


# In[ ]:


import os
from PIL import Image
import random
import matplotlib.pyplot as plt  # Importing matplotlib for displaying images in a grid

# Path to the directory containing style folders
styles_path = "MIS_Project/Styles"

# List of style folders
style_folders = ["vintage", "streetwear", "minimalist", "workwear", "preppy"]

# Dictionary to store user selections count for each style
selection_count = {style: 0 for style in style_folders}

# Iterate through each round
for round_num in range(4):
    print(f"Round {round_num + 1} of 4:")
    
    # Collecting images for each style
    style_images = {}

    # List to store indices of images displayed in this round
    displayed_indices = []

    # Iterate through each style folder
    for style in style_folders:
        # Collecting a random image for the current round
        image_index = random.randint(1, 4)  # Assuming there are 4 images for each style
        while image_index in displayed_indices:  # Ensure the image hasn't been displayed already in this round
            image_index = random.randint(1, 4)
        displayed_indices.append(image_index)

        # Constructing the path to the image file
        image_path = os.path.join(styles_path, style, f"{style}_{image_index}.jpg")  # Assuming image names are style_1.jpg, style_2.jpg, etc.
        if os.path.exists(image_path):
            img = Image.open(image_path)
            style_images[style] = img

    # Displaying images of each style together
    fig, axes = plt.subplots(1, len(style_images), figsize=(15, 5))  # Creating subplots for each style image
    for i, (style, img) in enumerate(style_images.items()):
        axes[i].imshow(img)
        axes[i].set_title(style)
        axes[i].axis('off')
    plt.show()

    # Now the user can select the preferred style based on the displayed images
    user_choice = input("Enter the name of the style you prefer: ").lower()

    # Update the selection count based on user's choice
    if user_choice in selection_count:
        selection_count[user_choice] += 1

# Find the most selected style
most_selected_style = max(selection_count, key=selection_count.get)
print(f"You selected {most_selected_style} the most!")

# Redirecting to Pinterest board based on the most selected style
pinterest_url = f"https://www.pinterest.com/search/pins/?q={most_selected_style}+style+inspiration"
print(f"Redirecting you to {pinterest_url}")
# Add code to open the URL in a web browser


# In[ ]:


from IPython.display import Image

# Replace 'image_path' with the path to your image file
image_path = 'https://i.pinimg.com/474x/5a/1a/4d/5a1a4d253e8eb7234fce40c26f369f86.jpg'

# Display the image
Image(filename=image_path)


# In[ ]:




