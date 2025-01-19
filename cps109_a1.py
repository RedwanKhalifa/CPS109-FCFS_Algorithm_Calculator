# -*- coding: utf-8 -*-
"""
@author: Redwan Khalifa 5########

Problem Description:
    
    The objective of this program is to produce the results of a simple CPU scheduling algorithm called FCFS (First Come First Serve). 
    The user will input the name of their process along with their respective arrival time and burst time in a file. The program will 
    then return the values for the turn around time and waiting time with averages for each process in the console.
    
    FCFS Algorithum and Formula for TAT and WT found here: https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/
"""

#Function takes data from file and translates it to a list
def readProcesses(textfile):
    
    #Create list to store input
    listOfProcesses = []
    
    #Read file
    with open(textfile, 'r') as file:
        next(file) #skip first line which demonstrates format
        for line in file:
            
            #Sorts out the data for each line that is requested
            processID, arrivalTime, burstTime = line.strip().split()
            
            listOfProcesses.append({
                'ProcessID': processID,
                'ArrivalTime': int(arrivalTime),
                'BurstTime': int(burstTime),
            })
            
    return listOfProcesses
    
#This function performs the FCFS algorithum
def computeFCFS(data):
    
    #Sorts processes based on ArrivalTime
    data.sort(key = lambda x: x['ArrivalTime'])
    
    #Initialize variables
    index, currentTime, totalTAT, totalWT = 0, 0, 0, 0
    
    #Cycle through all processes in data
    while index < len(data):
        
        i = data[index]
        arrivalTime = i['ArrivalTime']
        burstTime = i['BurstTime']
        
        #Current time must begin at Arrival Time or later
        if currentTime < arrivalTime:
            currentTime = arrivalTime
        
        #Find completionTime
        completionTime = currentTime + burstTime
        
        #Turn Around Time = Completion Time - Arrival Time
        i['TurnAroundTime'] = completionTime - arrivalTime
        
        #Waiting Time = Turn Around Time - Burst Time
        i['WaitingTime'] = i['TurnAroundTime'] - burstTime
        
        #Current Time updates after a process
        currentTime = completionTime
    
        #Add all data points for TAT and WT 
        totalTAT += i['TurnAroundTime']
        totalWT += i['WaitingTime']
        
        #Increment to next process
        index += 1
        
    #Find average for TAT and WT
    averageTurnAroundTime = round(totalTAT/len(data), 2)
    averageWaitingTime = round(totalWT/len(data), 2)
        
    finalData = [data, averageTurnAroundTime, averageWaitingTime]
    
    return finalData
    
def outputResults(finalData):
    
    #Unpack list
    data, averageTurnAroundTime, averageWaitingTime = finalData
    
    #Print headings
    print(f"{'Process':<12}{'Arrival Time':<17}{'Burst Time':<15}{'Waiting Time':<17}{'Turn Around Time':<17}")
    
    #Print data for each process
    for i in data:
        print(
            f"{i['ProcessID']:<12}"
            f"{i['ArrivalTime']:<17}"
            f"{i['BurstTime']:<15}"
            f"{i['WaitingTime']:<17}"
            f"{i['TurnAroundTime']:<17}"
            )
    
    #Print averages for WT an TAT
    print(f"\nAverage Waiting Time     : {averageWaitingTime}")
    print(f"Average Turn Around Time : {averageTurnAroundTime}")

#Input data from txt
processes = 'dataInput.txt'

#Run functions
processData = readProcesses(processes)

processFCFS = computeFCFS(processData)

outputResults(processFCFS)