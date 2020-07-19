import xlrd
import re

class Qa:
    def reader(self, path):
        data=xlrd.open_workbook(path)
        table=data.sheet_by_index(0)
        nrows=table.nrows
        animalList=[]
        foodList=[]
        relationList=[]
        formeList=[]
        actionList=[]
        animalMessage=[]
        for index in range(1,nrows):
            # print(table.cell(index,0).value)
            animalList.append(str(table.cell(index,0).value).lower())
            foodList.append(table.cell(index,1).value)
            relationList.append(table.cell(index,2).value)
            formeList.append(table.cell(index,3).value)
            actionList.append(table.cell(index,4).value)
        animalMessage.append(animalList)
        animalMessage.append(foodList)
        animalMessage.append(relationList)
        animalMessage.append(formeList)
        animalMessage.append(actionList)
        return animalMessage

    def analyseQuestion(self, question):
        return re.compile('\w+').findall(question)


if __name__=="__main__":
    qa=Qa()
    animalMessage=qa.reader("D:\\pic5_fin\\base.xlsx")
    question=input("your question: ")
    worlds=qa.analyseQuestion(question)
    #print(animalMessage[0].__len__())
    answeranimal=[]
    for i in worlds:
        for index in range(animalMessage[0].__len__()):
            if str(animalMessage[0].__getitem__(index)).lower()==str(i).lower():
                if i not in answeranimal:
                    answeranimal.append(i)
                    str1 = "The"+i+" is a "+animalMessage[3].__getitem__(index)+" animal. "+animalMessage[2].__getitem__(index)+" and "+animalMessage[4].__getitem__(index)+"And, his favorite food is "+animalMessage[1].__getitem__(index)+"."


    if len(answeranimal) == 0:
        print("Sorry, this question is too difficult, I can't answer your question")



