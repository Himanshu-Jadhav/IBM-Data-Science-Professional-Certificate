#!/usr/bin/env python
# coding: utf-8

# <h1>Exercise 1: Create a Jupyter Notebook</h1>

# <h2><strong>Name:</strong> IBM Data Science Ecosystem Peer Assignment Himanshu  </h2>

# <strong>Exercise 2 - Create a markdown cell with the title of the notebook.</strong>

# <h1>Data Science Tools and Ecosystem</h1>

# **Himanshu Jadhav**
# <br> BE - Artifical Intelligence and Data Science

# *I am interested in data science because I love telling stories with data and using data to help bring that data to life.I love helping others. In data science that could be helping a business understand its customers or improving the way it uses its customer data.*
# 
# <p>In this notebook, Data Science Tools and Ecosystem are summarized.<p>

# <strong>Exercise 3 - Create a markdown cell for an introduction. (1 pt)</strong>

# <strong>Objectives:</strong>
# <ul>
#     <li>List popular languages that Data Scientists use.</li>
#     <li>List commonly used libraries used by Data Scientists.</li>
#     <li>Comment on Data Science tools.</li>
# </ul>
#     

# <strong>Exercise 4 - Create a markdown cell to list data science languages. (3 pts)</strong>

# Some of the popular languages that Data Scientists use are:
# <ol>
#     <li>Python.</li>
#     <li>R.</li>
#     <li>SQL.</li>
#     <li>Java.</li>
#     <li>Julia.</li>
#     <li>Scala.</li>
#     <li>C/C++.</li>
#     <li>JavaScript.</li>
# </ol>
# 

# <strong>Exercise 5 - Create a markdown cell to list data science libraries. (3 pts)</strong>

# Some of the commonly used libraries used by Data Scientists include:
# <ol>
#     <li>TensorFlow.</li>
#     <li>NumPy.</li>
#     <li>SciPy.</li>
#     <li>Pandas.</li>
#     <li>Matplotlib.</li>
#     <li>Keras.</li>
#     <li>SciKit-Learn.</li>
#     <li>PyTorch.</li>
#     <li>Scrapy.</li>
#     <li>BeautifulSoup.</li>
#     <li>LightGBM.</li>
#     <li>ELI5.</li>
#     <li>Theano.</li>
#     <li>NuPIC.</li>
#     <li>Ramp.</li>
#     <li>Pipenv.</li>
#     <li>Bob.</li>
#     <li>PyBrain.</li>
#     <li>Caffe2.</li>
#     <li>Chainer.</li>
# </ol>

# <strong>Exercise 6 - Create a markdown cell with a table of Data Science tools. (3 pts)</strong>

# Data Science Tools:
# 
# <table style="width:100%">
#   <tr>
#     <th>Data Science Tools</th>
#     <th></th>
#     <th></th>
#   </tr>
#   <tr>
#     <td>SAS. It is one of those data science tools which are specifically designed for statistical operation</td>
#     <td></td>
#     <td></td>
#   </tr>
#   <tr>
#     <td>Apache Spark</td>
#     <td></td>
#     <td></td>
#   </tr>
#   <tr>
#     <td>BigML</td>
#     <td></td>
#     <td></td>
#   </tr>
# </table>

# <strong>Exercise 7 - Create a markdown cell introducing arithmetic expression examples. (1 pt)</strong>

# <h3>Below are a few examples of evaluating arithmetic expressions in Python</h3>

# In[21]:


# Arithmetic operations
code = compile("8 + 9", "<string>", "eval")
eval(code)


# In[22]:


code1 = compile("(4 - 8) * 2", "<string>", "eval")
eval(code1)


# In[23]:


import math
# Volume of a sphere
code2 = compile("2 / 8 * math.pi * math.pow(20, 3)", "<string>", "eval")
eval(code2)


# <strong>Exercise 8 - Create a code cell to multiply and add numbers.(2 pts)</strong>

# This a simple arithmetic expression to mutiply then add integers

# In[24]:


(7*3)+8


# <strong>Exercise 9 - Create a code cell to convert minutes to hours. (2 pts)</strong>

# This will convert 200 minutes to hours by diving by 60

# In[25]:


days = 0
hours = 0
mins = 0

time = 200
leftover_minutes = time % 1440
hours = leftover_minutes / 60
print(str(days) + " days, " + str(hours) + " hours, " + str(mins) +  " mins. ")


# <strong>Exercise 10 -Insert a markdown cell to list Objectives.</strong>

# <p>Below the introduction cell created in Exercise 3, insert a new markdown cell to list the objectives that this notebook covered (i.e. some of the key takeaways from the course). In this new cell start with an introductory line titled: Objectives: in bold font. Then using an unordered list (bullets) indicate 3 to 5 items covered in this notebook, such as List popular languages for Data Science.</p>

# <strong>Exercise 11 - Create a markdown cell to indicate the Author’s name.</strong>

# <h2>Author:</h2> Himanshu Jadhav
