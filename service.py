from nameko.rpc import rpc
import time
from dependencies.getprime import getprime, prime
from dependencies.getpalindrome import getpalindrome, palindrome
from celery.result import AsyncResult


class calculator_service:
    name = "calculator_service"

    @rpc
    def prime(self, index):
        num = getprime.apply_async([index])
        result = AsyncResult(num.id, app=prime)
        return result.get()

    @rpc
    def prime_palindrome(self, index):
        num = getpalindrome.apply_async([index])
        result = AsyncResult(num.id, app=palindrome)
        return result.get()
