import random
import time
import multiprocessing

def create_file(folder, file_num):
    file = open(f"{folder}\{file_num}.txt", "w" )
    
    for _ in range(1000000):
        line = random.randint(1, 100)
        file.write(str(line) + "\n")

    file.close()


def sequential():
    for file_num in range(10):
        create_file("seq", file_num)

def multiprocess():
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_cores)

    pool.starmap(create_file, [("multi", k) for k in range(10)])
 
        



if __name__ == "__main__":
    start = time.time()
    sequential()
    end = time.time()
    print("sequential time : " , end-start)
    
    
    start = time.time()
    multiprocess()
    end = time.time()
    print("multiprocess time : " , end-start)
