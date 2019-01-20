import re
class basic_calculator:
	def get_bracket(self,s):
		self.s=s;
		left_counter=0;
		counter=0;
		right_counter=0;
		left_bracket=[]
		right_bracket=[]
		outer_pair=[];
		for i in range(len(s)):
			if s[i]=='(':
				left_bracket.append(i);
				left_counter+=1
				counter+=1
			if s[i]==')':
				right_bracket.append(i);
				right_counter+=1;
				if right_counter==left_counter:
					if left_counter==1:
						outer_pair.append([left_bracket[counter-1],i]);"""solo small outter pair found"""
					else:
						outer_pair.append([left_bracket[counter-right_counter],i])
					left_counter=0;
					right_counter=0;"""big outter bracket found"""
		print("outer_pair is :",outer_pair)
		return outer_pair;
	def first_level_cal(self,s,l=[]):
		out_put=0;
		if len(l)==0:
			out_put=0;
		else:
			if len(l)>1:
				print("bigger")
				for j in range(len(l)-1):
					print(l[j][1],l[j+1][0])
					for m in range(l[j][1],l[j+1][0]):
						print(s[m])
						if s[m]=='+' and s[m+1]!='(':
							out_put+=int(self.Find_num(s,m+1,l[j+1][0]));
						if s[m]=='-' and s[m+1]!='(':
							out_put-=int(self.Find_num(s,m+1,l[j+1][0]));
			if l[0][0]!=0:
				out_put+=int(self.Find_num(s,0,len(s)));
				for i in range(0,l[0][0]):
					if s[i]=='+' and s[i+1]!='(':
						out_put+=int(self.Find_num(s,i+1,l[0][0]));
					if s[i]=='-' and s[i+1]!='(':
						out_put-=int(self.Find_num(s,i+1,l[0][0]));
			if l[-1][1]!=len(s)-1:
				for i in range(l[-1][1],len(s)):
					if s[i]=='+':
						out_put+=int(self.Find_num(s,i,len(s)));
					if s[i]=='-':
						out_put-=int(self.Find_num(s,i,len(s)));
		return out_put;

	def Cal(self,s):
		pairs=[];
		big_sum=0;
		inner_sum=0;
		operator="";
		if len(self.get_bracket(s))!=0:
			pairs=self.get_bracket(s);
			big_sum=self.first_level_cal(s,pairs);
			print("first level",big_sum)
			for j in range(len(pairs)):
				inner_sum=self.Cal(s[pairs[j][0]+1:pairs[j][1]])

				if s[pairs[j][0]-1]=='(' or pairs[j][0]==0:
					big_sum+=inner_sum;
				else:
					operator=s[pairs[j][0]-1];
					if operator=='+':
						big_sum+=inner_sum;
					if operator=='-':
						print("haha")
						big_sum-=inner_sum;
						print("big_sum 1 is:",big_sum)
			print("big_sum is:",big_sum)
			return big_sum
		else:
			inner_sum+=int(self.Find_num(s,0,len(s)));
			for m in range(len(s)):
				if s[m]=='+':
					inner_sum+=int(self.Find_num(s,m,len(s)));
				if s[m]=='-':
					inner_sum-=int(self.Find_num(s,m,len(s)));
			print("inner_sum is :",inner_sum)
			return inner_sum;

	def Find_num(self,s,start,end):
		print("whats left is:",s[start:end])
		a=re.findall(r'\d+',s[start:end]);
		return a[0];
