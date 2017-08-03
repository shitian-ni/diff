import sys
import os
import re
import Levenshtein as levenshtein

def new_change_in_line(a,b):
    mb = levenshtein.matching_blocks(levenshtein.editops(a,b), a, b)
    common = ''.join([a[x[0]:x[0]+x[2]] for x in mb])
    diff_in_b = ""
    common_index=0
    for c in b:
        if(common_index>=len(common)):
            diff_in_b+=c
            continue
        if(c==common[common_index]):
            common_index+=1
        else:
            diff_in_b+=c
    return diff_in_b

def clean_diff_output(diff_output):
	result = ""

	pattern="c[0-9,]*\n$"
	a=[]
	b=[]
	line_numbers=[]
	for i in range(len(diff_output)):
		output = diff_output[i];
		num=re.search(pattern,output)
		if(num):
		    these_line_numbers=num.group(0)[1:-1]
		    numbers = these_line_numbers.split(",")
		    if(len(numbers)>1):
		    	for i in range(int(numbers[0]),int(numbers[1])+1):
		    		line_numbers.append(str(i))
		    else:
		    	line_numbers.append(numbers[0])
		elif(output[:2]=="< "):
			a.append(output[2:])
		elif(output[:2]=="> "):
			b.append(output[2:])
			if(len(a)==len(b)):
				for a_,b_,line in zip(a,b,line_numbers):
					diff=new_change_in_line(a_,b_)
					result+="line #"+line+": "+diff+"\n"
				a.clear()
				b.clear()
				line_numbers.clear()
				
	return result

if __name__ == "__main__":

	if(len(sys.argv)!=4):
		print("need 3 file names as command line arguments, 2 input file name, 1 output file name")
	with open(sys.argv[1]) as f:
	    lines1 = f.readlines()
	with open(sys.argv[2]) as f:
	    lines2 = f.readlines()

	command_output=os.popen("diff "+sys.argv[1]+" "+sys.argv[2]).readlines()

	write_to_file = clean_diff_output(command_output)

	f = open(sys.argv[3], 'w')
	f.write(write_to_file)
	f.close()
