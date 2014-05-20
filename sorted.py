#coding=utf-8
strs = ['a', 'BB', 'zz', 'CC']
print (sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print (sorted(strs, reverse=True) )  ## ['zz', 'aa', 'CC', 'BB']
strs = ['ccc', 'aaaa', 'd', 'bb']
print (sorted(strs, key=len) ) ## ['d', 'bb', 'ccc', 'aaaa'] sort by length of character 中文注释测试
print ("中文输出")

#specifying "str.lower" as the key function is a way to force the sorting to treat uppercase and lowercase the same:
print (sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']


#sort by string's last letter
strs = ['xc', 'zb', 'yd' ,'wa']

def MyFn(s):
    return s[-1]

print (sorted(strs,key=MyFn))

#len get the length of strs
print ("The length of strs is:",len(strs))

# insertion sort
strN=[1,4,3,9,2,4,0,2,5]

def insertion_sort(strN):
    for index in range(1,len(strN)):
        value=strN[index]
        i=index-1
    #    print i,strN[i]," ",index,strN[index]
        while i>=0:
                if value<strN[i]:
                    #   print i,strN[i]," ",index,strN[index]
                    strN[i+1]=strN[i]
                    strN[i]=value
                    i=i-1
                else:
                    break
    return strN

print (insertion_sort(strN))


#how to define a string
a = "a string by quotes        gg"
b = 'second \" string" '
c = "b+a"
print (c)
print (a.split(' '))
print (a.find('q'))
print (eval (c)) #eval try to make () a program

print (13/3,13/3.0)
