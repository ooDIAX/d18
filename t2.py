import random
import multiprocessing
import threading
import time

lock = threading.Lock()

def add_num():
    
    sum = 0
    for _ in range(10):
        lock.acquire()

        file = open("t2/file.txt", "a" )
        line = random.randint(1, 10)
        sum += line
        file.write(str(line) + "\n")
        file.close()
        lock.release()

    print(sum)
    mod_num(0)

    

def mod_num(line):

    lock.acquire()

    file = open(f"t2/file.txt", "r" )
    file1 = file.readlines()
    file1[line] = str(random.randint(1, 10)) + "\n"
    file.close()
    file = open(f"t2/file.txt", "w" )
    file.writelines(file1)
    file.close()

    lock.release()

    time.sleep(0.3)
    mod_num( (line+1) % 10)


def print_sum():
    lock.acquire()
    
    file = open(f"t2/file.txt", "r" )
    file1 = file.readlines()
    sum = 0
    if(len(file1) == 10):
        
        for line in file1:
            sum += int(line)
    lock.release()

    print("sum :", sum)
    time.sleep(0.3)
    print_sum()
 
        



if __name__ == "__main__":

    file = open("t2/file.txt", "w" )
    file.close()

    
    thread1 = threading.Thread(target = add_num, args = ())
    thread2 = threading.Thread(target = print_sum, args = ())

    thread1.start()
    thread2.start()
    # add_num()