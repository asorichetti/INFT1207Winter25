###################################################
# Name: Alex Sorichetti
# Student #: 101000609
# Description: A program which takes in readings from temperature sensors
# and gives the minimum temp, the max temp, and the average temp
###################################################
def temp_input(num_sensors):
    temp_range = []
    contain=0
    print("Please remember, sensors can only detect temperatures ")
    for i in range (0, num_sensors, 1):
        contain=0
        while(contain == 0):
            try:
                entered_temp = float(input(f"Please enter the temperature reading from sensor number {i+1}: "))
                if -50 <= entered_temp <= 150:
                    temp_range.append(entered_temp)
                    contain = 1
                else:
                    print("Error: Temperature is out of valid range for sensor readings")
                
            except ValueError:
                print("Error: Please only enter numeric values")
    return(temp_range)

def temp_sort(temps):
    contain = 0
    while(contain < 5):
         temps.sort()
         contain+=1
    return(temps)

def temp_min_max(temps):
    result_holder = []
    result_holder.append(temps[0])
    result_holder.append(temps[len(temps)-1])
    return (result_holder)

def temp_average(temps, result_holder):
    avg = sum(temps)/len(temps)
    avg = round(avg, 2)
    result_holder.append(avg)
def main():
    print("Hello, Welcome to the Temperature Sensor Program.")
    num_sensors = int(input("How many sensors do you have in your system? "))
    temps = temp_input(num_sensors)
    temps = temp_sort(temps)
    result_holder = temp_min_max(temps)
    temp_average(temps, result_holder)
    print(f"Your sensors had a minimum recorded value of {result_holder[0]}, and a maximum recorded value of {result_holder[1]}. The average temperature was {result_holder[2]}")
main()