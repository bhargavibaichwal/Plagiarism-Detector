#!/usr/bin/env python
# coding: utf-8

# In[17]:


from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image
import os

top=Tk()
top.title('Plagiarism detector')

canvas=Canvas(width=800,height=500)
canvas.pack()


label1=Label(top,text='original text ',font=('Times New Roman',20),fg='white',bg='black')
label1.pack(side=RIGHT)
labell1=canvas.create_window(180,100,anchor=N,window=label1)

enl1=Entry(top,bd=10,font=('Times New Roman',20))
enl1.pack(side=RIGHT)
enll1=canvas.create_window(180,150,anchor=N,window=enl1)


label2=Label(top,text='Written text ',font=('Times New Roman',20),fg='white',bg='black')
label2.pack(side=RIGHT)
labell2=canvas.create_window(600,100,anchor=N,window=label2)


enl2=Entry(top,bd=10,font=('Times New Roman',20))
enl2.pack(side=RIGHT)
enll1=canvas.create_window(600,150,anchor=N,window=enl2)


def check():
    username=enl1.get()
    password=enl2.get()
    text1=username
    text2=password
    
    import re
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer as ps
    from nltk.stem import WordNetLemmatizer
    from tkinter import messagebox


    review=re.sub('[^a-zA-Z]', ' ',text1)# removing all the punctuation marks from the sentences by using sub method where are the charachters other than a-z will be replaced by spaces
    review=review.lower()# lowering each and every sentence

    text_tokens = nltk.word_tokenize(review)


    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]


    list1_compare=[]
    from nltk.stem import PorterStemmer
    ps =PorterStemmer()
    for w in tokens_without_sw:
        rootWord=ps.stem(w)
        list1_compare.append(rootWord)
        

    
    review2=re.sub('[^a-zA-Z]', ' ',text2)# removing all the punctuation marks from the sentences by using sub method where are the charachters other than a-z will be replaced by spaces
    review2=review2.lower()

    text_tokens2 = nltk.word_tokenize(review2)

    tokens_without_sw2 = [word for word in text_tokens2 if not word in stopwords.words()]


    list2_compare=[]
    from nltk.stem import PorterStemmer
    ps =PorterStemmer()
    for w in tokens_without_sw2:
            rootWord=ps.stem(w)
            list2_compare.append(rootWord)
    
    
    
    ls3=[]
    
    def intersection(list1,list2):
        for i in list1:
            if i in list2:
                ls3.append(i)       
                

    intersection(list1_compare,list2_compare)
    
    sum=len(list1_compare)+len(list2_compare)-len(ls3)

    similarity_index=(len(ls3)*100)/sum
    similarity_index
    
    if similarity_index==0:
        messagebox.showinfo(" Similarity index is ","0")
        
    elif similarity_index!=0:
        messagebox.showinfo(" Similarity index is ",similarity_index)
        

    

login_button=Button(top,text='Check Plagiarism',font=('Comic Sans MS',30),bg='white',command=check)
login_button.pack(side=TOP,pady=50)
login_button1=canvas.create_window(400,400,anchor=CENTER,window=login_button)




top.mainloop()


# In[ ]:





# In[51]:





# In[ ]:





# In[ ]:





# In[ ]:




