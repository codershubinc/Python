import requests # type: ignore
import random
import csv
import os

def generate_csv(file_name, headers, data_rows):
    try:
        # Ensure the 'temp' folder exists, if not, create it
        os.makedirs('./temp', exist_ok=True)

        # Define the full file path for storing the CSV in './temp'
        file_path = os.path.join('./temp', file_name)

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)  # Use the file object directly

            # Write headers
            writer.writerow(headers)

            # Write data rows
            writer.writerows(data_rows)

        print(f"CSV file '{file_path}' generated successfully!")
    except Exception as e:
        print(f"Error generating CSV: {e}")

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # If the response is JSON, parse and return it
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None






def generate_random_int(start, end):
    return random.randint(start, end)



def rand_id(id_length , type ):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    nums = '0123456789'
    symbols = '`~!@#$%^&*()-_=+[]{}|;:,.<>/?'
    id = ''

    if(type=='alpha') :
        for  i in range(id_length):
            id += alphabets[generate_random_int(0,25)]
            i+1
        return id
    elif(type=='num') :
        for  i in range(id_length):
            id += nums[generate_random_int(0,9)]
            i+1
        return id
    elif(type=='symbol') :
        for  i in range(id_length):
            id += symbols[generate_random_int(0,32)]
            i+1
        return id
    else :
        for i in range(id_length):
            id += alphabets[generate_random_int(0,len(alphabets)-1)] + nums[generate_random_int(0,len(nums)-1)] + symbols[generate_random_int(0,len(symbols)-1)]
            i+1
        return id


headers = ["ID", "Name", "Age", "Email"]



def gen_data(length_of_rows , data):
    data_rows = [] 

    for i in range(length_of_rows):
        rnd_int = generate_random_int(0,len(data['data']['data']['firstName'])-1)
        print(rnd_int) 
        data_rows.append(
            [
                rand_id(5,'num'),
                data['data']["data"]['firstName'][rnd_int] + " " + data['data']["data"]['lastName'][generate_random_int(0,len(data['data']['data']['lastName'])-1)],
                generate_random_int(1,100),
                data['data']['data']["firstName"][rnd_int] +"@"+ f"{rand_id(5,'alpha')}" +".com"
            ]
        )
        i+=1
    return generate_csv(f"{rand_id(10,'alpha')}.csv", headers, data_rows)