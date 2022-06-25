import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class calculatorGateway:
    name = 'calculator_gateway'

    calculator_rpc = RpcProxy('calculator_service')

    @http('GET', '/prime/<int:index>')
    def prime(self, request, index):
        prime = self.calculator_rpc.prime(index)
        return 200, json.dumps(prime)

    @http('GET', '/prime/palindrome/<int:index>')
    def prime_palindrome(self, request, index):
        prime_palindrome = self.calculator_rpc.prime_palindrome(index)
        return 200, json.dumps(prime_palindrome)
