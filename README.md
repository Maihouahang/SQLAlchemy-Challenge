# SQLAlchemy-Challenge

For this project, I will be using Python and SQLAlchemy to do a basic climate analysis and data exploration of Honolulu, Hawaii's climate database. Specifically, I will use SQLAlchemy ORM queries, Pandas, and Matplotlib to do a precipitation analysis and station analysis. After that, I will design a Flask API to create a climate app based on the queries that I have developed. 

References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with climate_starter.ipynb step 10 to make sure I was converting the dataset to datetime correctly. Retrieved from https://chat.openai.com/chat

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with climate_starter.ipynb step 11 for help with the code to perform a query to retrieve the data and precipitation scores. Retrieved from https://chat.openai.com/chat

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with climate_starter.ipynb step 14 for help with the code to design a query to find the most active stations. It specifically helped me with how to use the func.count method along with the group_by method to find the most active stations. Retrieved from https://chat.openai.com/chat

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with climate_starter.ipynb step 15 for help with the code to design a query to calculate the lowest, highest, and average temperature for the most active station ID. It specficially helped me with using the filter function to make sure I was retreviing the results from the most active station ID. Retrieved from https://chat.openai.com/chat

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with app.py step 74 to 77 for help with how to code the datetime format and how to properly filter through the dataset so that I'm able to location the most cative station and get all the data I need from that most active station. Retrieved from https://chat.openai.com/chat

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with app.py step 59 for help with how to code the datetime format properly, especially for this portion of the code: "dt.timedelta(days=365)". Retrieved from https://chat.openai.com/chat

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with app.py step 74 to 77 for help with how to properly filter through the dataset so that I'm able to location the most active station and get all the data I need from that most active station. Retrieved from https://chat.openai.com/chat

OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. Accessed on Dec 2024. I used this website for help with app.py step 84 to step 91 for help with how to find the min, avg, and max temps for the start date 01/01/2010 specifically. It also helped me with the if statements to make sure it gave me and/or whoever is using the climate app the error messages if they tried using a different date than the start date from the dataset. Lastly, it helped me with closing the if statement wih if no temps were found, what to notify whoever using the climate app a message to let them know. Retrieved from https://chat.openai.com/chat

