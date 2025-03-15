#Rename Filenames (Project Description)


import os


from datetime import datetime

# Specify the directory where the files are located
directory = 'files'


# Get a list of all filenames in the specified directory
filenames = os.listdir(directory)


# Loop through each file in the directory

for filename in filenames:
    
    # Construct the full file path
     filepath = os.path.join(directory, filename)   

    
     # Get the current date in YYYY-MM-DD format
     current_date = datetime.now().strftime('%Y-%m-%d')  

    
     #dify the filename to include the current date (removing the last 4 characters, usually ".txt")

     new_filename = f'{filename[:-4]}-{current_date}.txt' 

       # Construct the new full file path with the updated filename
     new_filepath = os.path.join(directory, new_filename)  
    
       # Rename the file
     os.rename(filepath, new_filepath)  

        # Print the old and new filenames
     print(f'{filename} rename to {new_filename}')

   

# Print a success message
print('Files renamed successfully!')    
