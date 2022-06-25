from celery import Celery

prime = Celery('prime', broker='redis://localhost:6379/0',
                  backend='redis://localhost:6379/0')

prime.conf.task_routes = {
    'getprime.getprime': {'queue': 'prime'}
}

@prime.task
def getprime(index):
    count = 0
    start = 2 
    target = 0
    end = 8

    while(count < end):
        prime = True
        for i in range(2, start):
            if(start % i == 0):
                prime = False
            if (prime):
                if count == end - 1:
                    target = start
            count += 1
        start += 1

    return target
