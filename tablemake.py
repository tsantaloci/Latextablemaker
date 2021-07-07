import os


def relativeenergtable(path):

    return


def dipoletable(name,path,path2,numb):
    filename = open(path,'r')
    data = filename.readlines()
    for num,i in enumerate(data):
        if 'Dipole' in i:
            for x in data[num+1:num+3]:
                if 'X=' in x:
                    xx = float(x[10:26])
                    yy = float(x[37:55])
                    zz = float(x[60:80])
                    tt = float(x[85:105])

                
                 #   print(x[60:])

    filename2 = open(path2 + '/' +'Dipinfo.tex','a+')
    filename2.write(str(numb) + ' & '+ str(xx) + " & " + str(yy) + ' & ' + str(zz) + ' & ' + str(tt)  + " \\\\ " + '\n' )


    return

def quadtable(name,path,path2,numb):
    filename = open(path,'r')
    data = filename.readlines()
    for num,i in enumerate(data):
        if 'Traceless' in i:
            for x in data[num+1:num+3]:
                if 'XX=' in x:
                    xx = float(x[10:26])
                    yy = float(x[37:55])
                    zz = float(x[60:])
                
                 #   print(x[60:])
                if 'XY=' in x:
                    xy = float(x[10:26])
                    xz = float(x[37:55])
                    yz = float(x[60:])
    filename2 = open(path2 + '/' +'quadinfo.tex','a+')
    filename2.write(str(numb) + ' & '+ str(xx) + " & " + str(yy) + ' & ' + str(zz) + ' & ' + str(xy) + ' & '+ str(xz) + ' & ' + str(yz) + " \\\\ " + '\n' )

    


 
   # os.remove('quad.out')
    

    return 




def main():
    path_to_src = '/Users/tsantaloci/Desktop/writingpapers/src'
    path_to_quad = '/Users/tsantaloci/Desktop/PAHcode/CNC2H/EOM/aniondipole/1Naph'
    name = 'CNC2H1Naph'
    os.chdir(path_to_quad)
    
    # When quadtables == yes will make the quadrapole moments tables
    
    quadtables = 'yes'
    quadtables = ''
    # makes the dipoletables == yes will make dipole moment tables 
    dipoletables = 'yes'
   # dipoletables = ''

    directory = []
    if quadtables == 'yes' and dipoletables == 'yes':
        print('Only one of them needs to not be commented')
        

    if quadtables == 'yes' and dipoletables == '':
        filename2 = open(path_to_src + '/' +'quadinfo.tex','w')
        filename2.write("\\begin{table}")
        filename2.write('\n')
        filename2.write("\\tiny")
        filename2.write('\n')
        filename2.write("\centering")
        filename2.write('\n')
        filename2.write("   \\begin{tabular}{ccccccc}")
        filename2.write('\n')
        filename2.write("    \hline")
        filename2.write('\n')
        # filename2.write("  B   & \multicolumn{2}{c}{Oscillator Strengths}  \\" + "\\")
        filename2.write(name +' & '+ "XX" + " & " + 'YY' + ' & ' + 'ZZ' + ' & ' + 'XY ' + '& '+ ' XZ' + ' & ' + 'YZ' + " \\\\")
        filename2.write('\n')
        filename2.write("\hline")
        filename2.write('\n')
        filename2.close()
        for i in os.listdir():
            i = int(i)
            directory.append(i)
        
        for i in sorted(directory):
            i = str(i)
            print(i)
            quadtable(name,path_to_quad + '/' + i +'/' + i + '.out',path_to_src,str(i))
        filename2.close()
        filename2 = open(path_to_src + '/' +'quadinfo.tex','a')
        filename2.write('\hline \n')
        filename2.write('\n')
        filename2.write('  \end{tabular}\n')
        filename2.write('\end{table}\n')
    if dipoletables == 'yes' and quadtables == '':
        filename2 = open(path_to_src + '/' +'dipinfo.tex','w')
        filename2.write("\\begin{table}")
        filename2.write('\n')
        filename2.write("\\tiny")
        filename2.write('\n')
        filename2.write("\centering")
        filename2.write('\n')
        filename2.write("   \\begin{tabular}{ccccccc}")
        filename2.write('\n')
        filename2.write("    \hline")
        filename2.write('\n')
        # filename2.write("  B   & \multicolumn{2}{c}{Oscillator Strengths}  \\" + "\\")
        filename2.write(name +' & '+ "X" + " & " + 'Y' + ' & ' + 'Z' + ' & ' + 'Tot ' +  " \\\\")
        filename2.write('\n')
        filename2.write("\hline")
        filename2.write('\n')
        filename2.close()
        for i in os.listdir():
            i = int(i)
            directory.append(i)
        
        for i in sorted(directory):
            i = str(i)
            print(i)
            dipoletable(name,path_to_quad + '/' + i +'/' + i + '.out',path_to_src,str(i))
        filename2.close()
        filename2 = open(path_to_src + '/' +'dipinfo.tex','a')
        filename2.write('\hline \n')
        filename2.write('\n')
        filename2.write('  \end{tabular}\n')
        filename2.write('\end{table}\n')

    


    return
main()
