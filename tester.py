from executioner_worker import tasks

re = tasks.execute.delay("print('h')","python3",["",""],["h","he"])
print(re.get(timeout=12))