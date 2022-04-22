#!/bin/bash


x=0

while IFS= read -r line
do
	for i in $line
	do	
		x_length=${#x}
		
		if [ "$x_length" == 3 ]
		then
			sudo docker stop "$i"
			sudo docker rmi -f "$i"
		fi
		
		x+=1
	done	
	x=0
	
done < <(sudo docker images)


while IFS= read -r line
do
	for i in $line
	do	
		x_length=${#x}
		
		if [ "$x_length" == 1 ]
		then
			sudo docker stop "$i"
			sudo docker rm -f "$i"
		fi
				x+=1
	done	
	x=0
	
done < <(sudo docker ps -a)
