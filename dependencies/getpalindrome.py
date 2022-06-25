from celery import Celery

palindrome = Celery('palindrome', broker='redis://localhost:6379/0',
                    backend='redis://localhost:6379/0')

palindrome.conf.task_routes = {
    'dependencies.getpalindrome.getpalindrome': {'queue': 'palindrome'}
}


@palindrome.task
def getpalindrome(index):
    a = 1
    target = 0
    count = 1
    i = 0
    if index == 1:
        return 2
    else:
        while True:
            y = True
            if(str(i) == str(i)[::-1]):
                if(i > 2):
                    for a in range(2, i):
                        if(i % a == 0):
                            y = False
                            break
                    if y:
                        target = i
                        count += 1
                        if count == index:
                            break
            i += 1

        return target
