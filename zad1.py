class hamming:
    def distance(self, str1, str2):
        if len(str1)!=len(str2):
            raise ValueError("Str nie są równej długości")
        elif str1!=str2:
            return 0
        elif len(str1) == 1 and len(str2)==1:
                return 1
        elif len(str1)>1 and len(str2)>1:
                suma=0
                for i in range(len(str1)):
                    if str1[i] != str2[i]:
                        suma+=1
                return suma
